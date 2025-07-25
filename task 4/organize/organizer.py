import os
import shutil

# Define file type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Others': []
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder not found.")
            return

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                category = get_category(ext)

                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                destination = os.path.join(category_folder, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename} -> {category}/")

        print("\nFile organization completed successfully.")

    except Exception as e:
        print("Error organizing files:", e)

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
