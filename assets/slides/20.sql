-- Lecture 20: SQL

-- Demo00
-- can prepopulate this data by doing:
-- python3 sqlite_shell.py --init 20.sql
CREATE TABLE employees AS
  SELECT "Alyssa P. Hacker" AS name, "Software Engineer" AS title, 120000 AS salary UNION
  SELECT "Oliver Warbucks", "Boss", 1000000 UNION
  SELECT "Louis Reasoner", "Software Engineer Intern", 30000 UNION
  SELECT "John Doe", "Software Engineer", 90000 UNION
  SELECT "Jane Doe", "Software Engineer", 90000;

-- can ask several questions of this table, like:
-- show all rows
-- select * from employees;
-- show only specific columns:
-- select name, salary from employees;

-- can ask more complicated queries, like:
-- the average salary by job title:
-- select title, avg(salary) from employees group by title;
