# Project Summary: Hospital Appointment Scheduler

## 1. Objective
To design and implement a reliable command-line scheduling tool using core Python data structures and date-time validation without relying on external databases.

## 2. Core Concepts Used
- *Dictionaries (dict):* Used as an in-memory database where each auto-generated Appointment ID (A101, A102, etc.) acts as a unique key mapping to a nested dictionary containing patient, doctor, date, and time.
- *datetime Module:* Used datetime.strptime() for strict format checking (%d-%m-%Y and %H:%M), calendar validity verification, and time-range boundary validation (09:00 to 16:30).
- *Modular Functions:* Separated concerns into dedicated functions (book_appointment(), view_all(), reschedule_appointment(), cancel_appointment(), validate_date(), validate_time(), and is_slot_available()).
- *Control Flow (while True):* Keeps the console menu active until the user explicitly chooses Exit (5).

## 3. Edge Cases Handled
1. *Double Booking:* Blocks a slot if the selected doctor already has an appointment at the exact date and time.
2. *Invalid Calendar Dates:* Rejects non-existent dates like 31-11-2026.
3. *Invalid Time Intervals:* Rejects times outside 09:00–16:30 or non-30-minute intervals (e.g., 10:15).
4. *Reschedule Self-Conflict:* When rescheduling an existing appointment, ignores its own current ID while checking for slot availability.

## 4. Test Execution Summary
All 4 prescribed test cases (Normal Booking, Boundary Time 16:30, Invalid Date/Duplicate Slot Rejection, and Reschedule/Cancel/View lifecycle) execute cleanly from an empty schedule and match expected outputs.