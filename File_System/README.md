# File Management System in Python

## Project Description
This project is a command-line-based File Management System built in Python. It allows users to perform various file and directory operations such as creating, renaming, deleting, moving, and displaying file structures. The project implements advanced data structures and concepts to mimic a file system environment.

## Features
- **Create Directories and Files:** Add new folders and files with content.
- **Navigate Directories:** Move forward and backward between directories.
- **Delete Files or Directories:** Remove files or directories from the system.
- **Copy, Cut, and Paste:** Perform copy and move operations within the file system.
- **Rename Files or Directories:** Change the names of files and directories.
- **Rewrite Files:** Replace the contents of an existing file.
- **Display File Structure:** Show the current directory's entire structure.
- **Metadata Information:** View file or directory details such as name, type, creation date, and content.
- **Clipboard Operations:** Support for cut and copy actions with paste functionality.
- **Persistent Storage:** Save and load the file system structure using the `pickle` library.

## Project Structure
```
File_System/
├── Datas/
|      └── Root_Binary.pkl  # Stores the serialized file system data
├── FileSys.py              # Core classes and logic for the file management system
├── Main.py                 # Entry point for the file management system
└──README.md                # README.md file
```

## How to Run the Project
1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/Rikan-M/Python-DSA-Projects.git>
   cd <File_System>
   ```

2. **Install Dependencies:**
   The project does not require external dependencies but ensures you have Python 3.6 or higher installed.

3. **Run the File Management System:**
   ```bash
   python main.py
   ```

## Available Commands
| Command                             | Description                                      |
|-------------------------------------|--------------------------------------------------|
| `makedir [directory name]`          | Create a new directory                           |
| `makefil [file name] [content]`     | Create a file with specified content             |
| `cd [directory name]`               | Enter a specified directory                      |
| `cd..`                              | Move to the parent directory                     |
| `delf [file/directory name]`        | Delete a file or directory                       |
| `copy [file/directory name]`        | Copy a file or directory                         |
| `cut [file/directory name]`         | Cut a file or directory                          |
| `paste`                             | Paste the copied or cut file/directory           |
| `open`                              | Show the content of the current file             |
| `disstruct`                         | Display the current directory structure          |
| `child`                             | Show child files and directories                 |
| `metadata`                          | Display metadata of the current directory/file   |
| `rename [old name] [new name]`      | Rename a file or directory                       |
| `rewrite [file name] [new content]` | Rewrite a file with new content                  |
| `renroot [new name]`                | Rename the root directory                        |
| `/help`                             | View all available commands                      |
| `/quit`                             | Exit the file management system                  |
| `/cls`                              | Clear the console screen                         |

## Example Usage
```
Root_Folder/> makedir Projects
Root_Folder/> cd Projects
Root_Folder/Projects/> makefil Project1.txt This is the project description.
Root_Folder/Projects/> cd Project1.txt
Root_Folder/Projects/Project1/> open
This is the project description.
Root_Folder/Projects/Project1/> cd..
Root_Folder/Projects/> disstruct
Root_Folder > Projects  :/> Project1.txt :Fil ;

Root_Folder/Projects/> cd..
Root_Folder/> disstruct
Root_Folder  :/> Projects :Dir ;
Root_Folder > Projects  :/> Project1.txt :Fil ;

```

## Key Concepts and Libraries
- **Object-Oriented Programming (OOP)**: Implemented using `Folder` and `File` classes.
- **Data Structures:** Tree-based structure for efficient file and directory management.
- **Pickle Library:** Used for saving and loading the file system state.
- **Datetime Module:** Tracks the creation date of files and directories.

## Contributing
Feel free to fork this repository and create pull requests for improvements or feature additions.

## License
This project is open-source and available under the MIT License.

