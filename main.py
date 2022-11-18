import xlshandler
import constants
from ptor import *
from person import *
from team import *
from task import *
def main():
    people = xlshandler.read_xls(constants.PEOPLE_FILE)
    teams = xlshandler.read_xls(constants.TEAMS_FILE)
    ptors = xlshandler.read_xls(constants.PTOR_FILE)
    tasks = xlshandler.read_xls(constants.TASKS_FILE)
    for person in people:
        if not is_legal_person(person):
            people.remove(person)
    for team in teams:
        if not is_legal_team(team):
            teams.remove(team)
    for ptor in ptors:
        if not is_legal_ptor(ptor):
            ptors.remove(ptor)
    for task in tasks:
        if not is_legal_task(task):
            tasks.remove(task)
    xlshandler.write_xls(constants.OUTPUT_FILE,people,[])


if __name__ == "__main__":
    main()