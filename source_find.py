import os
import glob
import source_manager

def findFiles(path, extension):
    pattern = os.path.join(path, f"*.{extension}")
    #print(pattern)
    
    found_files = glob.glob(pattern)

    return found_files



# Especifica la ruta del directorio donde deseas buscar archivos
actual_path=os.path.dirname(os.path.abspath(__file__))
datasetDir="\data\source"
PATH=actual_path+datasetDir

# Especifica la extensión de archivo que deseas buscar
EXTENSION = "xlsx"

# Llama a la función find_files() proporcionando la ruta del directorio y la extensión
files_list = findFiles(PATH, EXTENSION)

if  (files_list):
    source_manager.xlsManager(files_list)
else:
    print("No dataset found")



def fileCheck(fileList):
    if not fileList:
        return False
    else:
        return True
