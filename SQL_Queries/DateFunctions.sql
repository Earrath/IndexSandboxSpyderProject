use indexSandbox
GO

-- Drop the previous date function if it exists
IF OBJECT_ID('dbo.GetPrevious_Date', 'FN') IS NOT NULL
    DROP FUNCTION dbo.GetPrevious_Date;
GO

-- Drop the end of month date function if it exists
IF OBJECT_ID('dbo.GetEOM_Date', 'FN') IS NOT NULL
    DROP FUNCTION dbo.GetEOM_Date;
GO

-- Drop the next date function if it exists
IF OBJECT_ID('dbo.GetNext_Date', 'FN') IS NOT NULL
    DROP FUNCTION dbo.GetNext_Date;
GO

-- Drop the previous month end date function if it exists
IF OBJECT_ID('dbo.GetPrevious_EOM_Date', 'FN') IS NOT NULL
    DROP FUNCTION dbo.GetPrevious_EOM_Date;
GO

-- Drop the first day of the month function if it exists
IF OBJECT_ID('dbo.GetBOM_Date', 'FN') IS NOT NULL
    DROP FUNCTION dbo.GetBOM_Date;
GO
-- Create function to get the previous date from the calendar table
CREATE FUNCTION dbo.GetPrevious_Date(@CalendarID INT, @Date DATE)
RETURNS DATE
AS
BEGIN

    DECLARE @PreviousDate DATE;

    SELECT TOP 1 @PreviousDate = c.date
    FROM indexSandbox..calendars c
    WHERE c.calendarID = @CalendarID	
	AND c.date < @Date 
	AND daytype = 0						--DayType 0 is business day.
    ORDER BY c.date DESC;

    RETURN @PreviousDate;
END;
GO


-- Create function to get the end of month date from the calendar table
CREATE FUNCTION dbo.GetEOM_Date(@CalendarID INT, @Date DATE)
RETURNS DATE
AS
BEGIN
    DECLARE @EndOfMonthDate DATE;

    -- Set the date to the first day of the next month
    SET @Date = DATEADD(MONTH, DATEDIFF(MONTH, 0, @Date) + 1, 0);

    -- Retrieves the latest date in the previous month where daytype = 0 for the given calendarID
    SELECT TOP 1 @EndOfMonthDate = c.date
    FROM indexSandbox..calendars c
    WHERE c.calendarID = @CalendarID AND c.date < @Date AND c.daytype = 0
    ORDER BY c.date DESC;

    RETURN @EndOfMonthDate;
END;
GO


-- Create function to get the previous month end date from the calendar table
CREATE FUNCTION dbo.GetPrevious_EOM_Date(@CalendarID INT, @Date DATE)
RETURNS DATE
AS
BEGIN
    DECLARE @PreviousMonthEndDate DATE;

    -- Find the first day of the current month
    DECLARE @FirstDayOfCurrentMonth DATE = DATEADD(MONTH, DATEDIFF(MONTH, 0, @Date), 0);

    -- Find the last day of the previous month
    DECLARE @LastDayOfPreviousMonth DATE = DATEADD(DAY, -1, @FirstDayOfCurrentMonth);

    -- Retrieve the latest date in the previous month where daytype = 0 for the given calendarID
    SELECT TOP 1 @PreviousMonthEndDate = c.date
    FROM indexSandbox..calendars c
    WHERE c.calendarID = @CalendarID AND c.date <= @LastDayOfPreviousMonth AND c.daytype = 0
    ORDER BY c.date DESC;

    RETURN @PreviousMonthEndDate;
END;
GO


-- Create function to get the next date from the calendar table
CREATE FUNCTION dbo.GetNext_Date(@CalendarID INT, @Date DATE)
RETURNS DATE
AS
BEGIN
    DECLARE @NextDate DATE;

    -- Retrieve the earliest date after @Date where daytype = 0 for the given calendarID
    SELECT TOP 1 @NextDate = c.date
    FROM indexSandbox..calendars c
    WHERE c.calendarID = @CalendarID AND c.date > @Date AND c.daytype = 0
    ORDER BY c.date ASC;

    RETURN @NextDate;
END;
GO





-- Create function to get the first day of the month from the calendar table
CREATE FUNCTION dbo.GetBOM_Date(@CalendarID INT, @Date DATE)
RETURNS DATE
AS
BEGIN
    DECLARE @FirstDayOfMonth DATE;

    -- Find the first day of the month for the given @Date
    DECLARE @FirstDayOfGivenMonth DATE = DATEADD(MONTH, DATEDIFF(MONTH, 0, @Date), 0);

    -- Retrieve the earliest date in the month where daytype = 0 for the given calendarID
    SELECT TOP 1 @FirstDayOfMonth = c.date
    FROM indexSandbox..calendars c
    WHERE c.calendarID = @CalendarID AND c.date >= @FirstDayOfGivenMonth AND c.daytype = 0
    ORDER BY c.date ASC;

    RETURN @FirstDayOfMonth;
END;
GO






use indexSandbox
GO

DECLARE @CalendarID INT = 1;  -- Example CalendarID
DECLARE @SomeDate DATE = '2021-05-03';  -- Example Date

SELECT dbo.GetPrevious_Date(@CalendarID, @SomeDate) AS PreviousDate,
 dbo.GetEOM_Date(@CalendarID, @SomeDate) AS GetEOM_Date,
 dbo.GetPrevious_EOM_Date(@CalendarID, @SomeDate) AS GetPrevious_EOM_Date,
 dbo.GetNext_Date(@CalendarID, @SomeDate) AS GetNext_Date,
 dbo.GetBOM_Date(@CalendarID, @SomeDate) AS GetBOM_Date
 
select *from indexSandbox..calendars