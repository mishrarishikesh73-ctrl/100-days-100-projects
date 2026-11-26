
import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"]
}

def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"

def get_unique_path(folder, filename):
    name, extension = os.path.splitext(filename)
    destination = os.path.join(folder, filename)

    counter = 1

    while os.path.exists(destination):
        new_name = f"{name}_{counter}{extension}"
        destination = os.path.join(folder, new_name)
        counter += 1

    return destination

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        return

    summary = {}

    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)

        # Skip directories
        if not os.path.isfile(source):
            continue

        category = get_category(filename)

        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = get_unique_path(destination_folder, filename)

        try:
            shutil.move(source, destination)
            summary[category] = summary.get(category, 0) + 1
            print(f"Moved: {filename} -> {category}")

        except OSError as error:
            print(f"Could not move {filename}: {error}")

    print("\n====== ORGANIZATION SUMMARY ======")

    if not summary:
        print("No files to organize.")
    else:
        for category, count in summary.items():
            print(f"{category}: {count} files")

    print("\nFile organization completed!")

print("====== FILE ORGANIZER ======")

folder = input("Enter folder path to organize: ").strip().strip('"')

organize_files(folder)