
from pathlib import Path

#Absolute path - from root

#Relative path -


from pathlib import Path

##creating an instance
#path = Path("ecommerce")

## see if exists
#print(path.exists())

#path2 = Path("ecommerce1")
#print(path2.exists())

## make dir
#path3 = Path("emails")
#print(path3.mkdir())

##remove dir
#print(path3.rmdir())

##automation tip
##find all files and dir in a given path
## string for search pattern
## '*' - everything
## '*.*' - all files - no folders
## '*.xls' - all files of a given extension

path4 = Path()
#print(path4.glob('*.py'))
for file in path4.glob('*.py'):
    print(file)
