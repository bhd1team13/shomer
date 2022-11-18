import xlrd
import xlwt


def read_xls(file):
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(0)
    data = []
    for row in range(1, worksheet.nrows):
        elm = []
        for col in range(worksheet.ncols):
            elm.append(worksheet.cell_value(row, col))
        data.append(elm)
    return data


def write_xls(output_file, data, first_row):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('test')
    for index, value in enumerate(first_row):
        sheet.write(0, index, value)
    for i in range(len(data)):
        for index, value in enumerate(data[i]):
            sheet.write(i+1, index, value)
    workbook.save(output_file)
