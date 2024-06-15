# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 00:10:14 2024

File Schema
Key = checksum value of file
Name = Expected file name
Path = Expected file path
Date = Date file added
Package = Associated project
Prev = Previous file key
Next = Next file key
Desc = Description of use of file
Change = Changes from previous version

Tags Schema
Name = Tag name
Parents = List of parent tags
Child = list of child tags

Package Schema
Package = Name of package
Path = File path for file
Name = Name of file
Latest = Checksum value of latest version

@author: derew
"""


file_columns = ["Key", "Name", "Path", "Date", "Package", "Next", "Prev", 'Desc', 'Change']

tag_columns = ["Name", "Parent", "Child", "List of Files"]

package_columns = ['Package', 'Path', 'Name', 'Latest']

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import pandas as pd



fileName = ""    

#Load file from existing file
def loadData():
    #TODO Verify with test data
    print("Load data")
    path = askopenfilename()
    fileName = path.split("/")[-1]
    file_df = pd.read_hdf(path, key="files", append = True)
    tag_df = pd.read_hdf(path, key="tags", append = True)
    package_df = pd.read_hdf(path, key='packages', append = True)
    
    return file_df, tag_df, package_df, fileName
    

#Save data to file
def saveData(file_df, tag_df, package_df):
    print("Save data")
    path = askdirectory()
    path = path + "/" + fileName
    file_df.to_hdf(path, key = 'files', mode='a', complib='zlib', complevel=5)
    tag_df.to_hdf(path, key = 'tags', mode='a', complib='zlib', complevel=5)
    package_df.to_hdf(path, key = 'packages', mode='a', complib='zlib', complevel=5)