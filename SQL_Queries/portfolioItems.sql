-- Create the main bond portfolio table
CREATE TABLE portfolioItems (
    portfolioID NVARCHAR(255),
    portfolioDate DATE,
    profileDate DATE,
    bondID NVARCHAR(255),
    isin NVARCHAR(255),
    issuer NVARCHAR(255),
    issueDate DATE,
    maturityDate DATE,
    couponRate DECIMAL(10, 2),
    faceValue DECIMAL(18, 2),
    marketValue DECIMAL(18, 2),
    currency NVARCHAR(3),
    moodysRating NVARCHAR(255),
    spRating NVARCHAR(255),
    fitchRating NVARCHAR(255),
    sector NVARCHAR(255),
    referenceRate NVARCHAR(255),
    seniority NVARCHAR(255),
    typeOfBond NVARCHAR(255),
    weight DECIMAL(10, 2)
);
GO

-- Create the log table for the bond portfolio table
CREATE TABLE portfolioItems_log (
    logID INT IDENTITY(1,1) PRIMARY KEY,
    portfolioID NVARCHAR(255),
    portfolioDate DATE,
    profileDate DATE,
    bondID NVARCHAR(255),
    isin NVARCHAR(255),
    issuer NVARCHAR(255),
    issueDate DATE,
    maturityDate DATE,
    couponRate DECIMAL(10, 2),
    faceValue DECIMAL(18, 2),
    marketValue DECIMAL(18, 2),
    currency NVARCHAR(3),
    moodysRating NVARCHAR(255),
    spRating NVARCHAR(255),
    fitchRating NVARCHAR(255),
    sector NVARCHAR(255),
    referenceRate NVARCHAR(255),
    seniority NVARCHAR(255),
    typeOfBond NVARCHAR(255),
    weight DECIMAL(10, 2),
    logModTime DATETIME DEFAULT GETDATE(),
    userType NVARCHAR(255),
    modificationType NVARCHAR(50)
);
GO

-- Trigger for INSERT operation on portfolioItems
CREATE TRIGGER trg_portfolioItems_Insert
ON portfolioItems
AFTER INSERT
AS
BEGIN
    INSERT INTO portfolioItems_log (portfolioID, portfolioDate, profileDate, bondID, isin, issuer, issueDate, maturityDate, couponRate, faceValue, marketValue, currency, moodysRating, spRating, fitchRating, sector, referenceRate, seniority, typeOfBond, weight, userType, modificationType)
    SELECT portfolioID, portfolioDate, profileDate, bondID, isin, issuer, issueDate, maturityDate, couponRate, faceValue, marketValue, currency, moodysRating, spRating, fitchRating, sector, referenceRate, seniority, typeOfBond, weight, SUSER_SNAME(), 'INSERT'
    FROM inserted;
END;
GO

-- Trigger for UPDATE operation on portfolioItems
CREATE TRIGGER trg_portfolioItems_Update
ON portfolioItems
AFTER UPDATE
AS
BEGIN
    INSERT INTO portfolioItems_log (portfolioID, portfolioDate, profileDate, bondID, isin, issuer, issueDate, maturityDate, couponRate, faceValue, marketValue, currency, moodysRating, spRating, fitchRating, sector, referenceRate, seniority, typeOfBond, weight, userType, modificationType)
    SELECT portfolioID, portfolioDate, profileDate, bondID, isin, issuer, issueDate, maturityDate, couponRate, faceValue, marketValue, currency, moodysRating, spRating, fitchRating, sector, referenceRate, seniority, typeOfBond, weight, SUSER_SNAME(), 'UPDATE'
    FROM inserted;
END;
GO

-- Trigger for DELETE operation on portfolioItems
CREATE TRIGGER trg_portfolioItems_Delete
ON portfolioItems
AFTER DELETE
AS
BEGIN
    INSERT INTO portfolioItems_log (portfolioID, portfolioDate, profileDate, bondID, isin, issuer, issueDate, maturityDate, couponRate, faceValue, marketValue, currency, moodysRating, spRating, fitchRating, sector, referenceRate, seniority, typeOfBond, weight, userType, modificationType)
    SELECT portfolioID, portfolioDate, profileDate, bondID, isin, issuer, issueDate, maturityDate, couponRate, faceValue, marketValue, currency, moodysRating, spRating, fitchRating, sector, referenceRate, seniority, typeOfBond, weight, SUSER_SNAME(), 'DELETE'
    FROM deleted;
END;
GO
