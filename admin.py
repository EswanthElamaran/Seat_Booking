# ===============================
# admin.py
# ===============================

import csv
import os


class Admin:

    def __init__(self):
        self.filename = "adminCredential.csv"

    # -----------------------------
    # Admin Registration
    # -----------------------------
    def adminRegistration(self):

        print("\n" + "=" * 50)
        print("ADMIN REGISTRATION")
        print("=" * 50)

        username = input("Enter Username : ").strip()
        password = input("Enter Password : ").strip()

        # Check whether username already exists
        if os.path.exists(self.filename):

            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) >= 2 and row[0] == username:
                        print("\nUsername already exists!")
                        return

        # Save new admin
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        print("\nRegistration Successful!")

    # -----------------------------
    # Admin Login
    # -----------------------------
    def adminLogin(self):

        print("\n" + "=" * 50)
        print("ADMIN LOGIN")
        print("=" * 50)

        # Check if admin file exists
        if not os.path.exists(self.filename):
            print("\nNo Admin Registered.")
            print("Please register first.")
            return False

        username = input("Enter Username : ").strip()
        password = input("Enter Password : ").strip()

        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) >= 2:
                    if username == row[0] and password == row[1]:
                        print("\nLogin Successful!")
                        return True

        print("\nInvalid Username or Password.")
        return False