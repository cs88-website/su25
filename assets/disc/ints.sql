CREATE TABLE ints AS
  SELECT "zero" AS word, 0 AS one, 0 AS two, 0 AS four, 0 AS eight UNION
  SELECT "one"         , 1       , 0       , 0        , 0          UNION
  SELECT "two"         , 0       , 2       , 0        , 0          UNION
  SELECT "three"       , 1       , 2       , 0        , 0          UNION
  SELECT "four"        , 0       , 0       , 4        , 0          UNION
  SELECT "five"        , 1       , 0       , 4        , 0          UNION
  SELECT "six"         , 0       , 2       , 4        , 0          UNION
  SELECT "seven"       , 1       , 2       , 4        , 0          UNION
  SELECT "eight"       , 0       , 0       , 0        , 8          UNION
  SELECT "nine"        , 1       , 0       , 0        , 8;