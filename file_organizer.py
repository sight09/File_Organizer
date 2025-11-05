import os
import shutil

def organize_files(folder_path):
    """
    Organize files in the given folder based on file extensions.
    Example:
        - Images (.jpg, .png) → 'Images' folder
        - Documents (.pdf, .docx, .txt) → 'Documents' folder
        - Videos (.mp4, .mov) → 'Videos' folder
    """

    # Define file type categories and their extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".7z", ".tar"]
    }

    # Create target folders if they don’t exist
    for folder_name in file_types.keys():
        folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Loop through files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)

        # Move file based on extension
        moved = False
        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder_name, filename))
                print(f"Moved: {filename} → {folder_name}/")
                moved = True
                break

        # If file extension doesn’t match, move it to 'Others'
        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} → Others/")

    print("\n✅ File organization complete!")


if __name__ == "__main__":
    print("=== 🗂️ File Organizer ===")
    folder_path = input("Enter the path of the folder to organize: ").strip()

    if os.path.exists(folder_path):
        organize_files(folder_path)
    else:
        print("❌ Error: The specified folder path does not exist.")
