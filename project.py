# Name : Agniva Roy
# Class : XI
# Section : J
# Roll No: 7

from math import ceil
print("Welcome to Brihadeeswarar Temple, Thanjavur, Tamil Nadu")
agniva = {}
COST_TABLE = {
    "TW": {
        "1-2 hrs": 10,
        "3-5 hrs": 12,
        "6-10 hrs": 15,
        "Above 10 hrs": 20
    },
    "FW": {
        "1-2 hrs": 20,
        "3-5 hrs": 25,
        "6-10 hrs": 30,
        "Above 10 hrs": 40
    }
}
collection = 0
while True:
    cost = 0
    operation = input('''Please enter the operation you want to proceed with
Enter (For Vehicles entering the Temple),
Exit (For Vehicles exiting the temple),
End (To End the program and display total collection of the days)
> ''')
    if len(agniva) == 0 and operation.lower() != "enter":
        if operation.lower() == "end":
            print("Terminating application")
            print("The total collection of the day is", collection, "rupees")
            break
        if operation.lower() == "exit":
            print("No Cars present in parking lot")
            print("Invalid operation choosen")
    elif operation.lower() == "enter":
        print("Welcome to the temple")
        while True:
            T = input("Enter the type of the vehicle (TW/tw - For Two Wheeler or FW/fw - For Four Wheeler) : ")
            if T not in ["tw", "fw", "TW", "FW"]:
                print("Please enter the proper vehicle type again")
            else:
                break
        L = input("Enter the license plate number : ")
        H1 = int(input("Enter the current time (in 24hr format) : "))
        M1 = int(input("Enter the current min (from 0 to 59) : "))
        if L not in agniva.keys():
            while True:
                if H1 in range(0, 25) and M1 in range(0, 60):
                    agniva[L] = [T.upper(), H1, M1]
                    break
                else:
                    print("Please enter the time correctly")
                    H1 = int(input("Enter the current time (in 24hr format) : "))
                    M1 = int(input("Enter the current min (from 0 to 59) : "))
            print("Enjoy your time at the temple")
        else:
            print("Vehicle with the license plate number", L, "is already present in the parking lot")
    elif operation.lower() == "exit":
        print("Thank you for visting the temple")
        while True:
            L = input("Enter the license plate number : ")
            H2 = int(input("Enter the current hour (in 24hr format) : "))
            M2 = int(input("Enter the current min (from 0 to 59) : "))
            if H2 < agniva[L][1] or H2 not in range(0, 25) or M2 not in range(0, 60) or L not in agniva.keys():
                print("Please enter the info correctly")
            else:
                if L in agniva.keys():
                    agniva[L].append(H2)
                    agniva[L].append(M2)
                    break
        for k, v in agniva.items():
            if L == k:
                Tdiff = ceil((v[len(v) - 2] - v[1]) + (abs(v[len(v) - 1] - v[2])/100))
                if v[0].lower() == "tw":
                    if Tdiff in range(1, 3):
                        cost += Tdiff * COST_TABLE["TW"]["1-2 hrs"]
                    elif Tdiff in range(3, 6):
                        cost += Tdiff * COST_TABLE["TW"]["3-5 hrs"]
                    elif Tdiff in range(6, 11):
                        cost += Tdiff * COST_TABLE["TW"]["6-10 hrs"]
                    else:
                        cost += Tdiff * COST_TABLE["TW"]["Above 10 hrs"]
                elif v[0].lower() == "fw":
                    if Tdiff in range(1, 3):
                        cost += Tdiff * COST_TABLE["FW"]["1-2 hrs"]
                    elif Tdiff in range(3, 6):
                        cost += Tdiff * COST_TABLE["FW"]["3-5 hrs"]
                    elif Tdiff in range(6, 11):
                        cost += Tdiff * COST_TABLE["FW"]["6-10 hrs"]
                    else:
                        cost += Tdiff * COST_TABLE["FW"]["Above 10 hrs"]
                v.append(cost)
        print("Time elapased in parking lot", Tdiff, "hrs")
        print("Total parking fee for", L, "is", cost, "rupees")
        print("Thank you, May you have a nice day")
        collection += cost
        del agniva[L] 
    elif operation.lower() == "end":
        if len(agniva) != 0:
            print("There is/are", len(agniva), "car(s) in the parking lot")
            choice = input("Do you want to calculate their parking fee based on current time? (Y/N) : ")
            if choice.lower() == "n":
                print("Terminating application")
                print("The total collection of the day is", collection, "rupees")
                break
            else:
                cHour = int(input("Enter the current hour (in 24hr format) : "))
                cMin = int(input("Enter the current min (from 0 to 59) : "))
                for k, v in agniva.items():
                    if cHour < v[1] or cHour not in range(0, 25) or cMin not in range(0, 60):
                        print("Please the time correctly")
                        cHour = int(input("Enter the current hour (in 24hr format) : "))
                        cMin = int(input("Enter the current min (from 0 to 59) : "))
                    else:
                        v.append(cHour)
                        v.append(cMin)
                for k, v in agniva.items():
                    Tdiff = ceil((v[len(v) - 2] - v[1]) + (abs(v[len(v) - 1] - v[2])/100))
                    cCost = 0
                    if v[0].lower() == "tw":
                        if Tdiff in range(1, 3):
                            cCost += Tdiff * COST_TABLE["TW"]["1-2 hrs"]
                        elif Tdiff in range(3, 6):
                            cCost += Tdiff * COST_TABLE["TW"]["3-5 hrs"]
                        elif Tdiff in range(6, 11):
                            cCost += Tdiff * COST_TABLE["TW"]["6-10 hrs"]
                        else:
                            cCost += Tdiff * COST_TABLE["TW"]["Above 10 hrs"]
                    elif v[0].lower() == "fw":
                        if Tdiff in range(1, 3):
                            cCost += Tdiff * COST_TABLE["FW"]["1-2 hrs"]
                        elif Tdiff in range(3, 6):
                            cCost += Tdiff * COST_TABLE["FW"]["3-5 hrs"]
                        elif Tdiff in range(6, 11):
                            cCost += Tdiff * COST_TABLE["FW"]["6-10 hrs"]
                        else:
                            cCost += Tdiff * COST_TABLE["FW"]["Above 10 hrs"]
                    cost += cCost
                    print("Vehicle", k, "elapsed", Tdiff, "hrs in the parking lot and its parking fee as of now stands to be", cCost)
                print("As of now, the total parking fee of every vehicle stands to be", cost, "rupees")
                print("Esteemated collection", cost + collection)
                break
        else:
            print("The total collection of the day is", collection, "rupees")
            break
    else:
        print("Invalid Operation choosen")
