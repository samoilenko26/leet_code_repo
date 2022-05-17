
CREATE TABLE t_push_notify (
    a_shop_id               INT             NOT NULL REFERENCES t_shops (a_id),
    a_notify_date           DATE            NOT NULL,
    a_budget_month          DATE            NOT NULL,
    a_notify_reason         VARCHAR(255)    NOT NULL

);