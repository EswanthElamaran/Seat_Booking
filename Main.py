# ===============================
# Online Movie Booking System
# Main.py
# ===============================

from admin import Admin
from audienceinfo import audienceDataCsv
from TicketShow import TicketShow


def main():

    print("=" * 60)
    print("         ONLINE MOVIE BOOKING SYSTEM")
    print("=" * 60)

    admin = Admin()

    while True:

        print("\nMAIN MENU")
        print("1. Admin Registration")
        print("2. Admin Login")
        print("3. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # -------------------------------
        # Admin Registration
        # -------------------------------
        if choice == 1:
            admin.adminRegistration()

        # -------------------------------
        # Admin Login
        # -------------------------------
        elif choice == 2:

            if admin.adminLogin():

                while True:

                    print("\n" + "-" * 50)
                    print("ADMIN MENU")
                    print("-" * 50)
                    print("1. Book Movie Ticket")
                    print("2. Show Booked Ticket")
                    print("3. Logout")

                    try:
                        option = int(input("\nEnter your choice: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    if option == 1:
                        booking = audienceDataCsv()
                        booking.getaudienceInfo()
                        booking.saveInfo()

                    elif option == 2:
                        ticket = TicketShow()
                        ticket.ticketShow()

                    elif option == 3:
                        print("\nLogged out successfully.")
                        break

                    else:
                        print("Invalid Choice.")

        # -------------------------------
        # Exit
        # -------------------------------
        elif choice == 3:
            print("\nThank you for using Online Movie Booking System.")
            print("Visit Again!")
            break

        else:
            print("Invalid Choice.")


# ===============================
# Program Starts Here
# ===============================
if __name__ == "__main__":
    main()