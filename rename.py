import os

def rename_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    files = os.listdir(folder_path)
    # Loop through the files and rename them
    for ix, filename in enumerate(files):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_name = f"image{ix+1}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(os.path.join(folder_path, filename), new_path)

if __name__ == "__main__":
    folder_path = "images"
    rename_files(folder_path)
    print("Files renamed successfully.")
