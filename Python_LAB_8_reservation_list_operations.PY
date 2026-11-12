#TASK 1

passengers = ["Rahul Sharma", "Priya Patel", "Amit Verma"]

print("Passenger Reservation List:")
print(passengers)

print("\nFirst Passenger:", passengers[0])

print("Second Passenger:", passengers[1])

print("Third Passenger:", passengers[2])

#TASK 2

passengers = ["Rahul Sharma", "Priya Patel", "Amit Verma"]

print(passengers)

passengers.append("Sneha Joshi")
print(passengers)

passengers.remove("Amit Verma")
print(passengers)

passengers.insert(1, "Rohan Mehta")
print(passengers)

removed_passenger = passengers.pop(2)
print(passengers)

print("\nUpdated Reservation List:")
print(passengers)

