from models import(
    Roteador, Notebook, Smartphone
)







if __name__ == "__main__":
    
    roteador = Roteador()
    roteador.senha = "123"

    notebook = Notebook("NOtebok")
    smart = Smartphone("Celular")

    notebook.conectar(roteador, "123")
    smart.conectar(roteador, "12345")

    smart2 = Smartphone("Celular da Samsung")
    smart2.conectar(roteador, "123")

    roteador.listar_dispositivos()
    
    pass