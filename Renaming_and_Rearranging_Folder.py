import os

def rearrange(folder,x,ext):
  for count , filename in enumerate(os.listdir(folder)) :
    dat = f"{x}{str(count)}.{ext}"
    src = f"{folder}/{filename}"
    dest = f"{folder}/{dat}"
    os.rename(src,dest)

folder = input("Enter folder location : ")
x = input("Enter keyword : ")
ext = input("Enter extension : ")
rearrange(folder,x,ext)