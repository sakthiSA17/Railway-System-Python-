#TASK 1
passanger_name = "Raghul Sharma"
ticket_status = "Confirmed"

if ticket_status == "Confirmed":
    print("Ticket Is Confirmed")


#TASK 2
waiting_list = 3

if waiting_list == 0:
    print("Ticket Confirmed")
else:
    print("Ticket is in waiting List")


#TASK 3

ticket_status = "RAC"

if ticket_status == "Confirmed":
    print("Seat Allocated Successfully")
elif ticket_status == "RAC":
    print("Partial Reservation Available")
else:
    print("Ticket is in Waiting List")


#TASK 4

age = 65
if age >= 65:
    print("Passenger Eligible for Senior Citizen Discount")

#TASK 5

is_ticket_confirmed = True

if age >= 60 and is_ticket_confirmed == True:
 	print("Passenger eligible for Senior Citizen Benefits")

# TASK 6

ticket_status = "Confirmed"
payment_status = "Paid"

if ticket_status == "Confirmed" and payment_status == "Paid":
 	print("Ticket Successfully Booked")
elif ticket_status == "RAC":
 	print("Partial Seat Reservation Available")
else:
 	print("Booking Pending")
