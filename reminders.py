from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from datetime import datetime


def reminder_id():
    n = 1
    while True:
        yield n
        n += 1

reminder_id = reminder_id()


@dataclass
class Reminder(ABC):
    title: str
    time: str
    reminder_id: int = field(init=False, default_factory=next(reminder_id))

    @abstractmethod
    def remind(self):
        pass


@dataclass
class SimpleReminder(Reminder):

    def remind(self):
        return f"It's {self.time} : {self.title}"


@dataclass
class MeetingReminder(Reminder):
    participants: list[str]

    def remind(self):
        return f"Meeting Reminder: {self.time} - {self.title} with\n{self.participants}"


@dataclass
class DailyRoutineReminder(Reminder):
    repeater: bool

    def remind(self):
        status = "active" if self.repeater else "inactive"
        return f"Daily Routine: {self.time} - {self.title} (repeat daily: {status})"
