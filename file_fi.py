import os
import glob
import file_man

def findFiles(path, extension):
    pattern = os.path.join(path, f"*.{extension}")
    #print(pattern)
    
    found_files = glob.glob(pattern)

    return found_files



# Especifica la ruta del directorio donde deseas buscar archivos
actual_path=os.path.dirname(os.path.abspath(__file__))
datasetDir="\datasets"
PATH=actual_path+datasetDir

# Especifica la extensión de archivo que deseas buscar
EXTENSION = "csv"

# Llama a la función find_files() proporcionando la ruta del directorio y la extensión
files_list = findFiles(PATH, EXTENSION)

if  (files_list):
    file_man.dataManager(files_list)
else:
    print("No dataset found")



def fileCheck(fileList):
    if not fileList:
        return False
    else:
        return True


