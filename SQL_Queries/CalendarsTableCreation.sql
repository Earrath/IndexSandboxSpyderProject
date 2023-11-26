USE indexSandbox;
GO

-- Drop tables if they exist
IF OBJECT_ID('calendars_log', 'U') IS NOT NULL
    DROP TABLE calendars_log;
GO

IF OBJECT_ID('calendars', 'U') IS NOT NULL
    DROP TABLE calendars;
GO

-- Create the main calendars table with composite primary key
CREATE TABLE calendars (
    calendarID INT,
    date DATETIME,
    holiday NVARCHAR(255),
    weekday NVARCHAR(50),
    month INT,
    day INT,
    year INT,
    daytype INT,
    PRIMARY KEY (calendarID, date)
);
GO

-- Create the log table for calendars with date column
CREATE TABLE calendars_log (
    logID INT IDENTITY(1,1) PRIMARY KEY,
    calendarID INT,
    date DATETIME,
    logModTime DATETIME,
    userType NVARCHAR(255),
    modificationType NVARCHAR(50)
);
GO

-- Triggers for INSERT, UPDATE, and DELETE operations
-- Trigger for INSERT operations
CREATE TRIGGER trg_calendars_insert
ON calendars
AFTER INSERT
AS
BEGIN
    INSERT INTO calendars_log (calendarID, date, logModTime, userType, modificationType)
    SELECT i.calendarID, i.date, GETDATE(), SUSER_SNAME(), 'INSERT'
    FROM inserted i;
END;
GO

-- Trigger for UPDATE operations
CREATE TRIGGER trg_calendars_update
ON calendars
AFTER UPDATE
AS
BEGIN
    INSERT INTO calendars_log (calendarID, date, logModTime, userType, modificationType)
    SELECT i.calendarID, i.date, GETDATE(), SUSER_SNAME(), 'UPDATE'
    FROM inserted i
    INNER JOIN deleted d ON i.calendarID = d.calendarID;
END;
GO

-- Trigger for DELETE operations
CREATE TRIGGER trg_calendars_delete
ON calendars
AFTER DELETE
AS
BEGIN
    INSERT INTO calendars_log (calendarID, date, logModTime, userType, modificationType)
    SELECT d.calendarID, d.date, GETDATE(), SUSER_SNAME(), 'DELETE'
    FROM deleted d;
END;
GO
