# Initialize variables
truck_count = 0
bus_count = 0
car_count = 0
bike_count = 0
cycle_count = 0
total_vehicles = 0
total_gain = 0

# Functions for operations
def add_vehicle(vehicle_type, price):
    global total_vehicles, total_gain
    if vehicle_type == "truck":
        global truck_count
        truck_count += 1
    elif vehicle_type == "bus":
        global bus_count
        bus_count += 1
    elif vehicle_type == "car":
        global car_count
        car_count += 1
    elif vehicle_type == "bike":
        global bike_count
        bike_count += 1
    elif vehicle_type == "cycle":
        global cycle_count
        cycle_count += 1

    total_vehicles += 1
    total_gain += price
    print("Vehicle added successfully!")

def show_status():
    print("\n--- Current Status ---")
    print("Trucks:", truck_count)
    print("Buses:", bus_count)
    print("Cars:", car_count)
    print("Bikes:", bike_count)
    print("Cycles:", cycle_count)
    print("Total Vehicles:", total_vehicles)
    print("Total Gain:", total_gain)
    print("----------------------")

def delete_data():
    global truck_count, bus_count, car_count, bike_count, cycle_count, total_vehicles, total_gain
    truck_count = 0
    bus_count = 0
    car_count = 0
    bike_count = 0
    cycle_count = 0
    total_vehicles = 0
    total_gain = 0
    print("All data reset to zero!")

# Main program
while True:
    print("\n--- Vehicle Management System ---")
    print("1. Add Vehicle")
    print("2. Show Status")
    print("3. Delete Data")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        vehicle_type = input("Enter vehicle type: ").lower()
        price = float(input("Enter price: "))
        add_vehicle(vehicle_type, price)
    elif choice == "2":
        show_status()
    elif choice == "3":
        delete_data()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
            
