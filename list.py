import os
files = os.listdir(".")
 
lists= []
for filed in files:
    if filed.endswith(".flf"):
        lists.append(filed)
flag=0
looop=len(lists)
while flag<looop:
    os.system('figlet "Our Code World Rocks!" -f'+lists[int(flag)]+'-d ./figlet-fonts/ > output/' +str(flag)+'.md')
    flag=flag+1

