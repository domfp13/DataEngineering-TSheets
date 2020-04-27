-- # -*- coding: utf-8 -*-
-- # Created by Luis Fuentes

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
    notes           VARCHAR(255),
    customfields    VARCHAR(500),
    last_modified   VARCHAR(255)
);

-- Staging data into the Table Stage @%
PUT file://C:\Users\lf188653\Desktop\Data\global\TSHEETS\timesheets.csv @%T_TSHEETS_TIMESHEETS_STG/2020/04/27 AUTO_COMPRESS=true;

-- Listing out all the data stage for this table
LIST @%T_TSHEETS_TIMESHEETS_STG;

-- Loading data into tables requires a warehouse
ALTER WAREHOUSE BI_WH RESUME;
 
COPY INTO T_TSHEETS_TIMESHEETS_STG
  FROM @%T_TSHEETS_TIMESHEETS_STG/2020/04/27
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

--INSERT INTO <target_table> (col1, col2, etc) SELECT col1, PARSE_JSON(col2), etc, from <temp_table>;