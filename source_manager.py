import pandas as pd
import openpyxl





def csvManager(csv_list):
    print("Datasets found")
    print(len(csv_list))

def xlsManager(xls_list):
    print("XLS files found: ")
    print(len(xls_list)) 
    
    file=xls_list[0]

    colums_to_delete= [8,6,4]
    colums_to_delete.sort(reverse=True)

    xls_file = openpyxl.load_workbook(file)
    xls_sheet = xls_file['Hoja1']
    
    for indx in colums_to_delete:
        xls_sheet.delete_cols(idx=indx)


    save_path=pathSorter(file)
    xls_file.save(save_path+"New_file.xlsx")



def pathSorter(path):
    print(path)
    last_backslash_index= path.rfind("\\")
    if last_backslash_index != 1:
        new_path=path[:last_backslash_index+1]
        new_path=new_path.replace("\\source","\\datasets")
        print("New path"+new_path)
        return new_path
        
    else:
        print("Backslash not found")    


            


       