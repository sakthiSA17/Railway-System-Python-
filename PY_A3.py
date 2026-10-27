# Task 1
#Create variables to store passenger details
passenger_name = "Rahul Sharma"
passenger_age = 28
gender = "Male"
mobile_number = 9876543210

#Create variables to store passenger details
print("Passenger Name :", passenger_name)
print("Passenger Age :", passenger_age)
print("Gender :", gender)
print("Mobile Number :", mobile_number)

#Task 2
#Create variables for ticket information
train_name ="Rajdhani Express"
seat_number = "B2-45"
ticket_price = 2450
journey_date = "25-May-2026"

#Display ticket information using print() function
print("Train Name :", train_name)
print("Seat Number :", seat_number)
print("Ticket Price :", ticket_price)
print("Journey Date :", journey_date)

#Task 3
#Create variables for passenger count and fare calculation
number_of_passengers = 3
ticket_price = 2450

#Calculate total ticket amount
total_fare = number_of_passengers * ticket_price
print("Total Fare :", total_fare)

#Task 4
#Create a GST percentage variable
gst_percentage = 5

#Calculate GST amount
gst_amount = (total_fare * gst_percentage)/100
print("GST Amount :",gst_amount)

#Calculate final payable amount
final_amount = total_fare + gst_amount
print("Final Payable Amount :", final_amount)


#Task 5
#Display all passenger and ticket details in formatted structure
print("----------- Indian Railways Ticket -----------")
print("Passenger Name :", passenger_name)
print("Train Name 	:", train_name)
print("Seat Number	:", seat_number)
print("Journey Date   :", journey_date)
print("Passengers 	:", number_of_passengers)
print("Ticket Fare	:", total_fare)
print("GST Amount 	:", gst_amount)
print("Final Amount   :", final_amount)
print("----------------------------------------------")
