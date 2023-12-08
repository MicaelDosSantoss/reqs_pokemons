import openpyxl 
from openpyxl.styles import Font, Alignment, Side, Border, PatternFill
import json

excel = openpyxl.Workbook() # planilha do excel

print(excel.sheetnames)

excel.create_sheet('Pokedex') # Criação da tabela de Dados

excel_pg = excel['Pokedex']
with open('Pokedex.json','r') as Poke:
    pokedex_json = json.load(Poke)
title = ['número do pokemon','Nome de pokemon','Tipos']

excel_pg.append(title)

cont_tab = 1

for poke in pokedex_json:
    row_data = ([poke["numero"], poke["pokemon"]])

    for tipo in poke['tipos']:
        row_data.append(tipo)

        
    
    excel_pg.append(row_data)

    cont_tab += 1

align_center = Alignment(horizontal='center',vertical='center') # Alinhar os itens nas células do excel
border_style = Side(style='thin') # Inserir bordar na tabela
font_bold = Font(bold=True)


# Aplicar formatação a todas as células
for row in excel_pg.iter_rows(min_row=1, max_row=len(pokedex_json) + 1, min_col=1, max_col=len(title)):
    for cell in row:
        cell.alignment = align_center
        cell.border = Border(left=border_style, right=border_style, top=border_style, bottom=border_style)
        if cell.row == 1:  # Tornar títulos em negrito
            cell.font = font_bold

excel_pg.merge_cells('C1:D1')

colunaD = excel_pg['D']

cont = 1

for col in colunaD:
    cont += 1
    if col.value is None:
        excel_pg.merge_cells(f'C{cont}:D{cont}')

excel.save('Pokedex.xlsx') # Salvar alterações