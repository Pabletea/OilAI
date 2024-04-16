import pandas as pd




def csvManager(csv_list):
    print("Datasets found")
    print(len(csv_list))

def xlsManager(xls_list):
    print("XLS files found: ")
    print(len(xls_list)) 
    while(xls_list):
        for file in xls_list:
            xls_file = file
            df = pd.read_excel(xls_file)
            static_columns = ['columna1','columna2','columna3']
            df_filtered=df[static_columns]
            new_xls_file='new_xls_file.xls'
            df_filtered.to_excel(new_xls_file,index=False)
            print("Se ha creado el nuevo archivo filtrado")


       