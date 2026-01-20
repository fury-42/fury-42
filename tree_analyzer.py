import os 
from collections import defaultdict
from tkinter.font import names
folder = input("folder to scan: ")
files=folders=0
ext_cnt=defaultdict(int)    
big_size=0
big_path=""
for root,dirs,filenames in os.walk(folder):
    folders+=len(dirs)
    for name in names:
        files+=1
        ext =name.split('.')[-1] if '.' in name else 'no-ext'
        ext_cnt[ext]+=1
        full=os.path.join(root,name)
        try:
            size=os.path.getsize(full)
            if size>big_size:
                big_size=size
                big_path=full
        except OSError:
            pass
        def rain(n):
            return f"{n/1024/1024:.1f} MB" if n>1024*1024 else f"{n/1024:.1f} KB" if n>1024 else f"{n} B"   
print("\nfiles:",files )
print("folders:",folders)  
print("biggest file:",big_path,rain(big_size)) 

