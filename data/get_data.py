import requests
import zipfile
import os

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/seaborData.zip'

def download_file(url, file_name):
    """
    Download a file from the specified URL and save it to the current directory.

    Args:
        url (str): The full URL to download the file from.
        file_name (str): The name of the file to save.
    """
    
    response = requests.get(url)
    
    with open(file_name, 'wb') as file:
        file.write(response.content)
    
    print(f"Downloaded {file_name} successfully.")

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
    
    # Unzip the file into the specified folder
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print(f"Unzipped {file_name} into {extract_to}.")

def main():
    """Driven Function"""

    # Define the name of the zip file to download
    zip_file_name = 'ign_scores.zip'

    # Download the zip file
    download_file(SERVER_URL, zip_file_name)

    # Unzip the downloaded file
    unzip_file(zip_file_name)

if __name__ == '__main__':
    main()