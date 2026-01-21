import os 
from collections import defaultdict
from tkinter.font import names
folder = input("folder to scan: ")
files=folders=0
ext_cnt=defaultdict(int)    
big_size=0
big_path=""
def human_readable_size(n):
    if n > 1024 * 1024:
        return f"{n / 1024 / 1024:.1f} MB"
    elif n > 1024:
        return f"{n / 1024:.1f} KB"
    else:
        return f"{n} B"
    def analyze_directory(root_dir):
        """Recursively analyze the directory and its contents."""
        total_files = 0
        total_folders = 0
        total_size = 0
        ext_count = defaultdict(int)
        largest_file_size = 0
        largest_file_path = ""
        Permission_Error = []

        print(f"starting analysis of: {root_dir}")
        for root, dirs, files in os.walk(root_dir):
            for dir_name in dirs:
                directory_path = os.path.join(root, dir_name)
                if not os.access(directory_path, os.R_OK):
                    print(f"Permission denied: {directory_path}")
                    continue
                total_folders += len(dirs)
                total_files += len(files)
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if not os.access(file_path, os.R_OK):
                    print(f"Permission denied: {file_path}")
                    continue
                ext = file_name.split('.')[-1] if '.' in file_name else 'no-ext'
                ext_count[ext] += 1
                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    if file_size > largest_file_size:
                        largest_file_size = file_size
                        largest_file_path = file_path
                except OSError:
                    print(f"Could not access file size: {file_path}")
                    continue
    large_file.sort(key=lambda x: x[1], reverse=True)
    
    print("_" *30)
    print("Analysis summary:")
    print('_' *30)
    print(f"Total files: {total_files}")
    print(f"Total folders: {total_folders}")
    print(f"Largest file: {largest_file_path} ({human_readable_size(largest_file_size)})")
    print("File extensions and their counts:")
    for ext, count in ext_count.items():
            print(f".{ext}: {count}")
            print("\nTop 5 largest files(>10Mb):")
            if large_files:
                for file_path, size in large_files[:5]:
                    print(f"{file_path}: {human_readable_size(size)}")
                else:
                    print("No files larger than 10MB found.")
                     
                    if Permission_Errors:
                        print(f"\n{len (Permission_Errors)} permission errors encountered(snippet of first 5):")
                        for error in Permission_Errors[:5]:
                            print(f"- {error}")
                            print('For a full list of errors,please review output log.')

                            if __name__ == "__main__":
                                directory_to_scan = input("Enter the folder to scan: ")
                                analyze_directory(directory_to_scan)    