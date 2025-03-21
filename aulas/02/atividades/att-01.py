import datetime

def dataAtual():
    now = datetime.datetime.now()
    print(f"Data atual: ", now.strftime("%Y-%m-5d %H:%M:%S"))

dataAtual()