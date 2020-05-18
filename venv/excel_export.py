from xlwt import Workbook
from tkinter.filedialog import asksaveasfile

wb_obj = Workbook()

my_sheet = wb_obj.add_sheet('Imdb')

my_sheet.write(0, 0, 'Title')
my_sheet.write(1, 0, 'Joker')
my_sheet.write(2, 0, 'Interstellar')
my_sheet.write(3, 0, 'Inception')
my_sheet.write(4, 0, 'Avengers Endgame')

f = asksaveasfile(mode='w', defaultextension='.csv')

if f is not None:
    wb_obj.save(f.name)
    f.close()