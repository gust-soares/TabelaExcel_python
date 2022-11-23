import openpyxl

book = openpyxl.load_workbook('Planilha de Compras.xlsx')
frutas_page  = book['Frutas']

for rows in frutas_page.iter_rows(min_row=2, max_row = 5):
    for cell in rows:
      #  print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')
        if cell.value == 'Banana':
            cell.value = 'Fruta 1'


book.save('Planilha de Compras V2.xlsx')