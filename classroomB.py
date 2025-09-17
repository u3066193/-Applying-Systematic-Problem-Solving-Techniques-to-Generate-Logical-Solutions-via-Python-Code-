u3066193
 
Date: 17/09/2025

# import time
from datetime import datetime

  # --- Data Structures ---
students_checked_in = {}  # name: timestamp
equipment_status = {
    "Projector": True,
    "Smartboard": False,
    "Speakers": True
}
temperature_logs = []  # list of (timestamp, temperature)

# --- Helper Functions ---
def check_in_student(name: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    students_checked_in[name] = timestamp
    print(f"{name} checked in at {timestamp}")

def update_equipment(name: str, status: bool):
    if name in equipment_status:
        equipment_status[name] = status
        print(f"{name} status updated to {'Working' if status else 'Broken'}")
    else:
        print(f"{name} not found in equipment list.")

def log_temperature(temp: float):
    timestamp = datetime.now().strftime("%H:%M:%S")
    temperature_logs.append((timestamp, temp))
    print(f"Logged temperature: {temp}°C at {timestamp}")

def show_equipment_report():
    print("\n--- Equipment Status Report ---")
    for item, status in equipment_status.items():
        print(f"{item}: {'Working' if status else 'Broken'}")

def show_temperature_trend():
    print("\n--- Temperature Logs ---")
    for log in temperature_logs:
        print(f"{log[0]} → {log[1]}°C")

def show_check_in_summary():
    print("\n--- Student Check-ins ---")
    for student, time in students_checked_in.items():
        print(f"{student} checked in at {time}")
# --- Simulated Loop ---
def classroom_monitor():
    print("Smart Classroom Monitor Started\n")
    while True:
        print("\nOptions: [1] Check-in [2] Update Equipment [3] Log Temp [4] Reports [5] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            check_in_student(name)

        elif choice == "2":
            name = input("Enter equipment name: ")
            status_input = input("Is it working? (yes/no): ").lower()
            status = True if status_input == "yes" else False
            update_equipment(name, status)

        elif choice == "3":
            try:
                temp = float(input("Enter temperature (°C): "))
                log_temperature(temp)
            except ValueError:
                print("Invalid temperature input.")

        elif choice == "4":
            show_check_in_summary()
            show_equipment_report()
            show_temperature_trend()

        elif choice == "5":
            print("Exiting Smart Classroom Monitor.")
            break

        else:
            print("Invalid option. Try again.")

# --- Run the Monitor ---
# Uncomment below to run interactively
# classroom_monitor()





# -----------------------------
# SMART CLASSROOM MONITOR APP
# -----------------------------

registered_students = {"Citi_wadie", "J_xier", "ku", "k_Cli"}
checked_in_students = set()

equipment_status = {
    "Projector": True,
    "Whiteboard": True,
    "Speaker System": False,
    "Lights": True
}

temperature_logs = []

# -----------------------------
# CHECK-IN SYSTEM
# -----------------------------
def check_in(student_name: str) -> bool:
    """Registers a student check-in if they are registered."""
    if student_name in registered_students:
        checked_in_students.add(student_name)
        print(f"{student_name} checked in successfully.")
        return True
    else:
        print(f"{student_name} is not registered.")
        return False

def attendance_report():
    """Prints attendance summary."""
    print("\n--- Attendance Report ---")
    for student in registered_students:
        status = "Present" if student in checked_in_students else "Absent"
        print(f"{student}: {status}")

# -----------------------------
# EQUIPMENT MONITOR
# -----------------------------
def update_equipment(name: str, status: bool):
    """Updates the status of classroom equipment."""
    equipment_status[name] = status
    print(f"Equipment '{name}' status updated to {'Working' if status else 'Faulty'}.")

def equipment_report():
    """Displays current equipment status."""
    print("\n--- Equipment Status ---")
    for item, status in equipment_status.items():
        print(f"{item}: {'Working' if status else 'Faulty'}")

# -----------------------------
# TEMPERATURE LOGGER
# -----------------------------
def log_temperature(temp: float):
    """Logs the temperature with timestamp."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature_logs.append((timestamp, temp))
    print(f"Logged temperature: {temp}°C at {timestamp}")

def temperature_summary():
    """Analyzes temperature logs."""
    print("\n--- Temperature Summary ---")
    if not temperature_logs:
        print("No temperature data available.")
        return

    temps = [entry[1] for entry in temperature_logs]
    avg_temp = sum(temps) / len(temps)
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Max Temperature: {max(temps):.2f}°C")
    print(f"Min Temperature: {min(temps):.2f}°C")

# -----------------------------
# MAIN LOOP
# -----------------------------
def main():
    print("Welcome to Smart Classroom Monitor\n")

    while True:
        print("\nChoose an option:")
        print("1. Check-in student")
        print("2. View attendance report")
        print("3. Update equipment status")
        print("4. View equipment report")
        print("5. Log temperature")
        print("6. View temperature summary")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            name = input("Enter student name: ")
            check_in(name)

        elif choice == "2":
            attendance_report()

        elif choice == "3":
            eq_name = input("Enter equipment name: ")
            status_input = input("Is it working? (yes/no): ").lower()
            status = True if status_input == "yes" else False
            update_equipment(eq_name, status)

        elif choice == "4":
            equipment_report()

        elif choice == "5":
            try:
                temp = float(input("Enter temperature (°C): "))
                log_temperature(temp)
            except ValueError:
                print("Invalid temperature format.")

        elif choice == "6":
            temperature_summary()

        elif choice == "7":
            print("Exiting Smart Classroom Monitor. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()






# Pseudocode
  # -----------------------------
 # DATA STRUCTURES
 # -----------------------------

registered_students = {"S001", "S002", "S003", "S004"}  # Set of student IDs
check_in_logs = []  # List of (student_id, timestamp) tuples

equipment_status = {
    "Projector": True,
    "Smartboard": False,
    "Speakers": True,
    "WiFi": True
}

temperature_logs = []  # List of float values

# -----------------------------
# FUNCTIONS
# -----------------------------

def check_in(student_id: str, timestamp: str):
    if student_id in registered_students:
        check_in_logs.append((student_id, timestamp))
        print(f"Check-in successful for {student_id}")
    else:
        print("Student ID not recognized.")


def update_equipment(equipment_name: str, is_working: bool):
    if equipment_name in equipment_status:
        equipment_status[equipment_name] = is_working
        print(f"Updated status for {equipment_name}")
    else:
        print(f"Unknown equipment: {equipment_name}")

def log_temperature(temp: float):
    if 15.0 <= temp <= 30.0:
        temperature_logs.append(temp)
        print(f"Temperature logged: {temp}°C")
    else:
        print(f"Temperature out of range: {temp}°C")

def report_faulty_equipment():
    faulty = [name for name, status in equipment_status.items() if not status]
    return faulty

def average_temperature():
    if not temperature_logs:
        return None
    return sum(temperature_logs) / len(temperature_logs)


# -----------------------------
# MAIN LOOP
# -----------------------------

def main():
    while True:
        print("\nClassroom Monitor Menu")
        print("1. Student Check-in")
        print("2. Update Equipment Status")
        print("3. Log Temperature")
        print("4. Show Faulty Equipment")
        print("5. Show Average Temperature")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            sid = input("Enter student ID: ")
            time = input("Enter timestamp: ")
            check_in(sid, time)

        elif choice == "2":
            eq = input("Enter equipment name: ")
            status_input = input("Is it working? (yes/no): ").strip().lower()
            status = status_input == "yes"
            update_equipment(eq, status)

        elif choice == "3":
            temp_input = input("Enter temperature (°C): ")
            try:
                temp = float(temp_input)
                log_temperature(temp)
            except ValueError:
                print("Invalid temperature format.")

        elif choice == "4":
            issues = report_faulty_equipment()
            print("Faulty Equipment:", issues if issues else "All equipment is working.")

        elif choice == "5":
            avg = average_temperature()
            if avg is not None:
                print(f"Average Temperature: {round(avg, 2)}°C")
            else:
                print("No temperature data available.")

        elif choice == "6":
            print("Exiting Classroom Monitor.")
            break

        else:
            print("Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    main()






# Test runs & notes

monitor = SmartClassroomMonitor()
monitor.log_check_in(101, True)
assert monitor.check_ins[101] == True
monitor.update_equipment("Projector", False)
assert monitor.equipment_status["Projector"] == False
monitor.record_temperature(22.5)
monitor.record_temperature(23.0)
assert monitor.average_temperature() == 22.75


