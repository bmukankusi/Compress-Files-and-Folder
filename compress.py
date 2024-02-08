import os
import shutil
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_filename = f"{folder_name}_{current_date}.{compress_type}"
        
        if compress_type == "tgz":
            compressed_filename = f"{folder_name}_{current_date}.tar.gz"
            with tarfile.open(compressed_filename, "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, "w") as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), 
                                   arcname=os.path.relpath(os.path.join(root, file), 
                                                           os.path.join(folder_path, '..')))
        else:
            print("Invalid compression type.")
            return False
        
        print(f"Compression successful. Compressed file saved as: {compressed_filename}")
        return True
    except Exception as e:
        print(f"Compression failed: {e}")
        return False

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    compress_types = ["zip", "tar", "tgz", "rar", "gz"]
    print("Available compressed file types:")
    for i, c_type in enumerate(compress_types, 1):
        print(f"{i}. {c_type}")
    
    choice = input("Enter the number corresponding to the desired compression type: ")
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(compress_types):
            print("Invalid choice.")
            return
        
        compress_type = compress_types[choice_index]
        
        if compress_folder(folder_path, compress_type):
            print("Compression process completed successfully.")
        else:
            print("Compression process failed.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()