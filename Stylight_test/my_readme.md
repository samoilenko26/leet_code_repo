
Does your solution avoid sending duplicate notifications?
Yes. The notifications will be sent twice if the store reached 50% and 100% in a month. Other notifications will not be sent. The database has t_push_notify table that contains attributes "a_budget_month" and "a_notify_reason". 
"a_budget_month" - for which budget the notification was sent
"a_notify_reason" - the reason of the notification was sent
The algorithm checks this attributes befoe sending notofiacation. 
So the users will not get notification twise about the same event
See method is_notified() 

How does your solution handle a budget change after a notification has already been sent?
Notification will be sent once when 50% is reached. If there are new updates in the budget table in the range of 50-100%, this will not initiate a new notifications. If it reaches the limit of 100%, then the algorithm will initiate a new notification. It works thanks to the new t_push_notify table


Tech requirements:
DB: PostgresSQL 14
Python: 3.6

How to run the project:
python push_notify.py

Before run be sure that you have installed following libs:
psycopg2
datetime
python-dateutil