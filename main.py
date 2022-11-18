import xlshandler
import constants

def main():
    people = xlshandler.read_xls(constants.PEOPLE_FILE)
    teams = xlshandler.read_xls(constants.TEAMS_FILE)
    ptor = xlshandler.read_xls(constants.PTOR_FILE)
    tasks = xlshandler.read_xls(constants.TASKS_FILE)
    xlshandler.write_xls(constants.OUTPUT_FILE,people,[])


if __name__ == "__main__":
    main()