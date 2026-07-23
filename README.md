# 🎬 Seat Booking Application (Core Python)

## 📌 Overview

This is a simple **Seat Booking Application** developed using **Core Python**. It allows users to book movie tickets, view their ticket, and save booking details in a CSV file for future use.

This project follows the basic **Software Development Life Cycle (SDLC)**.

---

# 📋 SDLC Steps

Before starting the project:

1. Collect Requirements
2. Plan the Project
3. Analyze Each Module
4. Design the Output
5. Start Coding Module by Module
6. Test the Application

---

# ✨ Features

- View theatre details
- View available shows
- Select show timing
- Book seats
- Choose seat type (2D/3D)
- Calculate ticket fare
- Save booking details in CSV
- View booked ticket
- Admin can view all bookings

---

# 📁 Project Structure

```
Seat Reservation/
│
├── Show_info.py
├── TicketShow.py
├── Admin.py
├── main.py
├── passenger_data.csv
└── README.md
```

---

# 📂 File Description

### Show_info.py
Stores theatre and show details.

### TicketShow.py
Displays the booked ticket.

### Admin.py
Reads and displays booking records from the CSV file.

### main.py
Main program that connects all modules.

### passenger_data.csv
Stores booking details permanently.

---

# 🏛 Theatre Details

- Theatre Name
- Contact Number
- Address

---

# 🎥 Show Details

- Show Name
- Show Timing
- Date
- Day
- Seat Number
- Seat Type (2D/3D)
- Ticket Fare

---

# 👤 PassengerRegistration Class

Stores passenger information.

### Attributes

- passengerName
- noOfPassenger
- Show
- Showtiming
- selectDay
- selectSeatNo
- selectSeatType
- SeatFare
- autoInc
- countCol

---

# 💾 PassengerDataCsv

This class is responsible for:

- Saving booking details to a CSV file
- Reading booking records
- Keeping booking history

---

# 🎟 TicketShow

Displays the ticket after successful booking.

Example:

```
Movie Ticket

Passenger : Rahul
Movie      : Leo
Seat       : A10
Timing     : 6:00 PM
Seat Type  : 3D
Fare        : ₹250

Enjoy your movie!
```

---

# 👨‍💼 Admin

The Admin module can:

- View all bookings
- Read data from the CSV file
- Check booking history

---

# 🔄 Project Flow

```
Start
   ↓
Show Available Movies
   ↓
Enter Passenger Details
   ↓
Select Show & Seat
   ↓
Calculate Fare
   ↓
Save Booking in CSV
   ↓
Display Ticket
   ↓
End
```

---

# 🛠 Technologies Used

- Python 3
- CSV Module
- File Handling
- Object-Oriented Programming (OOP)

---

# ▶️ How to Run

Open the project folder and run:

```bash
python main.py
```

---

# 📚 What You Will Learn

- How to start a Python project
- Basic SDLC process
- Object-Oriented Programming
- Modular programming
- CSV file handling
- File handling
- Ticket generation
- Simple project structure

---

# 🚀 Future Improvements

- Add GUI using Tkinter
- Use MySQL or SQLite
- Online payment
- QR code tickets
- Multiple theatres
- User login system

---

# 👨‍💻 Conclusion

This project is a beginner-friendly Python application that demonstrates how a simple theatre booking system works. It helps in understanding project planning, modular programming, OOP concepts, and storing data permanently using CSV files.
