from reminders import *
import logging

logging.basicConfig(level=logging.INFO,
                    filename='reminder.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, reminder):
        if not reminder.title or not reminder.time:
            logging.error(f"{reminder.reminder_id} has no title or time.")
            return

        self.reminders.append(reminder)
        logging.info(f"Added reminder {reminder.reminder_id} - {reminder.title}")


    def remove_reminder(self, reminder_id):
        self.reminders = [r for r in self.reminders if r.reminder_id != reminder_id]
        logging.warning(f"Reminder {reminder_id} removed.")

    def list_reminders(self):
        return [f"{r.reminder_id}: {r.title} @ {r.time}" for r in self.reminders]

    def reminder_group(self, group_by="type"):
        groups = {}
        for reminder in self.reminders:
            key = (
                type(reminder).__name__ if group_by == "type"
                else reminder.time if group_by == "time"
                else reminder.category if group_by == "category"
                else None
            )
            if key is not None:
                groups.setdefault(key, []).append(reminder)

        return groups

    def execute_all(self):
        for reminder in self.reminders:
            try:
                msg = reminder.remind()
                print(msg)
                logging.info(f"Reminder {reminder.reminder_id} executed: {msg}")

            except Exception as e:
                logging.error(f"Error executing reminder {reminder.reminder_id}: {e}")

    def find_by_id(self, reminder):
        return next((r for r in self.reminders if r.reminder_id == reminder_id), None)