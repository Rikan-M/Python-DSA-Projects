from FileSys import Management
import re
import os
def is_valid_name(name: str) -> bool:
    """
    Validates a file or folder name based on common rules.
    Returns True if the name is valid, otherwise False.
    """
    # Check if the name is empty or only whitespace
    if not name.strip():
        print("Error: Name cannot be empty or only whitespace.")
        return False

    # Define a regular expression for invalid characters
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    
    # Check for invalid characters
    if re.search(invalid_chars, name):
        print("Error: Name contains invalid characters: <>:\"/\\|?*")
        return False

    # Check for name length
    if len(name) > 255:
        print("Error: Name exceeds the maximum length of 255 characters.")
        return False
    return True


folder=Management()
help_doc={"makedir [directory name]": "to create a directory",
    "makefil [file name] [file content]": "to create a content file",
    "cd [directory name]": "to enter a directory",
    "cd..": "to go to the parent directory",
    "delf [file/directory name]": "to delete files/directories",
    "copy [file/directory name]": "to copy files/directories",
    "cut [file/directory name]": "to cut a file/directory",
    "paste": "to paste the copied/cut file or directory",
    "open": "to see the content of the current file or directory",
    "disstruct": "to display the complete structure of the current directory",
    "child": "to display all the child files and directories in the current directory",
    "metadata": "to display metadata information of the current directory or file",
    "rename [old name] [new name]": "to rename a file or directory",
    "rewrite [file name] [new content]": "to rewrite a file with new content",
    "renroot [new name]": "to rename the root directory",
    "/help": "to view all available commands and their descriptions",
    "/quit": "to quit the file management system",
    "/cls": "to clear the console screen"
          }
while True:
    choice=input((str(folder.get_path())+'>'))
    splited=list(map(str,choice.split()))
    try:
        cmd=splited[0].lower()
    except:
        continue
    try:
        name=splited[1]
    except:
        name=None
    try:
        content=''.join((x+' ') for x in splited[2:]).strip()
    except:
        content=None
    if cmd=='makedir':
        if name and is_valid_name(name):
            folder.create_folder(name)
        if not name:
            print("File/Dir has no name")
        continue
    elif cmd=='makefil':
        if name and content and is_valid_name(name):
            folder.create_file(name,content)
        if not name:
            print("File/Dir has no name")
        elif not content:
            print("File has no content file")
    elif cmd=='cd':
        if name and is_valid_name(name):
            folder.move_foraord(name)
    elif cmd=='cd..':
        folder.move_backward()
    elif cmd=='delf':
        if name and is_valid_name(name):
            folder.delete(name)
    elif cmd=='copy':
        if name and is_valid_name(name):
            folder.copy(name)
    elif cmd=='paste':
        folder.paste()
    elif cmd=='cut':
        if name and is_valid_name(name):
            folder.cut(name)
    elif cmd=='open':
        print(folder.show_item())
    elif cmd=='disstruct':
        folder.display_structure()
    elif cmd=='child':
        folder.show_child()
    elif cmd=='metadata':
        folder.metadata()
    elif cmd=='rename':
        if name and content and is_valid_name(name) and is_valid_name(content):
            folder.rename(name,content)
    elif cmd=='rewrite':
        if name:
            folder.rewrite(name+' '+content)
        else:
            folder.rewrite('')
    elif cmd=='renroot':
        if name and is_valid_name(name):
            folder.renroot(name)
    elif cmd=='/help':
        for commands in help_doc:
            print(commands," : ",help_doc[commands])
    elif cmd=='/quit':
        break
    elif cmd=='/cls':
        os.system("cls" if os.name=='nt' else "clear")
    else:
        print("No such command exists.enter /help to see all commands.") 
    folder.save()
