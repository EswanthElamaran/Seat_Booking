# ============================================
# audienceinfo.py
# Online Movie Booking System
# ============================================

import csv
import os


class audienceRegistration:

    def __init__(self):

        self.bookingId = 0
        self.movieName = ""
        self.noOfTickets = 0
        self.showTime = ""
        self.bookingDate = ""
        self.bookingList = []
        self.ticketType = ""
        self.ticketFare = 0

    # ----------------------------
    # Get Booking Details
    # ----------------------------
    def getaudienceInfo(self):

        print("\n" + "=" * 50)
        print("MOVIE LIST")
        print("=" * 50)

        movies = {
            1: "KANGUVA",
            2: "AMARAN",
            3: "PUSHPA 2 : THE RULE",
            4: "DEADPOOL & WOLVERINE"
        }

        for key, value in movies.items():
            print(f"{key}. {value}")

        while True:
            choice = int(input("\nSelect Movie : "))
            if choice in movies:
                self.movieName = movies[choice]
                break
            print("Invalid Choice!")

        # ----------------------------
        # Number of Tickets
        # ----------------------------

        while True:
            self.noOfTickets = int(input("Enter Number of Tickets (1-5): "))
            if 1 <= self.noOfTickets <= 5:
                break
            print("Maximum 5 tickets allowed.")

        # ----------------------------
        # Show Time
        # ----------------------------

        timings = {
            1: "08:00 AM",
            2: "11:30 AM",
            3: "02:15 PM",
            4: "06:45 PM",
            5: "09:45 PM"
        }

        print("\nShow Timings")

        for key, value in timings.items():
            print(f"{key}. {value}")

        while True:
            choice = int(input("Select Show Time : "))
            if choice in timings:
                self.showTime = timings[choice]
                break
            print("Invalid Choice!")

        self.bookingDate = input("Enter Booking Date (DD-MM-YYYY): ")

        # ----------------------------
        # Seat Booking
        # ----------------------------

        print("\nAvailable Seats\n")

        for i in range(1, 41):
            print(f"{i:2}", end=" ")
            if i % 10 == 0:
                print()

        self.bookingList = []

        while len(self.bookingList) < self.noOfTickets:

            seat = int(input(f"\nChoose Seat {len(self.bookingList)+1}: "))

            if seat < 1 or seat > 40:
                print("Seat does not exist.")
                continue

            if seat in self.bookingList:
                print("Seat already selected.")
                continue

            self.bookingList.append(seat)

        # ----------------------------
        # Ticket Type
        # ----------------------------

        print("\nTicket Type")
        print("1. 2D - ₹150")
        print("2. 3D - ₹200")

        while True:

            choice = int(input("Choose Ticket Type : "))

            if choice == 1:
                self.ticketType = "2D"
                self.ticketFare = self.noOfTickets * 150
                break

            elif choice == 2:
                self.ticketType = "3D"
                self.ticketFare = self.noOfTickets * 200
                break

            else:
                print("Invalid Choice!")



# ============================================
# CSV Class
# ============================================

class audienceDataCsv(audienceRegistration):

    filename = "audienceData.csv"

    def saveInfo(self):

        # Generate Booking ID

        if os.path.exists(self.filename):

            with open(self.filename, "r", newline="") as file:
                data = list(csv.reader(file))
                bookingId = len(data) + 1

        else:
            bookingId = 1

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                bookingId,
                self.movieName,
                self.noOfTickets,
                self.showTime,
                self.bookingDate,
                ",".join(map(str, self.bookingList)),
                self.ticketType,
                self.ticketFare
            ])

        print("\n" + "=" * 50)
        print("BOOKING SUCCESSFUL")
        print("=" * 50)

        print(f"Booking ID   : {bookingId}")
        print(f"Movie        : {self.movieName}")
        print(f"Tickets      : {self.noOfTickets}")
        print(f"Show Time    : {self.showTime}")
        print(f"Date         : {self.bookingDate}")
        print(f"Seats        : {self.bookingList}")
        print(f"Ticket Type  : {self.ticketType}")
        print(f"Total Amount : ₹{self.ticketFare}")

        print("\nEnjoy Your Movie!")