
-- Drop the log table if it exists to avoid conflicts with foreign key constraints
IF OBJECT_ID('dbo.bondsInstruments_log', 'U') IS NOT NULL
    DROP TABLE dbo.bondsInstruments_log;
GO

-- Drop the main table if it exists
IF OBJECT_ID('dbo.bondsInstruments', 'U') IS NOT NULL
    DROP TABLE dbo.bondsInstruments;
GO

-- Creating the main bonds table
CREATE TABLE bondsInstruments (
    bondID NVARCHAR(255),
    ISIN NVARCHAR(255),
    Issuer NVARCHAR(255),
    IssueDate DATE,
    MaturityDate DATE,
    CouponRate FLOAT,
    FaceValue INT,
    MarketValue INT,
    Currency NVARCHAR(50),
    MoodysRating NVARCHAR(50),
    SPRating NVARCHAR(50),
    FitchRating NVARCHAR(50),
    Sector NVARCHAR(255),
    ReferenceRate NVARCHAR(255),
    Seniority NVARCHAR(255),
    TypeOfBond NVARCHAR(255),
    PRIMARY KEY (bondID)
);
GO

-- Creating the log table with all columns from the main table
CREATE TABLE bondsInstruments_log (
    LogID INT IDENTITY(1,1),
    bondID NVARCHAR(255),
    ISIN NVARCHAR(255),
    Issuer NVARCHAR(255),
    IssueDate DATE,
    MaturityDate DATE,
    CouponRate FLOAT,
    FaceValue INT,
    MarketValue INT,
    Currency NVARCHAR(50),
    MoodysRating NVARCHAR(50),
    SPRating NVARCHAR(50),
    FitchRating NVARCHAR(50),
    Sector NVARCHAR(255),
    ReferenceRate NVARCHAR(255),
    Seniority NVARCHAR(255),
    TypeOfBond NVARCHAR(255),
    LogModTime DATETIME DEFAULT GETDATE(),
    UserType NVARCHAR(255),
    ModificationType NVARCHAR(100)
    
);
GO

-- Drop the triggers if they exist
IF OBJECT_ID('dbo.trg_bondsInstruments_Insert', 'TR') IS NOT NULL
    DROP TRIGGER dbo.trg_bondsInstruments_Insert;
GO

IF OBJECT_ID('dbo.trg_bondsInstruments_Update', 'TR') IS NOT NULL
    DROP TRIGGER dbo.trg_bondsInstruments_Update;
GO

IF OBJECT_ID('dbo.trg_bondsInstruments_Delete', 'TR') IS NOT NULL
    DROP TRIGGER dbo.trg_bondsInstruments_Delete;
GO

-- Trigger for INSERT operations
CREATE TRIGGER trg_bondsInstruments_Insert
ON bondsInstruments
AFTER INSERT
AS
BEGIN
    INSERT INTO bondsInstruments_log (
        bondID,
        ISIN,
        Issuer,
        IssueDate,
        MaturityDate,
        CouponRate,
        FaceValue,
        MarketValue,
        Currency,
        MoodysRating,
        SPRating,
        FitchRating,
        Sector,
        ReferenceRate,
        Seniority,
        TypeOfBond,
        UserType,
        ModificationType
    )
    SELECT 
        i.bondID,
        i.ISIN,
        i.Issuer,
        i.IssueDate,
        i.MaturityDate,
        i.CouponRate,
        i.FaceValue,
        i.MarketValue,
        i.Currency,
        i.MoodysRating,
        i.SPRating,
        i.FitchRating,
        i.Sector,
        i.ReferenceRate,
        i.Seniority,
        i.TypeOfBond,
        SUSER_SNAME(),
        'INSERT'
    FROM inserted i;
END;
GO

-- Trigger for UPDATE operations
CREATE TRIGGER trg_bondsInstruments_Update
ON bondsInstruments
AFTER UPDATE
AS
BEGIN
    INSERT INTO bondsInstruments_log (
        bondID,
        ISIN,
        Issuer,
        IssueDate,
        MaturityDate,
        CouponRate,
        FaceValue,
        MarketValue,
        Currency,
        MoodysRating,
        SPRating,
        FitchRating,
        Sector,
        ReferenceRate,
        Seniority,
        TypeOfBond,
        UserType,
        ModificationType
    )
    SELECT 
        i.bondID,
        i.ISIN,
        i.Issuer,
        i.IssueDate,
        i.MaturityDate,
        i.CouponRate,
        i.FaceValue,
        i.MarketValue,
        i.Currency,
        i.MoodysRating,
        i.SPRating,
        i.FitchRating,
        i.Sector,
        i.ReferenceRate,
        i.Seniority,
        i.TypeOfBond,
        SUSER_SNAME(),
        'UPDATE'
    FROM inserted i;
END;
GO

-- Trigger for DELETE operations
CREATE TRIGGER trg_bondsInstruments_Delete
ON bondsInstruments
AFTER DELETE
AS
BEGIN
    INSERT INTO bondsInstruments_log (
        bondID,
        ISIN,
        Issuer,
        IssueDate,
        MaturityDate,
        CouponRate,
        FaceValue,
        MarketValue,
        Currency,
        MoodysRating,
        SPRating,
        FitchRating,
        Sector,
        ReferenceRate,
        Seniority,
        TypeOfBond,
        UserType,
        ModificationType
    )
    SELECT 
        d.bondID,
        d.ISIN,
        d.Issuer,
        d.IssueDate,
        d.MaturityDate,
        d.CouponRate,
        d.FaceValue,
        d.MarketValue,
        d.Currency,
        d.MoodysRating,
        d.SPRating,
        d.FitchRating,
        d.Sector,
        d.ReferenceRate,
        d.Seniority,
        d.TypeOfBond,
        SUSER_SNAME(),
        'DELETE'
    FROM deleted d;
END;
GO
