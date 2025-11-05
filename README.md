# 🗂️ File Organizer — Dev Tech Internship Task

## 📌 Task Description

**Task 2: File Organizer**

Write a Python script that automatically organizes files in a folder based on their file types.

**Example:**
- Move `.jpg` and `.png` files into an **Images** folder  
- Move `.pdf` files into a **Documents** folder  

This task demonstrates your ability to work with:
- File and folder management using **os** and **shutil**
- **Loops**, **conditions**, and **automation logic**
- Writing **clean, reusable, and practical code**

---

## 🎯 Internship Learning Goals

✅ Understand and apply **Python file handling**  
✅ Learn to use **automation scripts** for productivity  
✅ Practice **directory traversal and manipulation**  
✅ Develop clean code structure and console-based applications  

---

## 🚀 Features

- Automatically categorizes files by type:
  - 🖼️ **Images** → `.jpg`, `.jpeg`, `.png`, `.gif`
  - 📄 **Documents** → `.pdf`, `.docx`, `.txt`, `.pptx`
  - 🎬 **Videos** → `.mp4`, `.mov`, `.mkv`
  - 🎵 **Music** → `.mp3`, `.wav`
  - 📦 **Archives** → `.zip`, `.rar`, `.7z`, `.tar`
  - 📁 **Others** → Unrecognized file types

- Creates folders automatically if they don’t exist  
- Works on **Windows, macOS, and Linux**  
- Simple **console interface** for quick use  

---

## 🧩 How It Works

1. The program asks for a folder path from the user.  
2. It scans all files in that folder.  
3. Based on each file’s extension, it moves the file into the appropriate category folder.  
4. If no match is found, the file is moved into the **Others** folder.  
5. Displays a message for every file that’s moved.  

---

## 💻 Code File

**`file_organizer.py`**

```python
import os
import shutil

def organize_files(folder_path):
    """
    Organize files in the given folder based on file extensions.
    """

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

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder_name, filename))
                print(f"Moved: {filename} → {folder_name}/")
                moved = True
                break

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

⚙️ How to Run

    Clone this repository or download the script:

git clone https://github.com/sight09/File_Organizer.git
cd File_Organizer

Run the program:

    python File_Organizer.py

    Enter the path of the folder you want to organize.

🧠 Example Output

=== 🗂️ File Organizer ===
Enter the path of the folder to organize: C:\Users\Amanuel\Downloads
Moved: photo1.jpg → Images/
Moved: project.pdf → Documents/
Moved: song.mp3 → Music/
✅ File organization complete!

🧰 Requirements

    Python 3.7 or above

    No external dependencies (uses built-in modules os and shutil)

🧾 Folder Structure

devtech-file-organizer/
│
├── file_organizer.py
├── README.md
└── (organized folders created at runtime)

👨‍💻 Author

Amanuel Alemu Zewdu
Dev Tech Internship – Python Automation Task
📧 [zeamanuel09@gmail.com]
🌐 [github.com/sight09]
📜 License

Licensed under the MIT License.
Free to use, modify, and distribute for learning or development purposes.
