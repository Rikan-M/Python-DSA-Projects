
class Node:
    def __init__(self,price=0,Name=None,flavour=None,ingridients=[],left=None,right=None):
        self.left=left
        self.right=right
        self.name=Name
        self.flavour=flavour
        self.price=price
        self.ingridients=ingridients
class BST:
    def __init__(self,group_price=500,root=None):
        self.root=root
        self.group_price=group_price
    @classmethod
    def create(cls, data):
        return cls(group_price=data['group_price'], root=data['root'])
    def rec_insert(self,root,n):
        if root.name<n.name:
            if root.right is None:
                root.right=n
            else:
                self.rec_insert(root.right,n)
        elif root.name>n.name:
            if root.left is None:
                root.left=n
            else:
                self.rec_insert(root.left,n)
    def insert(self,name=None,price=0,flavour=None,ingridients=[]):
        n=Node(price,name.lower(),flavour,ingridients)
        if self.root==None:
            self.root=n
        else:
            self.rec_insert(self.root,n)
        self.group_price=(self.group_price+price)//2
    def search(self,name):
        return self.rec_search(name.lower(),self.root)
    def rec_search(self,name,root):
        if root is not None:
            if name>root.name:
                return self.rec_search(name,root.right)
            elif name<root.name:
                return self.rec_search(name,root.left)
            return root
    def show_preorder(self):
        self.rec_preorder(self.root)
    def rec_preorder(self,root):
        if root is not None:
            print("_"*100)
            print("Name : ",root.name)
            print("Price : ",root.price)
            print("Flavour : ",root.flavour)
            print("Ingridients : ", " ".join(x for x in root.ingridients))
            self.rec_preorder(root.left)
            self.rec_preorder(root.right)
    def show_inorder(self):
        self.recur_inorder(self.root)
    def recur_inorder(self,root):
        if root is not None:
            self.recur_show(root.left)
            print(root.price,root.name,root.flavour)
            self.recur_show(root.right)
    def update_cake(self,name,new_price):
        n=self.rec_search(name.lower(),self.root)
        if n:
            n.price=new_price
            self.group_price=(self.group_price+n.price)//2
    def delete(self,name):
        self.root=self.rec_delete(name,self.root)
    def rec_delete(self,name,root):
        if root is not None:
            if name>root.name:
                root.right=self.rec_delete(name,root.right)
            elif name<root.name:
                root.left=self.rec_delete(name,root.left)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = root.left
                while temp.right:
                    temp = temp.right
                root.name, root.flavour, root.price , root.ingridients = temp.name, temp.flavour, temp.price , temp.ingridients
                root.left = self.rec_delete( temp.name,root.left)
            return root
    def get_datas(self):
        return self.root
    def get_group_price(self):
        return self.group_price






