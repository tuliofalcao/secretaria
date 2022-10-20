import PySimpleGUI as sg

sg.theme('DarkAmber')

fevereiro = 17*9
marco = 21*9
abril = 15*9
maio = 21*9
junho = 20*9
julho = 9*9
agosto = 23*9
setembro = 20*9
outubro = 19*9
novembro = 20*9
dezembro = 16*9

def fev(fevereiro, faltasFev):
    return (100*(fevereiro - faltasFev))//fevereiro

def mar(marco,faltasMar):
    return (100*(marco - faltasMar))//marco

def abr(abril,faltasAbr):
    return (100*(abril - faltasAbr))//abril

def mai(maio,faltasMai):
    return (100*(maio - faltasMai))//maio

def jun(junho,faltasJun):
    return (100*(junho - faltasJun))//junho

def jul(julho,faltasJul):
    return (100*(julho - faltasJul))//julho

def ago(agosto,faltasAgo):
    return (100*(agosto - faltasAgo))//agosto

def setembroF(setembro,faltasSet):
    return (100*(setembro - faltasSet))//setembro

def out(outubro,faltasOut):
    return (100*(outubro - faltasOut))//outubro

def nov(novembro,faltasNov):
    return (100*(novembro - faltasNov))//novembro

def dez(dezembro,faltasDez):
    return (100*(dezembro - faltasDez))//dezembro

def mes():
    layout = [
        [sg.Text('Digite o número de faltas do mês. Se não houver, digite zero. Se o mês ainda não ocorreu, digite "n".')],
        [sg.Text('Fevereiro'), sg.Push(),sg.Input(key='fevereiro')],
        [sg.Text('Março'), sg.Push(),sg.Input(key='março')],
        [sg.Text('Abril'), sg.Push(),sg.Input(key='abril')],
        [sg.Text('Maio'), sg.Push(),sg.Input(key='maio')],
        [sg.Text('Junho'), sg.Push(),sg.Input(key='junho')],
        [sg.Text('Julho'), sg.Push(),sg.Input(key='julho')],
        [sg.Text('Agosto'), sg.Push(),sg.Input(key='agosto')],
        [sg.Text('Setembro'), sg.Push(),sg.Input(key='setembro')],
        [sg.Text('Outubro'), sg.Push(),sg.Input(key='outubro')],
        [sg.Text('Novembro'), sg.Push(),sg.Input(key='novembro')],
        [sg.Text('Dezembro'), sg.Push(),sg.Input(key='dezembro')],
        [sg.Push()],
        [sg.Button('Ok'), sg.Button('Cancelar')]
    ]
    return sg.Window('FREQUÊNCIA - ETEMAC (Auxílio Brasil)', layout,element_justification='center',finalize=True)


janela1 = mes()

meses = []

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Cancelar': # if user closes window or clicks cancel
        break
        
    if window == janela1 and event == 'Ok':
        
        faltasFev = values['fevereiro']
        faltasMar = values['março']
        faltasAbr = values['abril']
        faltasMai = values['maio']
        faltasJun = values['junho']
        faltasJul = values['julho']
        faltasAgo = values['agosto']
        faltasSet = values['setembro']
        faltasOut = values['outubro']
        faltasNov = values['novembro']
        faltasDez = values['dezembro']
        
        if faltasFev != "n":
            faltasFev = int(values['fevereiro'])
            meses.append(fev(fevereiro,faltasFev))

        if faltasMar != 'n':
            faltasMar = int(values['março'])
            meses.append(mar(marco,faltasMar))

        if faltasAbr != 'n':
            faltasAbr = int(values['abril'])
            meses.append(abr(abril,faltasAbr))

        if faltasMai != 'n':
            faltasMai = int(values['maio'])
            meses.append(mai(maio,faltasMai))
        
        if faltasJun != 'n':
            faltasJun = int(values['junho'])
            meses.append(jun(junho,faltasJun))

        if faltasJul != 'n':
            faltasJul = int(values['julho'])
            meses.append(jul(julho,faltasJul))
        
        if faltasAgo != 'n':
            faltasAgo = int(values['agosto'])
            meses.append(ago(agosto,faltasAgo))
        
        if faltasSet != 'n':
            faltasSet = int(values['setembro'])
            meses.append(setembroF(setembro,faltasSet))
        
        if faltasOut != 'n':
            faltasOut = int(values['outubro'])
            meses.append(out(outubro,faltasOut))
        
        if faltasNov != 'n':
            faltasNov = int(values['novembro'])
            meses.append(nov(novembro,faltasNov))
        
        if faltasDez != 'n':
            faltasDez = int(values['dezembro'])
            meses.append(dez(dezembro,faltasDez))

            
        for x in range(len(meses)):
            if len(meses) == 1:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro {meses[0]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 2:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )           
            if len(meses) == 3:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 4:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 5:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 6:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n Julho: {meses[5]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 7:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n Julho: {meses[5]}%\n Agosto: {meses[6]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 8:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n Julho: {meses[5]}%\n Agosto: {meses[6]}%\n Setembro: {meses[7]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 9:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n Julho: {meses[5]}%\n Agosto: {meses[6]}%\n Setembro: {meses[7]}%\n Outubro: {meses[8]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 10:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n Julho: {meses[5]}%\n Agosto: {meses[6]}%\n Setembro: {meses[7]}%\n Outubro: {meses[8]}%\n Novembro: {meses[9]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
            if len(meses) == 11:
                sg.Popup(
                    f"FREQUÊNCIA (PORCENTAGEM)\n\n Fevereiro: {meses[0]}%\n Março: {meses[1]}%\n Abril: {meses[2]}%\n Maio: {meses[3]}%\n Junho: {meses[4]}%\n Julho: {meses[5]}%\n Agosto: {meses[6]}%\n Setembro: {meses[7]}%\n Outubro: {meses[8]}%\n Novembro: {meses[9]}%\n Dezembro: {meses[10]}%\n\n TOTAL: {sum(meses)//len(meses)}%"
                )
window.close()
