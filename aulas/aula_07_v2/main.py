from nicegui import ui, app
from filme_obj_models import Diretor,Filme, Genero, Classificacao
from datetime import datetime
#from dados import dados_filmes, diretor1, diretor2, diretor3, diretor4, diretor5

#ui.run()




if __name__ == "__main__":
    from rich import print
    from filme_controller import FilmeController

    filme_controller = FilmeController()
    
    #for filme in filme_controller.listar_filmes():
    #    print("Título: " + filme.titulo)
    
    for diretor in filme_controller.listar_diretores():
        print(diretor.nome)
        
    for classificacao in filme_controller.listar_classificacoes():
        print(classificacao.descricao)
    
    # Initialize Database
    #test_create_movie() # teste de inserção de um filme
    #test_delete_movie(1)
    
    #db = SessionLocal() # db == database == banco de dados
    #filme = crud.get_filme(db, filme_id=2)
    #filme.titulo = "Avatar updated"
    #crud.update_filme(db, filme)

    #def test_add_filme():
    #    db = SessionLocal()
#
    #    for filme in filmes:
    #        add_filme(db, filme)
#
    #def test_list_filmes():
    #    db = SessionLocal()
    #    
    #    for filme in get_filmes(db):
    #        print("Titulo: " + filme.titulo)
#
    #def test_add_diretores():
    #    db = SessionLocal()
    #    add_diretor(db, diretor1)
    #    add_diretor(db, diretor2)
    #    add_diretor(db, diretor3)
    #    add_diretor(db, diretor4)
    #    add_diretor(db, diretor5)

    #test_add_diretores()


    #test_add_filme()

    ##test_list_filmes() # select all

    #print(results)
    
