from reminders import *
from manager import *

manager = ReminderManager()
while True:
    start = input(
        # "Reminder Manager System\n"
        # f"{'=' * 30}\n"
        "\n1. Add New Reminder\n"
        "2. Remove Reminder\n"
        "3. Show Reminders List\n"
        "4. Execute All Reminders\n"
        "5. Search by ID\n"
        "6. Group Reminders\n"
        "0. Exit\n"
    )

    if start == "1":
        r_type = input("Simple: 1\nMeeting: 2\nDaily: 3\n")
        if r_type == "1":
            title = input("Title: ")
            time = input("Time(eg 18:30): ")
            simple = SimpleReminder(title, time)
            manager.add_reminder(simple)
            continue

        elif r_type == "2":
            title = input("Title: ")
            time = input("Time: ")
            participants = input("Participants(separate by comma):\n").split(",")
            meeting = MeetingReminder(title, time, participants)
            manager.add_reminder(meeting)
            continue

        elif r_type == "3":
            title = input("Title: ")
            time = input("Time: ")
            daily = DailyRoutineReminder(title, time)

            repeat = input("Repeat? (y/n) ")
            if repeat == "y":
                daily.activate()
            manager.add_reminder(daily)
            continue

    elif start == "2":
        manager.list_reminders()
        rid = input("Enter reminder ID:\n")
        manager.remove_reminder(rid)
        continue

    elif start == "3":
        manager.list_reminders()
        continue

    elif start == "4":
        manager.execute_all()
        continue

    elif start == "5":
        rid = input("Reminder ID:\n")
        manager.find_by_id(rid)
        continue

    elif start == "6":
        gp = input("Group Reminders by (type|time):\n")
        manager.reminder_group(gp)
        continue

    elif start == "0":
        break