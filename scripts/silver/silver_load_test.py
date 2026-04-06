from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, text
import urllib

server = 'BRIAN\SQLEXPRESS' 
database = 'DataWarehouse'
driver = 'ODBC Driver 17 for SQL Server'

#Build the connection string
params = urllib.parse.quote_plus(
    f'DRIVER={{{driver}}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;' # Use 'yes' for Windows Auth, or UID/PWD for SQL Auth
)

#Create the engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
#%%
with engine.connect() as connection:
    result = connection.execute(text("SELECT @@VERSION"))
    for row in result:
        print(f"Connected to: {row[0]}")

#If you want to truncate a table before loading
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE silver.crm_cust_info"))
    conn.commit() # SQL Alchemy needs to commit

#Read Data
df_bronze = pd.read_sql("SELECT * FROM silver.crm_cust_info", engine)
