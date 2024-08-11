import openpyxl

fundos = {}

class Fundo:
    def __init__ (self):
        self.sigla = ""
        self.setor = 0.0
        self.preço_atual = 0.0
        self.liquidez = 0.0
        self.pvp = 0.0
        self.divyeldac = 0.0
        self.divyeldmedia = 0.0
        self.patrliquid = 0.0

plano = openpyxl.load_workbook("Filtro Fii.xlsx")
pagina = plano['Fundos']

for rows in pagina.iter_rows(min_row = 3, max_row = 79,max_col=8):
    fundo = Fundo()
    flag = 1
    for cell in rows:
        if flag == 1:
            fundo.sigla = str(cell.value)
        elif flag == 2:
            fundo.setor = str(cell.value)
        elif flag == 3:
            fundo.preço_atual = float(str(cell.value).replace(",","."))
        elif flag == 4:
            fundo.liquidez = float(str(cell.value).replace(",","."))
        elif flag == 5:
            fundo.pvp = float(str(cell.value).replace(",","."))
        elif flag == 6:
            fundo.divyeldac = float(str(cell.value).replace(",","."))
        elif flag == 7:
            fundo.divyeldmedia = float(str(cell.value).replace(",","."))
        elif flag == 8:
            fundo.patrliquid = float(str(cell.value).replace(",","."))
        flag+=1
    fundos[fundo.sigla] = fundo
for cada in fundos.values():
    print(cada.sigla, end= " | ")
    print(cada.setor, end= " | ")
    print(cada.preço_atual, end= " | ")
    print(cada.liquidez, end= " | ")
    print(cada.pvp, end= " | ")
    print(cada.divyeldac, end= " | ")
    print(cada.divyeldmedia, end= " | ")
    print(cada.patrliquid,"\n")