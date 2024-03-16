import csv
class details:
    def register(Self,name,email_id,phone_number,address,pincode):
        Self.nm=name
        Self.ed=email_id
        Self.pn=phone_number
        Self.ad=address
        Self.pd=pincode
        with open('details.csv','a',newline="") as credentials:
            store=csv.writer(credentials)
            store=store.writerow([Self.nm,Self.ed,Self.pn,Self.ad,Self.pd])
    def login(Self,username,password):
        Self.un=username
        Self.ps=password
        username=input("Enter your User name:")
        password=input(f"Enter Password for Your {username}:")
        if (username==Self.un and password==Self.ps):
            print("login Successful")
        else:
            print("Invaild Password")
obj=details()
obj.login("","")
obj.register("","","","","")