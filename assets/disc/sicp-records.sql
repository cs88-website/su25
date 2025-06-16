CREATE TABLE records AS
    SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "Wizard" AS title,
        60000 AS salary, "Oliver Warbucks" AS supervisor UNION
    SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
    SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
    SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
    SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" UNION
    SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
    SELECT "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" UNION
    SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge" UNION
    SELECT "Lana Lambda", "Administration", "Executive Director", 610000, "Lana Lambda";

CREATE TABLE salaries AS
    SELECT "Ben Bitdiddle" AS name, 60000 AS salary2022, 80000 AS salary2023 UNION
    SELECT "Alyssa P Hacker", 40000, 80000 UNION
    SELECT "Cy D Fect", 35000, 74000 UNION
    SELECT "Lem E Tweakit", 25000, 28000 UNION
    SELECT "Louis Reasoner", 30000, 30000 UNION
    SELECT "Oliver Warbucks", 150000, 120000 UNION
    SELECT "Eben Scrooge", 75000, 76000 UNION
    SELECT "Robert Cratchet", 18000, 20000 UNION
    SELECT "Lana Lambda", 610000, 610000;

CREATE TABLE meetings AS
    SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
    SELECT "Computer", "Wednesday", "4pm" UNION
    SELECT "Administration", "Monday", "11am" UNION
    SELECT "Administration", "Wednesday", "4pm";
