# create the class ticket which will be the abstract class inside that create a function book ticket which will be the abstract  method and has nothing in it.
# create a class make my trip which will use the book ticket fun()from ticket class to take the details such as name ,phoneno.,emailid,journey date and displays 
# msg saying thank u for bookin from makemytrip.create a class irctc which uses the book ticket of ticket class and take the same details as makemytrip but in
# the end  it will give an option to user to select whether it is one way or round trip.if the user option is round trip it again ask the user to enter the 
# return date as well and then prints the msg thank u for choosing irctcc else print the msg thank u for choosing irctcc.create a class indigo which takes 
# the details as irctc and just asks which mode of transport u want to go  in train ,flight,bus and displays thank u for choosing indigo.
from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def Book_Ticket(self):
        pass
class Make_My_Trip(Ticket):
    def Book_Ticket(self):
        name=input("Enter Your Name: ")
        email_id=input("Enter Your Email ID:")
        phone_no=input("Enter Your Phone Number: ")
        journey_date=input("Enter your Journey Date")
        print("Thank You For Booking From Make My Trip,{name}")
class IRCTC(Ticket):
    def Book_Ticket(self):
        name=input("Enter Your Name: ")
        email_id=input("Enter Your Email ID:")
        phone_no=input("Enter Your Phone Number: ")
        journey_date=input("Enter your Journey Date")
        Trip_Type=input("select the trip type you want choose:\none way trip\nround trip")
        if Trip_Type == "round trip":
            return_date=input("Enter Return Date:")
            print("Your Round Trip From {journey_date} to {return_date} ")
            print("Thank You For Booking From IRCTC,{name}")
class Indigo(Ticket):
    def Book_Ticket(self):
        name=input("Enter The Name:")
        email_id=input("Enter The EMAIL ID:")
        phone_no=input("Enter The Phone Number:")
        journey_date=input("Enter The Journey Date")
        Trip_Mode=input("Select Mode Of Transport:\nbus\ntrain\nflight")
        print("Thank You For Booking From Indigo")
obj=Indigo()

    


            