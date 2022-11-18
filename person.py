class Person:
    def _init_(self, name, team):
        self.name = name
        self.team = team
        self.ptor = list()
        self.night = True

    def add_ptor(self, ptor):
        self.ptor.append(ptor)

    def remove_ptor(self, ptor):
        self.ptor = [p for p in self.ptor if p != ptor]

    def change_time_mode(self, can_at_night):
        self.night = can_at_night

    def _eq_(self, other):
        return self.name == other.name