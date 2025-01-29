from datetime import datetime as dt
class Customers:
    def __init__(self, customers=None):
        self.customers = customers if customers else []           
    @classmethod
    def create(cls, data):
        return cls(customers=data)
    def convert_date(self,date):
        try:
            time=dt.strptime(date,"%Y-%m-%d %H:%M:%S")
            return time
        except:
            return False
    def add(self,name,date,order,quantity,Phone_number=None):
        formated_date=self.convert_date(date)
        if formated_date:
            self.customers.append({"name":name,"date":formated_date,"order":order,"quantity":quantity,"phone number":Phone_number})
        temp=len(self.customers)-1
        while temp>0 and self.customers[temp]["date"]<self.customers[temp-1]["date"]:
            self.customers[temp],self.customers[temp-1]=self.customers[temp-1],self.customers[temp]
            temp-=1
    def get_urgent_order(self):
        if len(self.customers)==0:
            return
        return self.customers[0]
    def cancel(self, phone_num):
        for i, customer in enumerate(self.customers):
            num=customer.get("phone number")
            if num and int(num)  == int(phone_num):
                return self.customers.pop(i)
        print(f"No customer found with phone number: {phone_num}")
        return False
    def done_urgent_order(self):
        if len(self.customers)>0:
            return self.customers.pop(0)
    def get_datas(self):
        return self.customers
    def get_cust_data(self,phone_num):
        for i, customer in enumerate(self.customers):
            if customer.get("phone number") == phone_num:
                return self.customers[i]
        print(f"No customer found with phone number: {phone_num}")
        return False
    def view_pending_data(self):
        for i in self.customers:
            print("_"*100)
            print("Name : ",i["name"])
            print("Phone Number : ",i["phone number"])
            print("Time : ",i["date"])
            print("Order : ",i["order"])
            print("Quantity : ",i["quantity"])
cust=Customers()
cust.add("rikan","2025-01-12 10:00:00","hello",1,9932611092)           
cust.add("arghya","2025-01-12 10:00:00","hello",1,1234567890) 

cust.view_pending_data()
print("After: ")
cust.cancel("9932611092")
cust.view_pending_data()   

