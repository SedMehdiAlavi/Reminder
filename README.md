
# Reminder Manager 🕒  

A simple yet powerful reminder management system built in Python for **Maktab Sharif Bootcamp – Series 12 (Maktab 137)**.  
This project demonstrates object-oriented design, logging with rotation, and a command-line interface (CLI) for user interaction.  

---

## 📂 Project Structure
```
Reminder/
├─ reminder.py        # Reminder classes (Simple, Meeting, DailyRoutine)
├─ manager.py         # ReminderManager for managing reminders
├─ logger.py          # Logging configuration with RotatingFileHandler
├─ main.py            # CLI interface for user interaction
└─ reminder.log       # Log file (auto-generated)
```

---

## ✨ Features
- Three types of reminders:
  - **SimpleReminder**: Basic reminder (e.g., buy bread)  
  - **MeetingReminder**: Reminder with participants list  
  - **DailyRoutineReminder**: Daily routine reminder with repeat toggle (active/inactive)  
- Unique ID generation for each reminder using a generator  
- ReminderManager capabilities:
  - Add (`add_reminder`)  
  - Remove (`remove_reminder`)  
  - List (`list_reminders`)  
  - Execute all reminders polymorphically (`execute_all`)  
  - Search by ID (`find_by_id`)  
  - Group reminders (`reminder_group`)  
- Logging all events to `reminder.log` with levels:
  - **INFO**: Adding and executing reminders  
  - **WARNING**: Removing reminders or invalid operations  
  - **ERROR**: Input or execution errors  
- **Log Rotation** with `RotatingFileHandler`:
  - New log file created when size reaches 100KB  
  - Up to 10 old log files preserved  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/SedMehdiAlavi/Reminder.git
   cd Reminder
   ```
2. Run the program:
   ```bash
   python main.py
   ```
3. CLI Menu:
   ```
   1. Add New Reminder
   2. Remove Reminder
   3. Show Reminders List
   4. Execute All Reminders
   5. Search by ID
   6. Group Reminders
   0. Exit
   ```

---

## 📄 Example Output
### Adding a Simple Reminder
```
Title: Buy bread
Time: 17:00
```
Output:
```
Added reminder 1 - Buy bread
```

### Executing All Reminders
```
It's 17:00 : Buy bread
Meeting Reminder: 09:30 - Team Meeting with
['Ali', 'Sara']
Daily Routine: 07:00 - Workout (repeat daily: active)
```

### Log File (`reminder.log`)
```
2025-12-07 17:30:00 - INFO - Added reminder 1 - Buy bread
2025-12-07 17:31:00 - WARNING - Reminder 1 removed.
2025-12-07 17:32:00 - ERROR - Reminder 2 has no title or time.
```

---

## 🏷 Releases

- **v1.0.0**  
  - Initial implementation of core features:  
    - Three reminder types (Simple, Meeting, DailyRoutine)  
    - ReminderManager with add/remove/list/execute/search/group  
    - Logging with rotation (`reminder.log`)  
    - Basic CLI interface  

- **v2.0.0**  
  - **Persistent Storage (JSON-based)**  
    - Reminders are now saved to a local JSON file (`reminders.json`).  
    - When the program restarts, all previously created reminders are automatically reloaded.  
    - This ensures reminders survive between program runs and makes the tool usable in daily life.  

  - **Desktop Notification Adapter**  
    - In addition to console output, reminders now trigger native desktop notifications.  
    - Users receive real-time pop-up alerts for their reminders, improving visibility and usability.  
    - Implemented using the `plyer` library for cross-platform support.  

---

## 🧪 Tests
To run tests (if added in a `tests/` folder):
```bash
pytest tests/
```

---

## 👨‍💻 Developer
Project for **Maktab Sharif Bootcamp – Series 12 (Maktab 137)**  
Developed by [SedMehdiAlavi](https://github.com/SedMehdiAlavi)  

---

