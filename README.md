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
```

👨‍💻 Author

Amanuel Alemu Zewdu 

Dev Tech Internship – Python Automation Task

📧 [zeamanuel09@gmail.com]

🌐 [github.com/sight09]

📜 License

Licensed under the MIT License.

Free to use, modify, and distribute for learning or development purposes.
