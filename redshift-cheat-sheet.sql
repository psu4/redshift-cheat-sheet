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

-- 1.e. show primiary keys of a table

select tco.constraint_schema,
       tco.constraint_name,
       kcu.ordinal_position as position,
       kcu.column_name as key_column,
       kcu.table_schema || '.' || kcu.table_name as table
from information_schema.table_constraints tco
join information_schema.key_column_usage kcu 
     on kcu.constraint_name = tco.constraint_name
     and kcu.constraint_schema = tco.constraint_schema
     and kcu.constraint_name = tco.constraint_name
where tco.constraint_type = 'PRIMARY KEY'
order by tco.constraint_schema,
         tco.constraint_name,
         kcu.ordinal_position;


--2. update tips

-- 2.a. update a object within the json column

update abc

set json = (regexp_replace(json::text, '"owner": "abc@zoo.com"', '"owner": "xyz@zoo.com"')::json)

where owner='abc@zoo.com' ;

--3. Json extract tips

-- 3.a postgresql extract json columns

-- https://stackoverflow.com/questions/32626261/how-to-parse-json-in-postgresql

SELECT
    column_name::json->'key_name' as new_column_name

    FROM table ;



-- 3.b redshift  extract json columns

--https://docs.aws.amazon.com/redshift/latest/dg/JSON_EXTRACT_PATH_TEXT.html

SELECT json_extract_path_text(column_name,'key_name', true) FROM table_name;

-- 3.c. Replace a json object based on the key

update table_name

set coumn_name = (regexp_replace(column_name::text, '"key": "old_value"', '"key": "new_value"')::json);

