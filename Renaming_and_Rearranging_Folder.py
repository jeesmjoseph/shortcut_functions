import os

def rearrange(folder,x):
  for count , filename in enumerate(os.listdir(folder)) :
    dat = f"{x}{str(count)}.jpg"
    src = f"{folder}/{filename}"
    dest = f"{folder}/{dat}"
    os.rename(src,dest)

folder = input("Enter folder location : ")
x = input("Enter keyword : ")
rearrange(folder,x)