# ============================================
# TicketShow.py
# Online Movie Booking System
# ============================================

import csv
import os


class TicketShow:

    filename = "audienceData.csv"

    def ticketShow(self):

        # Check if booking file exists
        if not os.path.exists(self.filename):
            print("\nNo bookings found.")
            return

        try:
            bookingId = int(input("\nEnter Booking ID : "))
        except ValueError:
            print("Invalid Booking ID.")
            return

        found = False

        with open(self.filename, "r", newline="") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) == 8 and int(row[0]) == bookingId:

                    found = True

                    print("\n")
                    print("=" * 65)
                    print("               ONLINE MOVIE BOOKING E-TICKET")
                    print("=" * 65)
                    print()

                    print(f"Theatre        : LA Cinemas")
                    print(f"Location       : Theppakulam, Trichy")
                    print(f"Phone          : 8000800088")
                    print("-" * 65)

                    print(f"Booking ID     : {row[0]}")
                    print(f"Movie          : {row[1]}")
                    print(f"No. of Tickets : {row[2]}")
                    print(f"Show Time      : {row[3]}")
                    print(f"Booking Date   : {row[4]}")
                    print(f"Seat Numbers   : {row[5]}")
                    print(f"Ticket Type    : {row[6]}")
                    print(f"Total Amount   : ₹{row[7]}")

                    print("-" * 65)
                    print("        Thank You For Booking With LA Cinemas")
                    print("              Enjoy Your Movie!")
                    print("=" * 65)

                    break

        if not found:
            print("\nBooking ID not found.")