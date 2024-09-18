import requests
import zipfile
import os

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

# def download_file(url, file_name):
#     """
#     Download a file from the specified URL and save it to the current directory.

#     Args:
#         url (str): The base URL to download the file from.
#         file_name (str): The name of the file to save.
#     """
    
#     with open(file_name, 'wb') as file:
#         file.write(requests.get(url + file_name).content)
#     print(f"Downloaded {file_name} successfully.")

# TODO: Create a function to call kaggle and download the dataset
# by passing the dataset name.

def unzip_file(file_name, extract_to='data'):
    """
    Unzips the specified zip file into a folder inside the given directory.

    Args:
        file_name (str): The name of the zip file to unzip.
        extract_to (str): The directory where the zip file should be extracted. 
                          Defaults to 'data'.
    """

    # Create 'data' folder if it doesn't exist
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    
    # Create a folder inside 'data' with the same name as the zip file (without .zip extension)
    folder_name = os.path.join(extract_to, os.path.splitext(file_name)[0])
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Unzip the file into the newly created folder
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(folder_name)
    print(f"Unzipped {file_name} into {folder_name}.")

def main():
    """Driven Function"""

    data01 = 'E:\WSU Classes\CS 4580 Fall 2024\my-notes-lukshsahitia\data\hotel-booking-demand.zip'
    #download_file(SERVER_URL, data01)
    unzip_file(data01)

if __name__ == '__main__':
    main()
