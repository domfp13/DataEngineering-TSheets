-- # -*- coding: utf-8 -*-
-- # Created by Luis Fuentes

-- Table creation
CREATE OR REPLACE TABLE T_TSHEETS_TIMESHEETS_STG
(
    id              VARCHAR(255),
    user_id         VARCHAR(255),
    jobcode_id      VARCHAR(255),
    start_date      VARCHAR(255),
    end_date        VARCHAR(255),
    duration        VARCHAR(255),
    date_date       VARCHAR(255),
    tz              VARCHAR(255),
    tz_str          VARCHAR(255),
    type_str        VARCHAR(255),
    location        VARCHAR(255),
    on_the_clock    VARCHAR(255),
    locked          VARCHAR(255),
    notes           VARCHAR(16777216),
    customfields    VARCHAR(16777216),
    last_modified   VARCHAR(255)
);

-- Staging data into the Table Stage @%
PUT file://C:\Users\lf188653\Desktop\Data\global\TSHEETS\timesheets.csv @%T_TSHEETS_TIMESHEETS_STG/2020/04 AUTO_COMPRESS=true;

LIST @%T_TSHEETS_TIMESHEETS_STG;

BEGIN;
TRUNCATE TABLE T_TSHEETS_TIMESHEETS_STG;

COPY INTO T_TSHEETS_TIMESHEETS_STG
  FROM @%T_TSHEETS_TIMESHEETS_STG/2020/04
  FILE_FORMAT = (TYPE='CSV'
                 FIELD_DELIMITER = ','
                 SKIP_HEADER = 1
                 VALIDATE_UTF8 = FALSE
                 TRIM_SPACE = FALSE
                 FIELD_OPTIONALLY_ENCLOSED_BY = '"' 
                 NULL_IF = ('null', ''))
  PATTERN = '.*.gz'
  ON_ERROR = 'skip_file'
  PURGE = TRUE;
  
COMMIT;
  
SELECT MAX(LEN(NOTES)), MAX(LEN(customfields))
FROM T_TSHEETS_TIMESHEETS_STG

SELECT * 
FROM T_TSHEETS_TIMESHEETS_STG
LIMIT 10;

--to_variant(customfields) AS customfields_new
--parse_json(customfields) AS customfields_new

WITH CTL AS (
  SELECT customfields, TRY_PARSE_JSON(customfields) AS customfields_new 
  FROM T_TSHEETS_TIMESHEETS_STG
)
SELECT customfields_new, customfields_new:"122645"    
FROM CTL;


