import os
import shutil

# Path to the folder you want to organize
folder_path = "D:\Desktop\Python programes\CodeAlpha 2025(1st May - 30th May)-2"  # <-- change this to your folder

# Go through each file in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        name, extension = os.path.splitext(filename)
        extension = extension[1:]  # Remove the dot (.)

        # Create a folder for this extension if it doesn't exist
        if extension:
            new_folder = os.path.join(folder_path, extension)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            # Move the file into the new folder
            shutil.move(os.path.join(folder_path, filename),
                        os.path.join(new_folder, filename))
            print(f"Moved {filename} to {extension} folder.")

print("\nDone organizing files!")
