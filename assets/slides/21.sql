-- Lecture 21: Tables

CREATE TABLE prices AS
  SELECT "soda" AS name, 1.1 AS price UNION
  SELECT "burger"          , 3.50        UNION
  SELECT "fries"        , 2.0           UNION
  SELECT "hot cocoa"         , 0.90 UNION
  SELECT "coffee", 0.75;

CREATE TABLE orders AS
  SELECT "soda" AS name, 20 AS quantity_sold UNION
  SELECT "burger", 13 UNION
  SELECT "fries", 25 UNION
  SELECT "hot cocoa", 11 UNION
  SELECT "secret item", 1;

-----------------------
---- BEGIN DEMO 00 ----
-----------------------
----------
-- Dogs --
----------

CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

-- Fur
CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur UNION
  SELECT "bella"      , "short"       UNION
  SELECT "charlie"    , "long"        UNION
  SELECT "daisy"      , "long"        UNION
  SELECT "ellie"      , "short"       UNION
  SELECT "finn"       , "curly"       UNION
  SELECT "ginger"     , "short"        UNION
  SELECT "hank"       , "curly";

-- Parents of curly dogs
SELECT parent FROM parents, dogs WHERE child = name AND fur = "curly";

-----------------------
---- END DEMO 00 ----
-----------------------

-----------------------
---- BEGIN DEMO 01 ----
-----------------------

-- this query throws an error: ambiguous column name: name
SELECT name, price, quantity_sold FROM prices, orders where prices.name = orders.name;

-- to fix this, use explicit names
SELECT prices.name, price, quantity_sold FROM prices, orders where prices.name = orders.name;

-- (better style) fully qualify all names
SELECT prices.name, prices.price, orders.quantity_sold FROM prices, orders where prices.name = orders.name;


-- Dog Siblings
-- first try: get "ambiguous column name" error message
SELECT child AS first, child AS second
  FROM parents, parents
  WHERE parent = parent;

-- fix: use table aliases a, b
-- first try: yields undesirable rows, duplicates ("bella|bella")
-- and different orderings ("bella|charlie" vs "charlie|bella")
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent;

-- fix attempt: a.child != b.child (in SQL syntax, != is also <>)
-- doesn't fix ordering issue though
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child != b.child;

-- final fix: clever use of comparison operator
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- expressed via `join` keyword
SELECT a.child AS first, b.child AS second
  FROM parents AS a
  JOIN parents AS b
  ON a.parent = b.parent
  WHERE a.child < b.child;

-- Grandparents
CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS granpup
    FROM parents AS a, parents AS b
    WHERE b.parent = a.child;

-- Grandogs with the same fur AS their granpups
SELECT grandog, granpup, c.fur FROM grandparents, dogs AS c, dogs AS d
  WHERE grandog = c.name AND
        granpup = d.name AND
        c.fur = d.fur;

-----------------------
---- END DEMO 01 ----
-----------------------

-----------------------
---- BEGIN DEMO 02 ----
-----------------------
-- Dog triples
SELECT a.name, b.name, c.name FROM dogs AS a, dogs AS b, dogs AS c
  WHERE a.name > b.name AND b.name > c.name AND a.fur = b.fur AND b.fur = c.fur;
-----------------------
---- END DEMO 02 ----
-----------------------

