/*
CREATE DATABASE AND SCHEMAS

Purpose: Creates a new database 'DataWarehouse' after checking if it already exists.
If it exists, it is dropped and a new one created.
Additionally three schemas are setup bronze silver and gold.

WARNING:
Running this will drop the entire database if it exists. All data is deleted.
Ensure proper backups.

*/

USE master;
GO

-- drop and recreate the database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'DataWarehouse')
BEGIN
    ALTER DATABASE DataWarehouse SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE DataWarehouse
END; 
GO


CREATE DATABASE DataWarehouse;
GO
USE DataWarehouse;
GO

-- create schemas
CREATE SCHEMA bronze;
GO
CREATE SCHEMA silver;
GO
CREATE SCHEMA gold;
GO
