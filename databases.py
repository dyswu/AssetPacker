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
import hashlib


   
fileName = ""
file_df = pd.DataFrame(index = file_columns)
tag_df = pd.DataFrame(index = tag_columns)
package_df = pd.DataFrame(index = package_columns)

#Get hash value of file
def md5(file_name):
    m = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            m.update(chunk)
        return m.hexdigest()
    
print("hello")

#Add file to database
def inputFile(path):
    #TODO
    print("Adding file to DB")
    
#Check to see if file already exists in database or not    
def checkFile(file):
    #TODO
    print("check file") 

#Create folders

#Add file to DB
def addFile():
    print("select file to add")
    path = askopenfilename()
    file_name = path.split("/")[-1]
    key = (md5(path))
    #TODO Check existing file
    #If yes -> file preview, ELSE
    #TODO Ask for tags
    #Add to existing project -> File name (new or updated)
    #Get date
    #If update -> get old id, set old next to key
    #Save changes in db
    saveData()

#if load:
#    file_df, tag_df, package_df, fileName = databases.loadData()
    

def resetData():
    file_df = pd.DataFrame(Data = None, index = file_columns)
    tag_df = pd.DataFrame(Data = None, index = tag_columns)
    package_df = pd.DataFrame(Data = None, index = package_columns)
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