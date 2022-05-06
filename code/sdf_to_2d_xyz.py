import numpy as np
import os
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
#filepath ="/home/user/Downloads/211116_Yang_source_code/"
filepath ="/home/user/yang/"

os.chdir(filepath+"sorce_code/example_data/sdf_file")
sdf_list = os.listdir(".")
for i in range(len(sdf_list)):
    os.chdir(filepath + "sorce_code/example_data/sdf_file")
    file=sdf_list[i]
    name = file[:-4]
    
    spl=Chem.SDMolSupplier(file,removeHs=True)#remove H atom
    
        
    a=spl[0]
    AllChem.Compute2DCoords(a)#calculate 2d coordinate
        
    with open (filepath + "sorce_code/example_data/xyz_file/2d_xyz/%s.xyz"%(name),"w") as f:
        f.write(Chem.MolToXYZBlock(a))
