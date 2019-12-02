
### 1. ad hoc queries to see if a DAG runs or not

SELECT
  *
FROM task_instance
where dag_id like 'whatever'
order by start_date desc
limit 100;



