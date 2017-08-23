import xlrd
import StructToUnicodeString as unistr


def uni_from_excel_cell(uni_cell):
    '''
    encodes a xlrd.sheet.Cell to unicode
    :param uni_cell: xlrd.sheet.Cell to encode
    :return: xlrd.sheet.Cell encoded as unicode
    '''
    return unicode(uni_cell.value)

# an example of how to add a new type for parsing
unistr.DEFAULT_PARSE_TABLE[type(xlrd.sheet.Cell)] = uni_from_excel_cell

# an example of real world application(ran in PyCharm),
# might have issue when ran on a console,
# because console might be missing support for those unicode characters
# in that case, either output to a file, or surround with try,except
if __name__ == '__main__':
    book = xlrd.open_workbook('example_book.xlsx')
    for sheet in book.sheets():
        print ('\tan example of what happens without StructToUnicodeString\n')
        for row_index in xrange(0, sheet.nrows):
            print (sheet.row_values(row_index))

        print ('\n\n\tan example of what happens with StructToUnicodeString\n')
        for row_index in xrange(0, sheet.nrows):
            print (unistr.uni_from_struct(sheet.row_values(row_index)))
