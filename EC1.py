#Create a program for people to choose what movie's ticket they want

#Displaying the available movies with each movie and showtime
print("Available movies today:")
print("A) 12 Strong:    1) 2:30 2) 4:40 3) 7:50 4) 10:50")
print("B) Coco:         1) 12:40 2) 3:45")
print("C) The Post:     1) 12:45 2) 3:35 3) 7:05 4) 9:55")

#User enters what movie they want with corresponding letter
choice = input("Movie choice: ")

#Making sure that user chooses one of the letters or it prints invalid
if choice not in ["A" , "B" , "C"]:
    print("Invalid option; please restart app...")
    quit()

#User enters what movie they want with corresponding letter
time = input("Showtime: ")

#Making sure that user chooses one of the numbers or it prints invalid
#This is for the A movie
if choice == "A" and time not in ["1", "2", "3", "4"]:
    print("Invalid option; please restart app...")
    quit()
#For B movie
elif choice == "B" and time not in ["1", "2"]:
    print("Invalid option; please restart app...")
    quit()

#For C movie
elif choice == "C" and time not in ["1", "2", "3", "4"]:
    print("Invalid option; please restart app...")
    quit()


#user now will enter number of either tickets they want
ticketA = input("Adult tickets: ")
ticketB = input("Kid tickets: ")

#turning variables input into integers, and value checking
try:
    ticketA = float(int(ticketA))
    ticketB = float(int(ticketB))
except ValueError:
    print("Invalid option; please restart app...")
    quit()

#if all tickets added up are greater than 30 than it will print invalid
if ticketA < 0 or ticketB < 0 or ticketA + ticketB > 30:
    print("Invalid option; please restart app...")
    quit()

#variables for the cost of Adult and Kid tickets, respectively
costA = float(0)
costB = float(0)

#Now the cost of tickets will be calculated based on what movie and showtime chosen
if choice == "A":
    costA = (ticketA * 12.45)
    costB = (ticketB * 9.68)

elif choice == "B":
    if time == "1":
        costA = (ticketA * 11.17)
        costB = ticketB * 8.00
    elif time == "2":
        costA = costA + (ticketA * 12.45)
        costB = costB + (ticketB * 9.68)

elif choice == "C":
    if time == "1":
        costA = (ticketA * 11.17)
        costB = (ticketB * 8.00)

    else:
       costA = (ticketA * 12.45)
       costB = (ticketB * 9.68)

#cost of all tickets is added and rounded
final = round(costA + costB, 2)

#cost is printed with statement 
print(f"Total cost: ${final}")

