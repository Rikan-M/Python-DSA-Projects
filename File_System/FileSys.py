from datetime import datetime as dt
import os
import pickle

os.makedirs("File_System/Datas",exist_ok=True)

class Folder:
    def __init__(self,name:str="New_Folder",child:dict={},parent=None):
        self.parent=parent
        self.child=child
        self.name=name
        self.is_file=False
        self.date=dt.now()
class File:
    def __init__(self,name="New_File",referance=None,parent=None):
        try:
            splited_name=list(map(str,name.split('.')))
            if len(splited_name)>1:
                self.extension=splited_name[-1]
                self.name=splited_name[0]
            else:
                self.extension="Unknown?"
                self.name=name
        except:
            self.extension="Unknown?"
            self.name=name
        self.ref=referance
        self.parent=parent
        self.is_file=True
        self.date=dt.now()
        

class Management:
    def __init__(self,root=Folder("Root_Folder")):
        self.root=root
        self.load()
        self.pointer=self.root
        self.path=str(self.root.name)+'/'
        self.clipboard=None
        self.clipboard_cut_type=False
        self.cuted_file_path=None
    def create_folder(self,FolderName):
        if self.pointer.is_file:
            print("Can't create directory inside a file")
            return
        folder=Folder(FolderName,{},self.pointer)
        confirm=True
        if self.pointer.child.get(FolderName):
            confirm=self.already_exist(FolderName)
        if confirm:
            self.pointer.child[FolderName]=folder
    def create_file(self,FileName,Filepath):
        if self.pointer.is_file:
            print("Can't create a file inside a file")
            return
        file=File(FileName,Filepath,self.pointer)
        confirm=True
        if self.pointer.child.get(FileName):
            confirm=self.already_exist(FileName)
        if confirm:
            self.pointer.child[FileName]=file
    def renroot(self,name):
        root_len=len(self.root.name)
        self.path=name+self.path[root_len]
        self.root.name=name
    def delete(self,name):
        if not self.pointer.is_file:
            if self.pointer.child.get(name):
                self.pointer.child.pop(name)
            else:
                self.not_found()
    def move_foraord(self,name):
        if self.pointer.is_file:
            print("Can't move forward! It is a file")
            return
        if self.pointer.child.get(name):
            self.pointer = self.pointer.child[name]
            self.path += str(self.pointer.name) + '/'
        else:
            self.not_found()
    def copy(self,name):
        if not self.pointer.is_file:
            if self.pointer.child.get(name):
                self.clipboard=self.create_copy(self.pointer.child.get(name))
                self.clipboard_cut_type=False
            else:
                self.not_found()
    def create_copy(self,root,prnt=None):
        if root:
            if root.is_file:
                f=File(root.name,root.ref,prnt)
            else:
                f=Folder(root.name,{},prnt)
                for child in root.child:
                    f.child[child]=self.create_copy(root.child.get(child),f)
        return f
        
    def cut(self,name):
        if not self.pointer.is_file:
            if self.pointer.child.get(name):
                self.cuted_file_path=self.pointer
                self.clipboard=self.pointer.child[name]
                self.clipboard_cut_type=True

            else:
                self.not_found()
    def paste(self):
        if self.pointer.is_file:
            print("Can't paste anything inside a file!")
            return
        if not self.clipboard:
            print("Nothing to paste!")
            return
        confirm=True
        if self.pointer.child.get(self.clipboard.name):
            confirm=self.already_exist(self.clipboard.name)
        if confirm:
            self.clipboard.parent=self.pointer
            self.pointer.child[self.clipboard.name]=self.clipboard
        if self.clipboard_cut_type:
            self.cuted_file_path.child.pop(self.clipboard.name)
            self.clipboard=None
            self.cuted_file_path=None
            self.clipboard_cut_type=False
    def move_backward(self):
        if self.pointer.parent is not None:
            l=len(self.pointer.name)
            self.pointer=self.pointer.parent
            self.path=self.path[:-l-1]
    def show_item(self):
        if self.pointer.is_file:
            return self.pointer.ref
        else:
            return "Directories does not contains any item!"
    
    def rename(self,oldname,newname):
        confirm=True
        if self.pointer.child.get(oldname):
            if self.pointer.child.get(newname):
                confirm=self.already_exist(newname)
            if confirm:
                node=self.pointer.child.pop(oldname)
                node.name=newname
                self.pointer.child[newname]=node
                node.parent = self.pointer
        else:
            self.not_found()
    def rewrite(self,text):
        if not self.pointer.is_file:
            print("Can't use rewrite in a directory")
            return
        self.pointer.ref=text
    def show_child(self):
        if self.pointer.is_file:
            print(None)
            return
        if len(self.pointer.child)>0:
            for child in self.pointer.child:
                print(child,':Fil' if self.pointer.child[child].is_file else ':Dir',end=" ; ")
            print()
        else:
            print(None)
    def not_found(self):
        print("No such file/dir exist in this directory!")
        print("Files/Dirs :> ",end='')
        self.show_child()
    def already_exist(self,name=""):
        print(f"Already contain a file/dir named {name}!")
        replace=input("Do you want to replace the existing ? (Y/N): ")
        return replace.upper()=='Y'
    def metadata(self):
        if self.pointer.is_file:
            print("Name : ",self.pointer.name)
            print("Type : ","File")
            print("Extension : ",self.pointer.extension)
            print("Parent Folder : ",self.pointer.parent.name)
            print("Created On : ", self.pointer.date)
            print("Content : ",self.pointer.ref)
        else:
            print("Name : ",self.pointer.name)
            print("Type : ","Directory")
            try:
                print("Parent Folder : ",self.pointer.parent.name)
            except:
                pass
            print("Created On : ", self.pointer.date)
            if len(self.pointer.child)>0:
                print("Child : ",end=" ")
                for child in self.pointer.child:
                    print(child ,end=' ; ')
                print()

    def save(self):
        with open("File_System/Datas/Root_Binary.pkl",'wb') as f:
            pickle.dump(self.root,f)
    def load(self):
        try:                                          
            with open("File_System/Datas/Root_Binary.pkl",'rb') as f:
                data=pickle.load(f)
                if data:
                    self.root=data
        except:
            with open("File_System/Datas/Root_Binary.pkl",'wb') as f:
                pickle.dump(self.root,f)
    def display_structure(self):
        self.rec_dis_struc(self.pointer)
    def rec_dis_struc(self,root):
        if root:
            if not root.is_file:
                if not root.parent:
                    print(root.name," :/>",end="")
                else:
                    print(root.parent.name,">",root.name," :/>", end="")
                if len(root.child)>0:
                    for child in root.child:
                        print(child,':Fil' if root.child[child].is_file else ':Dir',end=" ; ")
                    print()
                if len(root.child)>0:
                    for child in root.child:
                        self.rec_dis_struc(root.child[child])
            print()
    def get_path(self):
        return self.path

    


