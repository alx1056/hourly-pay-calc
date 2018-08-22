import xlwt
from xlwt import Workbook
import datetime


times = input("Would you like to calculate pay for weekly (1) bi-weekly (2) or monthly (4)? ")
startdate = input("What is your startdate? (mm/dd/yyyy) ")
enddate = input("What is your enddate? (mm/dd/yyyy) ")

if times == "1":
    #for x in range(1,10):
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Hours worked ')#+ str(x))
     
    hworked = int(input('Please enter the hours worked:'))
    hwage = int(input('Please enter the hourly wage:'))
    if hworked > 40:
      gross = (hworked - 40) * (hwage) * 1.5 + (hwage * (hworked - (hworked - 40)))
      print('The gross pay with overtime is',(hworked - 40) * (hwage) * 1.5 + (hwage * (hworked - (hworked - 40))),'$')
    else:
      print('The gross pay without overtime is', hworked * hwage, '$')
    
    
    sheet1.write(0, 0, 'Pay before tax')
    sheet1.write(0, 1, 'Pay after tax')
    sheet1.write(0, 2, 'total hours worked')
    sheet1.write(0, 3, 'Week')
    
    sheet1.write(1, 0, gross)
    sheet1.write(1, 1, gross * .725)
    sheet1.write(1, 2, hworked)
    sheet1.write(1, 3, startdate + " " + enddate)
    
        
    #wb.save('Hours Worked.xlsx')#excel 2010 and >
    wb.save('Hours worked.xls')#excel 97-2003
    
    
elif times == "2":
        #for x in range(1,10):
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Hours worked ')#+ str(x))
     
    hworked = int(input('Please enter the hours worked:'))
    hwage = int(input('Please enter the hourly wage:'))
    if hworked > 40:
      gross = (hworked - 40) * (hwage) * 1.5 + (hwage * (hworked - (hworked - 40)))
      print('The gross pay with overtime is',(hworked - 40) * (hwage) * 1.5 + (hwage * (hworked - (hworked - 40))),'$')
    else:
      print('The gross pay without overtime is', hworked * hwage * 2, '$')
    

    sheet1.write(0, 0, 'Pay before tax')
    sheet1.write(0, 1, 'Pay after tax')
    sheet1.write(0, 2, 'total hours worked')
    sheet1.write(0, 3, 'Week')
    
    sheet1.write(1, 0, gross)
    sheet1.write(1, 1, gross * .725)
    sheet1.write(1, 2, hworked)
    sheet1.write(1, 3, startdate + " " + enddate)
    
        
    #wb.save('Hours Worked.xlsx')#excel 2010 and >
    wb.save('Hours worked.xls')#excel 97-2003
    
    
else: 
        #for x in range(1,10):
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Hours worked ')#+ str(x))
     
    hworked = int(input('Please enter the hours worked:'))
    hwage = int(input('Please enter the hourly wage:'))
    if hworked > 40:
      gross = (hworked - 40) * (hwage) * 1.5 + (hwage * (hworked - (hworked - 40)))
      print('The gross pay with overtime is',(hworked - 40) * (hwage) * 1.5 + (hwage * (hworked - (hworked - 40))),'$')
    else:
      print('The gross pay without overtime is', hworked * hwage * 4, '$')

    
    sheet1.write(0, 0, 'Pay before tax')
    sheet1.write(0, 1, 'Pay after tax')
    sheet1.write(0, 2, 'total hours worked')
    sheet1.write(0, 3, 'Week')
    
    sheet1.write(1, 0, gross)
    sheet1.write(1, 1, gross * .725)
    sheet1.write(1, 2, hworked)
    sheet1.write(1, 3, startdate + " " + enddate)
    
        
    #wb.save('Hours Worked.xlsx')#excel 2010 and >
    wb.save('Hours worked.xls')#excel 97-2003
    
