import os, shutil

# Define the directory containing the files
documents_path = r"/Users/oscarcaddeo/Documents/"
image_path = r"/Users/oscarcaddeo/Pictures/"
downloads_path = r"/Users/oscarcaddeo/Downloads/"


file_name_documents = os.listdir(documents_path)
file_name_images = os.listdir(image_path)
file_name_downloads = os.listdir(downloads_path)

# Define folder names based on file types
folder_names = ['pdf files', 'text files', 'csv files']

# Create folders if they don't exist
for loop in range(0,3):
    if not os.path.exists(documents_path + folder_names[loop]):
        os.makedirs((documents_path + folder_names[loop]))

# Move files into their respective folders
for file in file_name_documents:
    if ".pdf" in file and not os.path.exists(documents_path + "pdf files/" + file):
        shutil.move(documents_path + file, documents_path + "pdf files/" + file)
    elif ".png" in file or ".jpeg" in file or ".jpg" in file:
        shutil.move(documents_path + file, image_path + file)
    elif ".txt" in file and not os.path.exists(documents_path + "text files/" + file):
        shutil.move(documents_path + file, documents_path + "text files/" + file)
    elif ".csv" in file and not os.path.exists(documents_path + "csv files/" + file):
        shutil.move(documents_path + file, documents_path + "csv files/" + file)

#TODO Move files from Pictures folder to documents and from both to code
for file in file_name_images:
    if ".pdf" in file or ".txt" in file or ".csv" in file:
        shutil.move(image_path + file, documents_path + file)

#TODO Organize files from downloads folder & desktop

for file in file_name_downloads:
    if ".pdf" in file or ".txt" in file or ".csv" in file:
        shutil.move(downloads_path + file, documents_path + file)
    elif ".png" in file or ".jpg" in file or ".jpeg" in file or ".PNG" in file or ".JPG" in file or ".JPEG" in file:
        shutil.move(downloads_path + file, image_path + file)