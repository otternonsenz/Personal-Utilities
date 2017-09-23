#Find CSV to Add to database
#Open CSV and check against SQL Database headers/rows
#If CSV Checks out, then load data into staging
#Once data is loaded in staging, clean
#For transaction, apply unit system based on date of transaction old to new
#If credit, color green. If debit, color red.
#For line color = green, add point to credit_green.
#For line color = red, add point to credit_green.
#For Company name, if <Category> is Null, then prompt for <category>
#For Company name, if <Category> is True, then apply to all uses of Company name
#If staging shows clean data, then move to database
#Update dashboard
