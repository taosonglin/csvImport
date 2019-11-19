"""
#           corax_field_dic
# key:      field name
# value:    field type (and length)
# author:   create on 2019/11/14 by taosonglin
# notes:    update this dic when get new field and \
#           flush NON_CHAR_TYPES & INT_TYPES
"""
corax_field_dic = {}
corax_field_dic['RIC'] = 'CHAR(30)'
corax_field_dic['Ticker'] = 'CHAR(50)'
corax_field_dic['Security Description'] = 'CHAR(200)'
corax_field_dic['Delete Marker'] = 'TINYINT(1)'
corax_field_dic['Dividend Announcement Date'] = 'DATE'
corax_field_dic['Dividend Record Date'] = 'DATE'
corax_field_dic['Dividend Ex Date'] = 'DATE'
corax_field_dic['Dividend Pay Date'] = 'DATE'
corax_field_dic['Period End Date'] = 'DATE'
corax_field_dic['Dividend Payment Type'] = 'CHAR(3)'
corax_field_dic['Dividend Frequency'] = 'BIGINT(15)'
corax_field_dic['Dividend Frequency Description'] = 'CHAR(70)'
corax_field_dic['Period Length'] = 'BIGINT(15)'
corax_field_dic['Period Units'] = 'BIGINT(15)'
corax_field_dic['Period Units Description'] = 'CHAR(70)'
corax_field_dic['Dividend Type Marker'] = 'BIGINT(15)'
corax_field_dic['Dividend Type Marker Description'] = 'CHAR(70)'
corax_field_dic['Dividend Rate'] = 'DECIMAL(18,14)'
corax_field_dic['Dividend Currency'] = 'CHAR(3)'
corax_field_dic['Dividend Currency Description'] = 'CHAR(40)'
corax_field_dic['Dividend Source of Funds'] = 'TINYINT(1)'
corax_field_dic['Dividend Source of Funds Description'] = 'CHAR(16)'
corax_field_dic['Dividend Tax Rate'] = 'DECIMAL(18,14)'
corax_field_dic['Dividend Tax Marker'] = 'BIGINT(15)'
corax_field_dic['Dividend Tax Marker Description'] = 'CHAR(70)'
corax_field_dic['Dividend Market Event ID'] = 'BIGINT(15)'
corax_field_dic['Corporate Action Notes'] = 'VARCHAR(4096)'
corax_field_dic['Last Update Timestamp'] = 'CHAR(24)'
corax_field_dic['Exchange Code'] = 'CHAR(3)'
corax_field_dic['ISIN'] = 'CHAR(12)'
corax_field_dic['Shares Amount'] = 'BIGINT(24)'
corax_field_dic['Shares Amount Date'] = 'DATE'
corax_field_dic['Shares Amount Type'] = 'CHAR(10)'
corax_field_dic['Shares Amount Type Description'] = 'CHAR(40)'
corax_field_dic['Shares Amount Type Default Flag'] = 'CHAR(1)'
corax_field_dic['TRBC Business Sector Code'] = 'CHAR(4)'
corax_field_dic['TRBC Business Sector Code Description'] = 'CHAR(50)'
corax_field_dic['TRBC Industry Code'] = 'CHAR(8)'
corax_field_dic['TRBC Industry Code Description'] = 'CHAR(50)'
corax_field_dic['GICS Industry Code'] = 'CHAR(8)'
corax_field_dic['GICS Industry Code Description'] = 'CHAR(50)'
corax_field_dic['Market MIC'] = 'CHAR(4)'
corax_field_dic['Quote PermID'] = 'CHAR(18)'
corax_field_dic['Issue PermID'] = 'CHAR(18)'
corax_field_dic['Issuer Name'] = 'VARCHAR(110)'
corax_field_dic['Issuer PermID'] = 'CHAR(18)'
corax_field_dic['Issuer OrgID'] = 'CHAR(10)'
corax_field_dic['Trading Status'] = 'TINYINT(1)'
corax_field_dic['Asset Status'] = 'CHAR(3)'
corax_field_dic['Asset Status Description'] = 'CHAR(30)'
corax_field_dic['Asset Type'] = 'CHAR(4)'
corax_field_dic['Asset Type Description'] = 'CHAR(30)'
corax_field_dic['Asset SubType'] = 'CHAR(20)'
corax_field_dic['Asset SubType Description'] = 'CHAR(20)'
corax_field_dic['Currency Code'] = 'CHAR(3)'
corax_field_dic['Currency Code Description'] = 'CHAR(40)'
corax_field_dic['Exchange Description'] = 'CHAR(70)'
corax_field_dic['File Code'] = 'CHAR(15)'
corax_field_dic['Open'] = 'DECIMAL(18,9)'
corax_field_dic['High'] = 'DECIMAL(18,9)'
corax_field_dic['Low'] = 'DECIMAL(18,9)'
corax_field_dic['Last'] = 'DECIMAL(18,9)'
corax_field_dic['Universal Close Price'] = 'DECIMAL(39,14)'
corax_field_dic['Volume'] = 'BIGINT(15)'
corax_field_dic['Turnover'] = 'DECIMAL(39,14)'
corax_field_dic['Trade Date'] = 'DATE'
corax_field_dic['Actual Adjustment Factor'] = 'DECIMAL(39,14)'
corax_field_dic['Actual Adjustment Type'] = 'CHAR(3)'
corax_field_dic['Actual Adjustment Type Description'] = 'CHAR(100)'
corax_field_dic['Adjustment Factor'] = 'DECIMAL(39,14)'
corax_field_dic['Capital Change Ex Date'] = 'DATE'
corax_field_dic['GICS Industry Code'] = 'CHAR(8)'
corax_field_dic['GICS Industry Code Description'] = 'CHAR(50)'
corax_field_dic['EPS Amount'] = 'DECIMAL(39,14)'
corax_field_dic['EPS Basis Number of Shares'] = 'DECIMAL(39,14)'
corax_field_dic['EPS Calculation Basis'] = 'CHAR(3)'
corax_field_dic['EPS Currency'] = 'CHAR(3)'
corax_field_dic['EPS General Marker'] = 'BIGINT(15)'
corax_field_dic['EPS General Marker Description'] = 'CHAR(70)'
corax_field_dic['EPS Net/Gross Marker'] = 'BIGINT(15)'
corax_field_dic['EPS Net/Gross Marker Description'] = 'CHAR(70)'
corax_field_dic['Earnings Announcement Date'] = 'DATE'

corax_fields = corax_field_dic.keys()

"""
define non_char types list for field filter and transform data
"""
INT_TYPES = ['SMALLINT(3)', 'TINYINT(1)', 'BIGINT(15)', 'BIGINT(24)']
DECIMAL_TYPES = ['DECIMAL(18,9)', 'DECIMAL(12,6)', 'DECIMAL(39,14)']



corax_map={}
corax_map['']
