import pandas as pd
import openpyxl





def csvManager(csv_list):
    print("Datasets found")
    print(len(csv_list))

def xlsManager(xls_list):
    print("XLS files found: ")
    print(len(xls_list)) 
    
    file=xls_list[0]
    og_name=keepOriginalName(file)

    colums_to_delete= [8,6,4]
 
    colums_to_delete.sort(reverse=True)
  

    xls_file = openpyxl.load_workbook(file)
    xls_sheet = xls_file['Hoja1']

    
    


    for indx in colums_to_delete:
        xls_sheet.delete_cols(idx=indx)


    save_path=pathSorter(file)+og_name

    xls_file.save(save_path)

    sourceConverter(save_path)

    




def pathSorter(path):
    print(path)
    last_backslash_index= path.rfind("\\")
    if last_backslash_index != 1:
        new_path=path[:last_backslash_index+1]
        new_path=new_path.replace("\\source","\\datasets")
        #print("New path"+new_path)
        return new_path
    else:
        print("Backslash not found")    

def keepOriginalName(path):
    print(path)
    last_backslash_index= path.rfind("\\")
    if last_backslash_index != 1:
        og_name=path.split("\\")[-1]
        #print("New path"+new_path)
        return og_name
    else:
        print("Backslash not found")    


def sourceConverter(file):
    df = pd.read_excel(file,sheet_name='Hoja1',header=0)
    dataset_path=pathSorter(file)+"newCSV.csv"
    df.to_csv(dataset_path,index=False)

    return dataset_path
       