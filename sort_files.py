import os, shutil

# Define the directory containing the files
path = r"/Users/oscarcaddeo/Documents/"
image_path = r"/Users/oscarcaddeo/Pictures/"

file_name = os.listdir(path)
file_name_images = os.listdir(image_path)

# Define folder names based on file types
folder_names = ['pdf files', 'text files', 'csv files']

# Create folders if they don't exist
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))

# Move files into their respective folders
for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".png" in file or ".jpeg" in file or ".jpg" in file:
        shutil.move(path + file, image_path + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)

#TODO Move files from Pictures folder to documents and from both to code

#TODO Organize files from downloads folder & desktop