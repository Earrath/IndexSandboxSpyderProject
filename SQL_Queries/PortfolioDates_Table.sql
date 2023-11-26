USE indexSandbox;
GO

-- Drop tables if they exist
IF OBJECT_ID('portfolioDates_log', 'U') IS NOT NULL
    DROP TABLE portfolioDates_log;
GO

IF OBJECT_ID('portfolioDates', 'U') IS NOT NULL
    DROP TABLE portfolioDates;
GO

-- Create the main portfolioDates table with composite primary key
CREATE TABLE portfolioDates (
    portfolioID INT,
    date DATETIME,
    PRIMARY KEY (portfolioID, date)
);
GO

-- Create the log table for portfolioDates with date column
CREATE TABLE portfolioDates_log (
    logID INT IDENTITY(1,1) PRIMARY KEY,
    portfolioID INT,
    date DATETIME,
    logModTime DATETIME,
    userType NVARCHAR(255),
    modificationType NVARCHAR(50)
);
GO

-- Triggers for INSERT, UPDATE, and DELETE operations
-- Trigger for INSERT operations
CREATE TRIGGER trg_portfolioDates_insert
ON portfolioDates
AFTER INSERT
AS
BEGIN
    INSERT INTO portfolioDates_log (portfolioID, date, logModTime, userType, modificationType)
    SELECT i.portfolioID, i.date, GETDATE(), SUSER_SNAME(), 'INSERT'
    FROM inserted i;
END;
GO

-- Trigger for UPDATE operations
CREATE TRIGGER trg_portfolioDates_update
ON portfolioDates
AFTER UPDATE
AS
BEGIN
    INSERT INTO portfolioDates_log (portfolioID, date, logModTime, userType, modificationType)
    SELECT i.portfolioID, i.date, GETDATE(), SUSER_SNAME(), 'UPDATE'
    FROM inserted i
    INNER JOIN deleted d ON i.portfolioID = d.portfolioID;
END;
GO

-- Trigger for DELETE operations
CREATE TRIGGER trg_portfolioDates_delete
ON portfolioDates
AFTER DELETE
AS
BEGIN
    INSERT INTO portfolioDates_log (portfolioID, date, logModTime, userType, modificationType)
    SELECT d.portfolioID, d.date, GETDATE(), SUSER_SNAME(), 'DELETE'
    FROM deleted d;
END;
GO
