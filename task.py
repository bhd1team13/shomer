class Task:
    #span is list
    def _init_(self, name, span):
        self.name = name
        self.span = span

    def _eq_(self, other):
        return self.name == other.name