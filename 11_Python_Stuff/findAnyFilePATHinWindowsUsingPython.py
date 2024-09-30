import os

confirm_home_drive="c:\\"
myfile = "blah_blah_blah.txt"

breaknum=0
for dirpath, dirfolders, dirfilenames in os.walk(confirm_home_drive):
    f_len=len(dirfilenames)
    counter=0
    for filenames in dirfilenames:
        x=dirfilenames[counter]
        if  x == myfile:
            p=os.path.join(dirpath, x)
            breaknum=1
        counter+=1
        if breaknum == 1:
            break
    if breaknum ==1:
        break
print(p)
                
             