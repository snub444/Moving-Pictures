import shutil
import os
year=input('which year? ')
month=input('Which month, in MM format please? ')

source = 'C:\\Users\\caboo\\Desktop\\TEST'  #gotta double backslash to escape \; this is where the files come from
dest1 = os.path.join('C:\\Users\\caboo\\Desktop\\TEST\\',month)  #this is where the files a moving to


yearAndmonth= (year+month)  #this sets up the search below for YYYYMM format
files = os.listdir(source)  #this gets the files from the source folder to search
#TODO: learn about os.listdir()

os.chdir(source) #this changes the current working directory to the source from above,you have to do this for it to work

for f in files:
    if (f.startswith(yearAndmonth)):
        shutil.move(f, dest1)
print ('All ',month,'files have been moved to the',year,month,'folder.')
