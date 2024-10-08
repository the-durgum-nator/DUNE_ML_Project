import numpy as np
import pandas as pd
import os 
import h5py

chip = "Board_DUAL_DUT_FEChip_P5B_003-07281_RT"

mainpath = os.getcwd()+ f"/LocalDataCopy/{chip}"
folders = os.listdir(mainpath)
mainpath += "/"


#getting a list of folders for later use 
folders= [f.path for f in os.scandir(mainpath) if f.is_dir()]
folders = [x for x in folders if ".csv" not in x]
folders = [x for x in folders if ".pdf" not in x]
folders = [x.replace(mainpath, "") for x in folders]


#custom file searcher associating all files and files in subfolders as one.
def list_print(a :list):
    for x in a:
        print(x)
        print()

# our data-structure linking folders and files within folders.     
linked = dict.fromkeys(folders, [])
print(linked.keys())

# main parsing through all "necessary" data
for curpath, dirs, files in os.walk(mainpath):
    if curpath == mainpath: continue
    curfolder = curpath.replace(mainpath,"").split("/")[0] 
    files = [x for x in files if '.png' not in x]
    files = [x for x in files if ".pdf" not in x]
    
    if linked[curfolder] == []:
        linked[curfolder] = files
    else:
        linked[curfolder].extend(files)     

# implementation of finding a file given a filepath
def findFile(filepath : str):
    for curpath, dirs, files in os.walk(mainpath):
        for path in os.scandir(curpath):
            if path.name == filepath:
                return os.path.abspath(path)
    


with h5py.File("test.hdf5", 'a') as file:
    for k, v in linked.items():
        label = file.create_group(name=f"{k}")
        for value in v:
            flag = True if ".bin" in value else False
            try:
                if ".cmos" in value: pass
                if flag:
                    data = label.create_dataset(value, data = np.fromfile(findFile(value)))
                else: 
                    #print("debugging!")
                    data = label.create_dataset(value, data= pd.read_csv(findFile(value)))
            except:
                print("Error for: " + findFile(value))