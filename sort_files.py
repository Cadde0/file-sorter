import os, shutil

# Define the directory containing the files
path = r"/Users/oscarcaddeo/Documents/py-fileSort/"

file_name = os.listdir(path)

# Define folder names based on file types
folder_names = ['pdf files', 'image files', 'text files', 'csv files']

# Create folders if they don't exist
for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))

# Move files into their respective folders
for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    else:
        print("File where not moved" + file)