select * from  indexSandbox..calendars where CalendarID=1
select * from  indexSandbox..calendars_log where CalendarID=1

select top 1 date from indexSandbox..calendars where calendarid=1 
select * from indexsandbox..portfoliodates_log
select * from indexsandbox..portfoliodates




select * from indexSandbox..calendars where calendarID = 1 AND MONTH(DATe)=1 AND DAY(DATE)=1

select * from indexSandbox..calendars_log where calendarID = 1 AND MONTH(DATe)=1 AND DAY(DATE)=1
UPDATE indexSandbox..calendars 
SET Holiday='New Year''s Day',DayType=2
where calendarID = 1 AND MONTH(DATe)=1 AND DAY(DATE)=1



SELECT * from indexsandbox..bondsinstruments 
SELECT distinct issuer  from indexsandbox..bondsinstruments order by issuedate desc

	'Bond Name':'BondName',
	'ISIN':'ISIN',
	'Issuer':'Issuer',
	'Issue Date':'IssueDate',
	'Maturity Date':'MaturityDate',
	'Coupon Rate':'CouponRate',
	'Face Value':'FaceValue',
	'Market Value':'MarketValue',
	'Currency':'Currency',
	'Moody''s Rating':'MoodysRating',
	'S&P Rating':'SPRating',
	'Fitch Rating':'FitchRating',
	'Sector':'Sector',
	'Reference Rate':'ReferenceRate',
	'Seniority':'Seniority',
	'Type of Bond':'TypeOfBond',
	
	select *from indexSandbox..lkup_portfolio_details