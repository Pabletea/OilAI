import pandas as pd
import openpyxl





def csvManager(csv_list):
    print("Datasets found")
    print(len(csv_list))

def xlsManager(xls_list):
    print("XLS files found: ")
    print(len(xls_list)) 
    while(xls_list):
        for file in xls_list:
            xls_file = openpyxl.load_workbook(file)
            xls_sheet = xls_file['Hoja1']
            xls_sheet.delete_cols(idx=4)
            xls_sheet.delete_cols(idx=6)
            xls_sheet.delete_cols(idx=8)
            xls_file.save("New_file.xlsx")
            break
            


       