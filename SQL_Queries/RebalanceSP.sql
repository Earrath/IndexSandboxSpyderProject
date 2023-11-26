-- Template for creating a stored procedure in SQL Server

CREATE PROCEDURE ProcedureName 
    -- Add the parameters for the stored procedure here
    @Param1 DataType1, 
    @Param2 DataType2 OUTPUT, -- Example of an OUTPUT parameter
    ...
AS
BEGIN
    -- Set NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert statements for the stored procedure here
    -- Example: SELECT * FROM MyTable WHERE Column1 = @Param1

    -- An example of using the OUTPUT parameter
    -- SET @Param2 = 'SomeValue'

    -- Your SQL statements go here
END
GO
