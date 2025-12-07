from logger import setup_logging
from reminders import *
logger = setup_logging()
import json
from plyer import notification

class ReminderManager:
    def __init__(self):
        self.reminders = []
        self.storage = "reminders.json"
        self.load_reminders()

    def save_reminders(self):
        try:
            file = open(self.storage, "w", encoding="utf-8")
            json.dump([r.__dict__ for r in self.reminders], file, indent=4)
            file.close()
            logger.debug("Reminders saved to storage")
        except Exception as e:
            logger.error(f"Failed to save reminders: {e}")

    def load_reminders(self):
        try:
            file = open(self.storage, "r")
            data = json.load(file)
            for r in data:
                if "participants" in r:
                    self.reminders.append(MeetingReminder(**r))

                elif "repeater" in r:
                    self.reminders.append(DailyRoutineReminder(**r))

                else:
                    self.reminders.append(SimpleReminder(**r))
            file.close()
            logger.debug("Reminders loaded from storage")
        except FileNotFoundError:
            logger.info("No existing storage file found. Starting fresh.")

        except Exception as e:
            logger.error(f"Failed to load reminders: {e}")

    def add_reminder(self, reminder):
        if not reminder.title or not reminder.time:
            logger.error(f"Reminder {reminder.reminder_id} has no title or time.")
            return

        self.reminders.append(reminder)
        self.save_reminders()
        logger.info(f"Added reminder {reminder.reminder_id} - {reminder.title}")


    def remove_reminder(self, reminder_id):
        self.reminders = [r for r in self.reminders if r.reminder_id != int(reminder_id)]
        self.save_reminders()
        logger.warning(f"Reminder {reminder_id} removed.")

    def list_reminders(self):
        for r in self.reminders:
            print(f"{r.reminder_id}: {r.title} @ {r.time}")
        logger.debug("reminders listed.")

    def reminder_group(self, group_by="type"):
        groups = {}
        for reminder in self.reminders:
            key = (
                type(reminder).__name__ if group_by == "type"
                else reminder.time if group_by == "time"
                else None
            )
            if key is not None:
                groups.setdefault(key, []).append(reminder.__dict__)

        for k, v in groups.items():
            print(k)
            for r in v:
                print(r)
        logger.debug(f"reminders grouped by {group_by}.")

    def execute_all(self):
        for reminder in self.reminders:
            try:
                msg = reminder.remind()
                print(msg)
                notification.notify(
                    title="Reminder",
                    message=msg,
                    timeout=5
                )
                logger.info(f"Reminder {reminder.reminder_id} executed: {msg}")

            except Exception as e:
                logger.error(f"Error executing reminder {reminder.reminder_id}: {e}")

    def find_by_id(self, reminder_id):
        for r in self.reminders:
            if r.reminder_id == int(reminder_id):
                print(f"{r.reminder_id}: {r.title} @ {r.time}")
                return
        print(f"reminder with Id '{reminder_id}' not found")
        logger.debug("reminder searched by id.")