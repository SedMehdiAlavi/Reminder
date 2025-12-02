from dataclasses import dataclass

def reminder_id():
    n = 1
    while True:
        yield n
        n += 1

reminder_id = reminder_id()

@dataclass
class Reminder:
    title: str
    time: str

@dataclass
class SimpleReminder(Reminder):
    unique_id: int = next(reminder_id)


@dataclass
class MeetingReminder(Reminder):
    participants: list[str]
    unique_id: int = next(reminder_id)



@dataclass
class DailyRoutineReminder(Reminder):
    repeater: bool
    unique_id: int = next(reminder_id)


