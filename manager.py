from reminders import *
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("ReminderManager")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    filename="reminder.log",
    mode="a",
    maxBytes=100 * 1024,
    backupCount=3,
    encoding="utf-8"
)

formatter = logging.Formatter("%(levelname)s - %(message)s")
handler.setFormatter(formatter)

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, reminder):
        if not reminder.title or not reminder.time:
            logger.error(f"Reminder {reminder.reminder_id} has no title or time.")
            return

        self.reminders.append(reminder)
        logger.info(f"Added reminder {reminder.reminder_id} - {reminder.title}")


    def remove_reminder(self, reminder_id):
        self.reminders = [r for r in self.reminders if r.reminder_id != reminder_id]
        logger.warning(f"Reminder {reminder_id} removed.")

    def list_reminders(self):
        for r in self.reminders:
            print(f"{r.reminder_id}: {r.title} @ {r.time}")

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

        print(groups)

    def execute_all(self):
        for reminder in self.reminders:
            try:
                msg = reminder.remind()
                print(msg)
                logger.info(f"Reminder {reminder.reminder_id} executed: {msg}")

            except Exception as e:
                logger.error(f"Error executing reminder {reminder.reminder_id}: {e}")

    def find_by_id(self, reminder_id):
        for r in self.reminders:
            if r.reminder_id == reminder_id:
                print(f"{r.reminder_id}: {r.title} @ {r.time}")
                return
        print(f"reminder with Id '{reminder_id}' not found")