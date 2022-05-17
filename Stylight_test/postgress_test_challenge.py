import dateutil
import psycopg2
from datetime import datetime
from dateutil.relativedelta import relativedelta

class PushNotify():

    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test_1")

    def read_from_db(self, postgreSQL_select_Query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(postgreSQL_select_Query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    def change_db(self, postgreSQL_select_Query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(postgreSQL_select_Query)
            self.connection.commit()
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while writing data to PostgreSQL", error)


    def push_notify(self, shop_info, budget_info, reason):
        current_date = datetime.now().strftime('%Y-%m-%d')
        shop_name = shop_info[1]
        current_months_budget = budget_info[1]
        current_expenditure = budget_info [3]
        percentage = (budget_info[3]*100)/budget_info[2]
        message = "Dear {shop_name}, inform you that to the date ({current_date}) you have spent {current_expenditure}. " \
                  "This is {percentage}% of your rate of month {current_months_budget}".format(shop_name=shop_name,
                                                                                                   current_date=current_date,
                                                                                                   current_expenditure=current_expenditure,
                                                                                                   percentage=percentage//1,
                                                                                                   current_months_budget=current_months_budget)
        print(message)
        current_month = datetime.now().strftime('%Y-%m')
        print()
        self.change_db("INSERT INTO t_push_notify VALUES ({}, '{}-01', '{}', '{}')".format(shop_info[0], current_month, current_months_budget, reason))

    def set_shop_offline(self, shop):
        self.change_db("UPDATE t_shops SET a_online = 0 WHERE a_id = {}".format(shop[0]))

    def is_notified(self, budget_info, t_push_notify, reason):
        for notify_info in t_push_notify:
            if notify_info[0] == budget_info[0] and notify_info[3] == reason and budget_info[1] == notify_info[2]:
                return True
        return False


    def send_notify_if_possible(self, number_of_previous_month):
        now_minus_number_of_previous_month = datetime.now() - relativedelta(months=number_of_previous_month)
        date_for_request = now_minus_number_of_previous_month.strftime('%Y-%m')
        t_budgets = self.read_from_db("SELECT * FROM t_budgets WHERE a_month > '{}-01'".format(date_for_request))
        t_push_notify = self.read_from_db("SELECT * FROM t_push_notify WHERE a_notify_date > '{}-01'".format(date_for_request))

        for budget_info in t_budgets:
            if (budget_info[3]*100)/budget_info[2] > 100:
                if not self.is_notified(budget_info, t_push_notify, "more than 100"):
                    shop_info = self.read_from_db("SELECT * FROM t_shops WHERE a_id = {}".format(budget_info[0]))
                    self.push_notify(shop_info[0], budget_info, reason="more than 100")
                    self.set_shop_offline(shop_info[0])

            elif (budget_info[3]*100)/budget_info[2] > 50:
                if not self.is_notified(budget_info, t_push_notify, "more than 50 and less 100"):
                    shop_info = self.read_from_db("SELECT * FROM t_shops WHERE a_id = {}".format(budget_info[0]))
                    self.push_notify(shop_info[0], budget_info, reason="more than 50 and less 100")


if __name__ == "__main__":
    push_notify = PushNotify()
    push_notify.send_notify_if_possible(number_of_previous_month=100)
