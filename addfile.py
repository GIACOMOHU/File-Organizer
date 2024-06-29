import os
import shutil
import csv
import argparse

def move_file(file_name):
    # Define the input folder and output folders
    INPUT_FOLDER = "files"
    OUTPUT_FOLDERS = {"audio": [".mp3", ".wav"],
                      "docs": [".odt", ".txt", ".docx", ".pdf"],
                      "images": [".jpg", ".jpeg", ".png", ".gif"]}
    RECAP_FILE = "recap.csv"

    # Check if the file exists in the input folder
    file_path = os.path.join(INPUT_FOLDER, file_name)
    if not os.path.exists(file_path):
        print("The specified file does not exist in the folder.")
        return

    # Get the file name and extension
    file_name, file_extension = os.path.splitext(file_name)

    # Find the file type based on the extension
    file_type = None
    for folder, extensions in OUTPUT_FOLDERS.items():
        if file_extension.lower() in extensions:
            file_type = folder
            break

    # If the file type is not recognized, ignore it
    if file_type is None:
        print("The file type is not supported.")
        return

    # Move the file to the appropriate folder if it doesn't already exist
    destination_folder = os.path.join(INPUT_FOLDER, file_type)
    destination_path = os.path.join(destination_folder, file_name + file_extension)
    if not os.path.exists(destination_path):
        shutil.move(file_path, destination_path)
    else:
        print("The file already exists in the destination folder.")

    # Update the recap file
    with open(os.path.join(INPUT_FOLDER, RECAP_FILE), 'a', newline='') as recap_file:
        writer = csv.writer(recap_file)
        writer.writerow([file_name, file_type, os.path.getsize(destination_path)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    move_file(args.file_name)

if __name__ == "__main__":
    main()


# da terminale scrivere [python addfile.py "nomedelfile.formato"]