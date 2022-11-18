class Team:
    def _init_(self, name, days_hour_span=None):
        self.name = name
        self.days_hour_span = days_hour_span

    def _eq_(self, other):
        return self.name == other.name
def is_legal_team(team):
    pass