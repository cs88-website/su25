CREATE TABLE family AS
    SELECT "Kim" AS first_name, "Kardashian" AS last_name, "Kris" AS parent_one,  "Robert" AS parent_two UNION
    SELECT "Kourtney",          "Kardashian",              "Kris",                "Robert" UNION
    SELECT "Khloe",             "Kardashian",              "Kris",                "Robert" UNION
    SELECT "Rob",               "Kardashian",              "Kris",                "Robert" UNION
    SELECT "Kendall",           "Jenner",                  "Kris",                "Caitlyn" UNION
    SELECT "Kylie",             "Jenner",                  "Kris",                "Caitlyn" UNION
    SELECT "Mason",             "Disick",                  "Kourtney",            "Scott" UNION
    SELECT "Penelope",          "Disick",                  "Kourtney",            "Scott" UNION
    SELECT "Reign",             "Disick",                  "Kourtney",            "Scott" UNION
    SELECT "North",             "West",                    "Kim",                 "Kanye" UNION
    SELECT "Saint",             "West",                    "Kim",                 "Kanye" UNION
    SELECT "Chicago",           "West",                    "Kim",                 "Kanye" UNION
    SELECT "Psalm",             "West",                    "Kim",                 "Kanye" UNION
    SELECT "True",              "Thompson",                "Khloe",               "Tristan" UNION
    SELECT "Dream",             "Kardashian",              "Rob",                 "Blac" UNION
    SELECT "Stormi",            "Webster",                 "Kylie",               "Travis";

-- source: https://pagesix.com/article/kardashian-jenner-family-tree/

CREATE TABLE net_worth AS
    SELECT "Kim" AS name, 1000 AS net_worth UNION
    SELECT "Kanye",       6600 UNION
    SELECT "Kylie",        700 UNION
    SELECT "Kris",         190 UNION
    SELECT "Khloe",         40 UNION
    SELECT "Kendall",       18 UNION
    SELECT "Travis",        39.5 UNION
    SELECT "Kourtney",      35 UNION
    SELECT "Caitlyn",      100 UNION
    SELECT "Scott",         40 UNION
    SELECT "Tristan",       45 UNION
    SELECT "Rob",           10 UNION
    SELECT "Robert",        30;

-- source: https://www.harpersbazaar.com/celebrity/latest/a22117965/kardashian-family-net-worth/
-- source: https://www.celebritynetworth.com/richest-businessmen/lawyers/robert-kardashian-net-worth/

