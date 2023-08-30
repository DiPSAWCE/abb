"""
Name: Banele
Surname: Mjayezi
Task: Subtask 4 Isat
Subject: BPCP
"""

import array as arr

# Declare and initialise variables
Price_list = arr.array('f', [9.50, 18.75, 37])
Car_Count = 0
Bike_Count = 0
Truck_Count = 0
Total_Money_Made = 0
file = open("Totals.txt", 'w')
# Prompt user for input
print('MAIN MENU')
print('1.Register vehicle ')
print('2.Show totals ')
print('3.End day')
print('4.Write report ')
print('5.Exit Program')

# Modularisation
while True:
    charOption = input("Enter option  ;> ")

    if charOption == '1':
        print(Price_list)
        v_count = input("Please enter vehicle type (b, c, or t): ")

        if v_count.lower() == 'c':
            Car_Count += 1
            Total_Money_Made += Price_list[1]
        elif v_count.lower() == 'b':
            Bike_Count += 1
            Total_Money_Made += Price_list[0]
        elif v_count.lower() == 't':
            Truck_Count += 1
            Total_Money_Made += Price_list[2]
        else:
            print("Invalid vehicle type. Please enter b, c, or t.")

    elif charOption == '2':
        print("Totals:")
        print("Cars:", Car_Count)
        print("Bikes:", Bike_Count)
        print("Trucks:", Truck_Count)
        print("Money : R", Total_Money_Made)

    elif charOption == '3':
        print("The total number of cars is", Car_Count)
        print("The total number of Bikes is", Bike_Count)
        print("The total number of trucks is", Truck_Count)
        print("The total income is R ", Total_Money_Made)

    elif charOption == '4':
        print("Writing report.")
        file.write("Total number of bikes is: " + str(Bike_Count) + "\n")
        file.write("Total number of cars is: " + str(Car_Count) + "\n")
        file.write("Total number of trucks is: " + str(Truck_Count) + "\n")
        file.write("Total number of vehicles is: " + str(Bike_Count + Car_Count + Truck_Count) + "\n")
        file.write("Total income is R " + str(Total_Money_Made))

    elif charOption == '5':
        print("Exiting the program.")
        file.close()
        break

    else:
        print("Invalid option. Please choose a valid option.")

print("Program has ended.")
