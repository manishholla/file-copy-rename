import os
import shutil
import tkinter.filedialog
import tkinter.messagebox

# define parent and target folder. Opens file-dialog
parent_folder = tkinter.filedialog.askdirectory(title="Choose Parent folder")
output_folder = tkinter.filedialog.askdirectory(title="Choose Output folder")

# Copy files from Parent folder to output folder
i = 1
for root, dirs, files in os.walk(parent_folder, topdown=True):
    for name in files:
        # To copy all file types
        sourceFolder = os.path.join(root, name)
        shutil.copy(sourceFolder, output_folder)

# Rename files in output folder
        filename = os.path.join(output_folder, name)
        file_ext = os.path.splitext(filename)
        new_name = os.path.join(output_folder, f'{(file_ext [0])}_{i}{(file_ext[1])}')
        os.rename(filename, new_name)
        i += 1
        print(new_name)

print("\n")
print(f"{i-1} files have been copied and renamed to the output folder")

# Opens message-dialog with result
tkinter.messagebox.showinfo(title="Output Info", message=f"{i-1} files have been copied and renamed to the output folder")

# Py-program ends here
