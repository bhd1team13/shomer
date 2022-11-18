class Ptor:
    def _init_(self, name, illegal_tasks):
        self.name = name
        self.illegal_tasks = illegal_tasks

    def _eq_(self, other):
        return self.name == other.name