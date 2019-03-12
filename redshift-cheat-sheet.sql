-- By Pin-Chih Su

-- 1. table tips

-- 1.a. alter table

ALTER TABLE mqt_tabviews.fraud_rule_violations ADD COLUMN mcc_description varchar(1000) default NULL;

-- 1.b. check user permissions

SELECT
    u.usename,
    s.schemaname,
    has_schema_privilege(u.usename,s.schemaname,'create') AS user_has_select_permission,
    has_schema_privilege(u.usename,s.schemaname,'usage') AS user_has_usage_permission
FROM
    pg_user u
CROSS JOIN
    (SELECT DISTINCT schemaname FROM pg_tables) s
WHERE
    u.usename = 'user-name-variable'

;

-- 1.c. check if a table exists or not

SELECT * FROM information_schema.tables where table_name='table-name';

-- 1.d. check if a column exists or not

SELECT EXISTS (

SELECT * FROM information_schema.columns where table_name='name' and column_name='name' ); -- return true or false


--2. update tips

-- 2.a. update a object within the json column

update abc

set json = (regexp_replace(json::text, '"owner": "abc@zoo.com"', '"owner": "xyz@zoo.com"')::json)

where owner='abc@zoo.com' ;
