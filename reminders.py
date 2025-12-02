from dataclasses import dataclass
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

    @abstractmethod
    def remind(self):
        pass


@dataclass
class SimpleReminder(Reminder):
    unique_id: int = next(reminder_id)

    @abstractmethod
    def remind(self):
        if self.time == datetime.now().time():
            print(f"{self.time} - {self.title}")


@dataclass
class MeetingReminder(Reminder):
    participants: list[str]
    unique_id: int = next(reminder_id)

    @abstractmethod
    def remind(self):
        if self.time == datetime.now().time():
            print(f"meeting: {self.time} - {self.title} with\n{self.participants}")


@dataclass
class DailyRoutineReminder(Reminder):
    repeater: bool
    unique_id: int = next(reminder_id)

    @abstractmethod
    def remind(self):
        if self.time == datetime.now().time() and self.repeater:
            print(f"daily: {self.time} - {self.title}")
