list =["DealId", "DealVersionId", "Advertiser", "Brand", "Campaign", "Channel", "Programme", "Start_Day", "End_Day", "Start_Time", "End_Time", "MBA Channel Name", "MBA Producer Name", "MBA Programme Name", "MBA Episode Name", "MBA Start Time (HH:MM)", "MBA End Time (HH:MM)", "Remarks", "PT/NPT", "Impact", "Gross_Rate", "FCT", "FCT_Dispersion", "Cost", "TVR_Based_On", "TVRs1", "AFTVRs1", 
"NGRPs1", "Program_CPRP1", "TVRs2", "AFTVRs2", "NGRPs2", "Program_CPRP2", "GenreName", "GenreSequence", "channelsequence", "ExpiryDate"]

# Reading an excel file using Python
import xlrd
import pandas
import pandas as pd
 
# Give the location of the file
loc = ("C:\\Users\\Soujanya\\Downloads\\Buying Basket_Backup_vijji.xls")
#loc=('C:\\Users\\ADMIN\\Desktop\\python\\Buying Basket_Backup_vijji.xlsx')
book=xlrd.open_workbook(loc)
sheet1 = pd.read_excel(r'Book1.xlsx')
 
# To open Workbook
#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0
#print(sheet.cell_value(0, 0))