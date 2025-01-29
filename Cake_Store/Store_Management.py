from Binary_Search_Tree import BST
from Customers import Customers
from datetime import datetime as dt
import pickle

import os

os.makedirs("Cake_Store/Cake_Data" , exist_ok=True)
class Store:
    def __init__(self):
        self.customers=Customers()
        self.cake_groups = {
            "Pastry": BST(50),
            "Normal": BST(500),
            "Expensive": BST(2000),
        }
        self.Load()

    def save(self):
        try:
            with open("Cake_Store/Cake_Data/Customer_Data.pkl","wb") as f:
                cust_data=self.customers.get_datas()
                pickle.dump(cust_data, f)
            cake_data = {key: group.__dict__ for key, group in self.cake_groups.items()}
            with open("Cake_Store/Cake_Data/Cake_Data.pkl","wb") as f:
                pickle.dump(cake_data, f)
               
        except Exception as e:
            return f"Saving Data Error : {e}"
    def Load(self):
        try:
            with open("Cake_Store/Cake_Data/Customer_Data.pkl", "rb") as f:
                data = pickle.load(f)
                self.customers = Customers.create(data)
                print(data)
            with open("Cake_Store/Cake_Data/Cake_Data.pkl", "rb") as f:
                cake_data = pickle.load(f)
                for key, data in cake_data.items():
                    self.cake_groups[key]=BST.create(data)
        except FileNotFoundError:
            print("Data files not found. Starting fresh.")
        
        except Exception as e:
            print(f"Error loading data: {e}")


    def select_group(self,price):
        diff=float('inf')
        group=None
        for cake in self.cake_groups:
            Gprice=self.cake_groups[cake].get_group_price()
            if abs(Gprice-price)<diff:
                diff=abs(Gprice-price)
                group=cake
        return group
    def add_cake(self,name=None,price=0,flavour=None,ingridients=[]):
        group=self.select_group(price)
        if group:
            self.cake_groups[group].insert(name,price,flavour,ingridients)
    def change_cake_price(self,name,old_price,new_price):
        group=self.select_group(old_price)
        if group:
            self.cake_groups[group].update_cake(name,new_price)
    def show(self,group_name):
        self.cake_groups[group_name].show_preorder()
    def remove_cake(self,name,group):
        for groups in self.cake_groups:
            if groups.lower()==group.lower():
                self.cake_groups[groups].delete(name)
                return True
        return False
    def check_date(self,date):
        time=None
        try:
            time=dt.strptime(date,"%Y-%m-%d %H:%M:%S")
            if time:
                return True
        except:
            return False
    def new_order(self,cust_name,date,order,quantity,phone_no):
        if not self.check_date(date):
            return False
        self.customers.add(cust_name,date,order,quantity,phone_no)
    def remove_order(self,phone_no):
        return self.customers.cancel(phone_no)
    def urgent_order_completed(self):
        return self.customers.done_urgent_order()
    def get_urgent_order(self):
        return self.customers.get_urgent_order()
    def show_all_cakes(self):
        for group_name, group in self.cake_groups.items():
            print(f"--- {group_name} Cakes ---")
            group.show_preorder()
    def show_all_customers(self):
        self.customers.view_pending_data()

