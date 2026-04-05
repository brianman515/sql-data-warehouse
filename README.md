# sql-data-warehouse
Data warehouse with SQL Server, incl. ETL processes, data modelling and analytics

**Guidelines:**

naming: lower_case (ie. customer_id)

language: english

avoid reserved keywords

Bronze Rules:

- all names must start with source system name, and table names must match their original names without renaming
- <sourcesystem><entity>
    - <sourcesystem>: crm or erp
    - <entity>: exact table name from the source system
    - Example: crm_customer_info

Silver Rules:

- all names must start with source system name, and table names must match their original names without renaming
- <sourcesystem><entity>
    - <sourcesystem>: crm or erp
    - <entity>: exact table name from the source system
    - Example: crm_customer_info

Gold Rules:

- all names must be meaningful, business-aligned names, starting with category prefix
- <category><entity>
    - <category>: describes the role of the table such as dim or fact or agg
    - <entity>: descriptive name of variable, aligned with business domain (e.g. customers, products, sales)

**Column Naming:**

Surrogate Keys:

- all primary keys in dim tables must use the suffix _key
- <table_name>_key
    - <table_name>: name of table
    - _key: suffix indicating that this column is a surrogate key
    - Example: customer_key

Technical Columns:

- All technical columns must start with prefix dwh_, followed by a descriptive name indicating the column’s purpose
- dwh_<column_name>
    - dwh: prefix exclusive for system-generated metadata
    - Example: dwh_load_date → System generated column used to store the date when the record was loaded

**Stored Procedure:**

- All stored procedures used for loading data must follow the same naming pattern:
- load_<layer>
    - <layer>: represents the layer being loaded: gold, silver, bronze
