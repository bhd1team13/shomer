from task import Task
from constants import *


class Person:
    def _init_(self, name, team):
        self.name = name
        self.team = team
        self.ptors = list()
        self.night = True

    def add_ptor(self, ptor):
        self.ptors.append(ptor)

    def remove_ptor(self, ptor):
        self.ptors = [p for p in self.ptors if p != ptor]

    def change_time_mode(self, can_at_night):
        self.night = can_at_night

    def _eq_(self, other):
        return self.name == other.name

    def can_do_task(self, task):
        assert isinstance(task, Task)
        for p in self.ptors:
            if task.name in p.illegal_tasks:
                return False
        if not self.night and task.get_task_mode() in [NIGHT, DAY_NIGHT]:
            return False
        return True
def is_legal_person(person):
    pass