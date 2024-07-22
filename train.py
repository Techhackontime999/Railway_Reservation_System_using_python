# Created a Railway Reservation System.
# import random
# l=0
# # seats in train
# # 1,2,3,4,5,6,7,8,9....................200
# class Train:
#def __init__(self,name,fare,seats,seatno):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#         self.seatno=seatno
#         self.l=random.randint(1000000000000001,9999999999999999)
#         self.x=0
#         self.index=7777777777777
#     def getstatus(self):
#         print(f"Name of the train is : {self.name} ")
#         print(f"Total no of seats available in the train are : {self.seats}")    
#     def fareinfo(self):
#         print(f"The Price of a ticket in {self.name} is : Rs.{self.fare}")
                
           
#     def bookticket(self):
#         if self.seats > 0:
#             if self.x != 0:
#                 print(f"Your ticket has been booked! Your seat number is: {self.x}")
#                 print("Your Ticket No : ",self.l)     s=[]
#     
#                 Train.s.append(self.x)
#                 Train.s.sort()
#                 self.seats=self.seats-1
#                 self.x=0
                
#             else:
#                 print(f"Your ticket has been booked! Your seat number is: {self.seatno}")
#                 print("Your 16-digit Ticket No : ",self.l)
#                 Train.s.append(self.seatno)
#                 self.seats -= 1
#                 self.seatno +=1
#         else:
#             print("Sorry, this train is full. Kindly try in Tatkal!")
              
#     def seat(self):
#          print("Seat is booked earlier which seatno : ",Train.s)
                  
#     def cancelticket(self,seatno):
#             print(f"your Ticket is successfully cancelled seatno: [{seatno}] ! Money is refund within 24 hours. ")
#             self.index=Train.s.index(seatno)
#             self.x=Train.s.pop(self.index)
#             self.seats=self.seats+1
# print("**************************************************************************************************************")            
# print('''Enter [info or 1] to get seat information ,Enter ["Ticket or 3"] to Book a ticket,Enter ["cancel or 4"] to cancel ticket\nEnter ["fare or 5"] to get fareinfo of the train,Enter [stop] to stop Query...........''')
# print('''Welcome to Indian Railway Service Plateform. \nBe Happy and suspicius Journey !''') 

# # work directly all methods
# b=50
# c=200
# d=1
# # intercity=Train("intercity",b,c,d)
# # intercity.bookticket()
# # intercity.bookticket()
# # intercity.fareinfo()
# # intercity.getstatus()
# # print(Train.s)
# # intercity.cancelticket(1)
# # intercity.getstatus()
# # intercity.bookticket()
# # intercity.bookticket()
# # intercity.fareinfo()
# # intercity.getstatus()
# # print(Train.s)


# # work directly all method.




     
# # # loop is not work continuesly because methods is called only one time in a loop
# n=100
# def ask():
#     r=int(input("enter no of Tickets : "))
#     return r
# for i in range(n):
#      b=50
#      c=20
#      d=1
#      intercity=Train("intercity",b,c,d)
     
#      print("...........................................................................\n")
#      a=input("Enter your Query : ")

#      # below four line is used only for service provider .
#      if a=="stop" or a==6:
#          break
#      elif a=="Ticket" or a=="3" :
#              for k in range(i,ask()):
#                    intercity.getstatus()
#                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#                    print(intercity.bookticket())
                   
#                    print("______ ______ ______ _______ ________ _________ _______ ______")              

#      elif a=="cancel" or a=="4":
#          j=int(input("enter number of Tickets : "))
#          for i in range(j):
#               z=int(input("Enter your seat no : "))
#               print(intercity.cancelticket(z))
                     
#      elif a=="fare" or a=="5":
#          print(intercity.fareinfo())
#      elif a=="info" or a=="1":
#          print(intercity.seat())
#      else:
#          print("invalid input Query .Kindly Please Try again !")


        








