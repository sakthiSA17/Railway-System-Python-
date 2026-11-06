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

# Actvivity 5

#Task 1
passenger_age = 25
ticket_confirmed = True

if passenger_age >= 18 and ticket_confirmed:
   print("Passenger Eligible for Travel")

# Task 2
confirmed_seat = False
rac_seat = True

if confirmed_seat or rac_seat:
   print("Reservation Available")

# Task 3
ticket_cancelled = False

if not ticket_cancelled:
   print("Ticket is Active")

# Task 4
passenger_age = 65
payment_completed = True

if passenger_age >= 60 and payment_completed:
   print("Senior Citizen Reservation Approved")

#Task 5
available_seats = 5
payment_status = True

if available_seats > 0 and payment_status:
   print("Ticket Confirmed Successfully")
else:
   print("Reservation Failed")

#Task 6

valid_id_proof = True
booking_time_valid = True

if valid_id_proof and booking_time_valid:
   print("Tatkal Booking Allowed")
else:
   print("Tatkal Booking Denied")

#Task 7

passenger_name = "Rahul Sharma"
passenger_age = 30
available_seats = 2
payment_completed = True
ticket_cancelled = False

if (
   passenger_age >= 18 and
   available_seats > 0 and
   payment_completed and
   not ticket_cancelled
):
   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Reservation Status : Confirmed")
else:
   print("Reservation Failed")

