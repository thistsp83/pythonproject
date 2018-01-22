from datetime import datetime
 import xlsxwriter

 # Create a workbook and add a worksheet.
 workbook = xlsxwriter.Workbook('user.xlsx')
 worksheet = workbook.add_worksheet()

 # Add a bold format to use to highlight cells.
 bold = workbook.add_format({'bold': 1})

 # Add a number format for cells with money.
 money_format = workbook.add_format({'num_format': '$#,##0'})

 # Add an Excel date format.
 date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

 # Adjust the column width.
 worksheet.set_column(1, 1, 15)

 # Write some data headers.
 worksheet.write('A1', 'Url', bold)
 worksheet.write('B1', 'word', bold)
 worksheet.write('C1', 'count', bold)

 # Some data we want to write to the worksheet.
 expenses = (
     ['www.niit.com', 'welcome', 10],
     ['www.niit.com',  'niit',  8],
     ['www.niit.com', 'world',  3],
  
 )

 # Start from the first cell below the headers.
 row = 1
 col = 0

 for item, date_str, cost in (expenses):
     # Convert the date string into a datetime object.
     date = datetime.strptime(date_str, "%Y-%m-%d")

     worksheet.write_string  (row, col,     item              )
     worksheet.write_datetime(row, col + 1, date, date_format )
     worksheet.write_number  (row, col + 2, cost, money_format)
     row += 1

 # Write a total using a formula.
''' worksheet.write(row, 0, 'Total', bold)
 worksheet.write(row, 2, '=SUM(C2:C5)', money_format)'''

 workbook.close()