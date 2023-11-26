-- Create main lookup table
CREATE TABLE lkup_portfolio_details (
    portfolioID INT PRIMARY KEY,
    portfolioName VARCHAR(255),
    portfolioDescription VARCHAR(255),
    parentPortfolioID INT
);

-- Create log table
CREATE TABLE lkup_portfolio_details_log (
    logID INT PRIMARY KEY AUTO_INCREMENT,
    portfolioID INT,
    portfolioName VARCHAR(255),
    portfolioDescription VARCHAR(255),
    parentPortfolioID INT,
    logModTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    userType VARCHAR(255),
    modificationType VARCHAR(50)
);

-- Trigger for INSERT operation
DELIMITER //
CREATE TRIGGER after_lkup_portfolio_details_insert
AFTER INSERT ON lkup_portfolio_details
FOR EACH ROW
BEGIN
    INSERT INTO lkup_portfolio_details_log (portfolioID, portfolioName, portfolioDescription, parentPortfolioID, userType, modificationType)
    VALUES (NEW.portfolioID, NEW.portfolioName, NEW.portfolioDescription, NEW.parentPortfolioID, 'userTypeValue', 'INSERT');
END;
//

-- Trigger for UPDATE operation
CREATE TRIGGER after_lkup_portfolio_details_update
AFTER UPDATE ON lkup_portfolio_details
FOR EACH ROW
BEGIN
    INSERT INTO lkup_portfolio_details_log (portfolioID, portfolioName, portfolioDescription, parentPortfolioID, userType, modificationType)
    VALUES (NEW.portfolioID, NEW.portfolioName, NEW.portfolioDescription, NEW.parentPortfolioID, 'userTypeValue', 'UPDATE');
END;
//

-- Trigger for DELETE operation
CREATE TRIGGER after_lkup_portfolio_details_delete
AFTER DELETE ON lkup_portfolio_details
FOR EACH ROW
BEGIN
    INSERT INTO lkup_portfolio_details_log (portfolioID, portfolioName, portfolioDescription, parentPortfolioID, userType, modificationType)
    VALUES (OLD.portfolioID, OLD.portfolioName, OLD.portfolioDescription, OLD.parentPortfolioID, 'userTypeValue', 'DELETE');
END;
//
DELIMITER ;
