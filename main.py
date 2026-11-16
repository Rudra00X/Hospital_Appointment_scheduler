from datetime import datetime

# Global dictionary to store appointments and counter for ID
appointments = {}
id_counter = 101
VALID_DOCTORS = ["Dr. Mehta", "Dr. Rao"]

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validate_time(time_str):
    try:
        t = datetime.strptime(time_str, "%H:%M")
        # Check range 09:00 to 16:30 and 30-minute intervals
        start_time = datetime.strptime("09:00", "%H:%M")
        end_time = datetime.strptime("16:30", "%H:%M")
        if start_time <= t <= end_time and t.minute in (0, 30):
            return True
        return False
    except ValueError:
        return False

def is_slot_available(doctor, date_str, time_str, ignore_id=None):
    for app_id, details in appointments.items():
        if app_id == ignore_id:
            continue
        if (details["doctor"] == doctor and 
            details["date"] == date_str and 
            details["time"] == time_str):
            return False
    return True

def book_appointment():
    global id_counter
    patient = input("Patient: ").strip()
    doctor = input("Doctor: ").strip()
    date_str = input("Date: ").strip()
    time_str = input("Time: ").strip()

    if doctor not in VALID_DOCTORS:
        print(f"Invalid doctor. Choose from: {', '.join(VALID_DOCTORS)}")
        return

    if not validate_date(date_str):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    if not validate_time(time_str):
        print("Invalid time. Please enter a 30-minute slot between 09:00 and 16:30 (HH:MM).")
        return

    if not is_slot_available(doctor, date_str, time_str):
        print(f"Slot unavailable: {doctor} already has an appointment on {date_str} at {time_str}.")
        return

    app_id = f"A{id_counter}"
    id_counter += 1
    appointments[app_id] = {
        "patient": patient,
        "doctor": doctor,
        "date": date_str,
        "time": time_str
    }
    print(f"Appointment booked. ID: {app_id} | {patient} | {doctor} | {date_str} {time_str}")

def view_all():
    if not appointments:
        print("No appointments scheduled.")
        print("Total appointments: 0")
        return
    for app_id, d in appointments.items():
        print(f"{app_id} | {d['patient']} | {d['doctor']} | {d['date']} {d['time']}")
    print(f"Total appointments: {len(appointments)}")

def reschedule_appointment():
    app_id = input("Enter Appointment ID: ").strip()
    if app_id not in appointments:
        print(f"Appointment ID {app_id} not found.")
        return

    new_date = input("New Date (DD-MM-YYYY): ").strip()
    new_time = input("New Time (HH:MM): ").strip()

    if not validate_date(new_date):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    if not validate_time(new_time):
        print("Invalid time. Please enter a 30-minute slot between 09:00 and 16:30 (HH:MM).")
        return

    doctor = appointments[app_id]["doctor"]
    if not is_slot_available(doctor, new_date, new_time, ignore_id=app_id):
        print(f"Slot unavailable: {doctor} already has an appointment on {new_date} at {new_time}.")
        return

    appointments[app_id]["date"] = new_date
    appointments[app_id]["time"] = new_time
    print(f"Appointment {app_id} rescheduled to {new_date} {new_time}.")

def cancel_appointment():
    app_id = input("Enter Appointment ID: ").strip()
    if app_id in appointments:
        del appointments[app_id]
        print(f"Appointment {app_id} cancelled.")
    else:
        print(f"Appointment ID {app_id} not found.")

def main():
    while True:
        print("\n--- Hospital Appointment Scheduler ---")
        print("1. Book")
        print("2. View all")
        print("3. Reschedule")
        print("4. Cancel")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_all()
        elif choice == "3":
            reschedule_appointment()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()