from constants import *

class Task:
    #span is list
    def _init_(self, name, span):
        self.name = name
        self.span = span

    def _eq_(self, other):
        return self.name == other.name

    def get_task_mode(self):
        st = self.span[0]
        en = self.span[1]
        if en - st > MINS_IN_DAY:
            return DAY_NIGHT
        st %= MINS_IN_DAY
        en %= MINS_IN_DAY
        if st < en and st >= DAY_START_MINUTES and en < DAY_END_MINUTES:
            return DAY
        elif st < DAY_START_MINUTES:
            if en > DAY_START_MINUTES:
                return DAY_NIGHT
            else:
                if st < en:
                    return NIGHT
                else:
                    return DAY_NIGHT
        elif st < DAY_END_MINUTES:
            return DAY_NIGHT
        else:
            if en < st and en > DAY_START_MINUTES:
                return DAY_NIGHT
            else:
                return NIGHT
def is_legal_task(task):
    pass