def calculaFrequencia():

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

    media = []

    while True:
        mes = input("Informe o mês (para sair digite '0'): ")
        if mes == '0':
            break
            
        elif mes == 'fevereiro':
            n = int(input("Número de faltas: "))
            mediaFevereiro = fev(fevereiro,n)
            media.append(mediaFevereiro)
            print(f"Fevereiro: {mediaFevereiro}")
            
        elif mes == 'março':
            n = int(input("Número de faltas: "))
            mediaMarco = mar(marco,n)
            media.append(mediaMarco)
            print(f"Março: {mediaMarco}")
            
        elif mes == 'abril':
            n = int(input("Número de faltas: "))
            mediaAbril = abr(abril,n)
            media.append(mediaAbril)
            print(f"Abril: {mediaAbril}")
            
        elif mes == 'maio':
            n = int(input("Número de faltas: "))
            mediaMaio = mai(maio,n)
            media.append(mediaMaio)
            print(f"Maio: {mediaMaio}")
            
        elif mes == 'junho':
            n = int(input("Número de faltas: "))
            mediaJunho = jun(junho,n)
            media.append(mediaJunho)
            print(f"Junho: {mediaJunho}")
            
        elif mes == 'julho':
            n = int(input("Número de faltas: "))
            mediaJulho = jul(julho,n)
            media.append(mediaJulho)
            print(f"Julho: {mediaJulho}")
            
        elif mes == 'agosto':
            n = int(input("Número de faltas: "))
            mediaAgosto = ago(agosto,n)
            media.append(mediaAgosto)
            print(f"Agosto: {mediaAgosto}")
            
        elif mes == 'setembro':
            n = int(input("Número de faltas: "))
            mediaSetembro = setembroF(setembro,n)
            media.append(mediaSetembro)
            print(f"Setembro: {mediaSetembro}")
            
        elif mes == 'outubro':
            n = int(input("Número de faltas: "))
            mediaOutubro = out(outubro,n)
            media.append(mediaOutubro)
            print(f"Outubro: {mediaOutubro}")
            
        elif mes == 'novembro':
            n = int(input("Número de faltas: "))
            mediaNovembro = nov(novembro,n)
            media.append(mediaNovembro)
            print(f"Novembro: {mediaNovembro}")
            
        elif mes == 'dezembro':
            n = int(input("Número de faltas: "))
            mediaDezembro = dez(dezembro,n)
            media.append(mediaDezembro)
            print(f"Dezembro: {mediaDezembro}")

    m = sum(media)//len(media)
    print(f"Média Geral: {m}")

def fev(fevereiro, n):
    return (100*(fevereiro - n))//fevereiro

def mar(marco,n):
    return (100*(marco - n))//marco

def abr(abril,n):
    return (100*(abril - n))//abril

def mai(maio,n):
    return (100*(maio - n))//maio

def jun(junho,n):
    return (100*(junho - n))//junho

def jul(julho,n):
    return (100*(julho - n))//julho

def ago(agosto,n):
    return (100*(agosto - n))//agosto

def setembroF(setembro,n):
    return (100*(setembro - n))//setembro

def out(outubro,n):
    return (100*(outubro - n))//outubro

def nov(novembro,n):
    return (100*(novembro - n))//novembro

def dez(dezembro,n):
    return (100*(dezembro - n))//dezembro

calculaFrequencia()
