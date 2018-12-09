import psycopg2
import sys
from Drop_music_interface import interface as i
from DropMusic_Artista import DropMusic_artista as ar
from DropMusic_Musica import DropMusic_Musica as mm
from DropMusic_Concert import DropMusic_Concerto as cc
from DropMusic_User import DropMusic_User as us
from DropMusic_Genero import DropMusic_Genero as ge
from DropMusic_Playlist import DropMusic_Playlist as pl
from DropMusic_Album import DropMusic_Album as aa

class menu:
    
    # login screen
    def inicial():
        print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n Bem vindo à Drop Music! \n *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n MENU: \n Para criar um novo registo pressione a tecla (r) seguido de ENTER \n Para fazer login pressione a tecla (l) seguido de ENTER  ")
        choice=input()
        return choice

    #login/regist
    def login():
        print('username: ')
        user=input()
        print('password: ')
        pas= input()
        return [user, pas]

###########################################   
    def appbar():
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n logout(x)   search(s)'
              + '\n *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n ')
    def sidebar(editor):
        print('MENU: \n p- as minhas playlists \n u-Uploads \n ******')
        if editor:
            print('edit - editar ')
##sidebar + listaAlbuns O QUE NAO FAZ MTO SENTIDO
    def mainMenu():
        aa.listaAlbum()
        #print('MENU: \n p- as minhas playlists \n u-Uploads \n ******')
        ans=input()
        return ans
    def mainMenuM():
        mm.listMusic()
        ans=input()
        return ans
##########################################

    # ask or an album
    def details():
        print('Escolha um álbum: \n')
        title=input('título: ')
        data=input('data de lançamento (dd/mm/aaaa): ')
        return [title, str(data)]


    def showingAlbum():
        print ('********************** \n Comentários (sc) ')
        print ('********************** \n Músicas (m) \n')
        print ('********************** \n Deixar comentário (c) \n')
        print ('back(b)')
        x=input()
        return x


    def comment():
        points=input('pontuação (1-5): ')
        cause= input('justificação e comentários: ')
        return [points, cause]


    def alterAlbum():
        print("""alterar título - t \n alterar data de lançamento - d
        \n alterar editora - ed \n alterar estúdio - as
        \n remover artista - r \n adicionar artista - a
        \n remover música - rm \n adicionar música - am""")
        
        print('voltar (v)')
        x=input()
        return x

    def delete():
        print("""Ao completar esta ação estará a apagar permanentemente este objeto e todos os que se relacionam com ele
        \n Tem a certeza que pretende porsseguir?""")
        v=input ('confirmar(v)  *-*-* cancelar (c)')
        return v

    
    def setValue():
        x=input('novo valor: ')
        v=input ('confirmar(v)  *-*-* cancelar (c)')
        if v=='v':
            return x
        else:
            return 'q'


    def alterMusic():
        print("""alterar nome - t \n alterar data de lançamento - d \n alterar letra - l \n adicionar musica a um álbum - aa \n
        \n alterar duracao - du \n adicionar/remover artista - r \n adicionar/remover genero - a \n adicionar/remover concerto - c""")
        print('voltar (v)')
        x=input()
        return x


    def editorMenu():
        print(""""Adicionar Album - a \n Permissões - up \n Adicionar Música - m
        \n Adicionar Concerto (c) \n Adicionar Artista (ar) \n Adicionar Género (g)""")## a acrescentar opcoes
        print('voltar (v)')
        x=input()
        return x

    def askType():
        x=input('banda(b)/artista(a)')
        return x

    def addArtist():
        print('(*) campo de preenchimento obrigatório')
        nome=input('nome(*): ')
        bio=input('biografia: ')
        return [nome,bio]
    def addArt():
        dataN=input('data de nascimento(*): ')
        dataO=input('data de óbito (null)(*): ')
        localN= input('local de nascimento: ')
        return [dataN,dataO, localN]
        
    def addBand():
        
        dataI=input('data de formação: ')
        localI=input('local de formação: ')
        dataF=input('data de fim (null) (*): ')

        print('artistas:')
        oo=input('+ artista (a)')
        artistas=[]
        funcoes=[]
        datasE=[]
        datasS=[]
        while oo=='a':
            artista=input('id do artista: ')
            c=ar.verifyA(artista)
            if c:
                artistas.append(artista)
                funcao=input('função do artista na banda: ')
                dataE=input('data de entrada: ')
                dataS=input('data de saída: ')
                funcoes.append(funcao)
                datasE.append(dataE)
                datasS.append(dataS)

            oo=input('+ artista (a)')

        return [dataI, localI, dataF, artistas, funcoes, datasE, datasS]

    def addAlbum():
        print('(*) campo de preenchimento obrigatório')
        titulo=input('titulo(*): ')
        data=input('data de lançamento(*): ')
        estudio=input('estúdio: ')
        editora=input('editora: ')

        print('artistas:')
        oo=input('+ artista (a)')
        artistas=[]

        while oo=='a':
            artista=input('id do artista: ')
            c=ar.verifyA(artista)

            if c:
                artistas.append(artista)
                
            oo=input('+ artista (a)')

        print('musicas (por ordem):') ### SE FIZERMOS ASSIM ATE E MAIS FACIL BOTAR LA SERIAL NA BD
        o=input('+ musica (m)')
        musicas=[]

        while o=='m':
            musica=input('id da musica: ') ##### E SE ELE POE ESTES VALORES MAL?!
            c=mm.verifyM(musica)

            if c:
                musicas.append(musica)

            o=input('+ musica (m)')

        return [titulo, data, estudio, editora, artistas, musicas]

    def addMusic():
        print('(*) campo de preenchimento obrigatório')
        titulo=input('titulo(*): ')
        data=input('data de lançamento(*): ')      ##NAO DEIXA ADICIONAR SEM DATA OU DURACAO.. HA PROBLEMA?
        duracao=input('duração(*): ')
        letra=input('letra: ')
        
        print('artistas:')
        oo=input('+ artista (a)')
        artistas=[]
        funcoes=[]
        while oo=='a':
            artista=input('id do artista: ')
            c=ar.verifyA(artista)
            if c:
                artistas.append(artista)
                funcao=input('função do artista na música: ')
                funcoes.append(funcao)
            oo=input('+ artista (a)')

        print('géneros musicais:') ### SE FIZERMOS ASSIM ATE E MAIS FACIL BOTAR LA SERIAL NA BD
        o=input('+ genero (g)')
        generos=[]

        while o=='g':
            genero=input('género: ') ##### E SE ELE POE ESTES VALORES MAL?!
            c=ge.verifyG(genero)

            if c:
                generos.append(genero)

            o=input('+ género (g)')

        return [titulo, data, duracao, letra,funcoes, artistas, generos]        

    def addConcert():
        print('(*) campo de preenchimento obrigatório')
        titulo=input('tour: ')
        data=input('data(*) : ')
        localizacao=input('localização: ')
        
        print('artistas (por ordem de atuação):')
        oo=input('+ artista (a)')
        artistas=[]

        while oo=='a':
            artista=input('id do artista: ')
            c=ar.verifyA(artista)
            if c:
                artistas.append(artista)
            oo=input('+ artista (a)')

        print('músicas (por ordem):') ### SE FIZERMOS ASSIM ATE E MAIS FACIL BOTAR LA SERIAL NA BD
        o=input('+ musica (m)')
        musicas=[]
############ ELE TA A COMECAR AS POSICOES NO CONCERTO ALBUM ETC EM 0 EM VEZ DE 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
        while o=='m':
            musica=input('id da musica: ') ##### E SE ELE POE ESTES VALORES MAL?!
            c=mm.verifyM(musica)

            if c:
                musicas.append(musica)

            o=input('+ musica (m)')

        return [titulo, data, localizacao, artistas, musicas]      
        
    def selectPlaylist():
        print('voltar(v)')
        a=input('nome da playlist: ')
        return a


    def selectUser():
        print('voltar(v)')
        a=input('nome do user : ')
        return a


    def getSong():
        print('voltar(v)')
        a=input('posicao da musica: ')
        return a


    def showmusic():
        print("""artistas - a \n concerto - c \n adicionar a playlist - ap \n""") ##upload
        x=input()
        return x


    def choosePlaylist(user):
        publica=None
        exists=None

        print('select a playlist (s): ')
        pl.showPlaylists(user)
        print ('create new (cn)')
        x=input()
        choosenlist=input('nome: ')

        if x=='s':
            exists='Yes'

        elif x=='cn':
            publica=input('publica (True/False): ')
            exists='No'
        return [choosenlist, exists, publica]

    def addRemove():
        x=input('adicionar (a)/ remover (d): ')
        return x
    
    def askGenero():
        gen=input('género: ')
        return gen
    def askId():
        x=input('introduza um id: ')
        return x
    def askFuncao():
        gen=input('função: ')
        return gen

    def searchMusic():
        print('Pesquisa por: \n 1) nome \n 2) id \n 3) Nome do Artista')
        print('\n 4) Id do Artista \n 5) Album \n 6) Genero \n 7) Data \n')
        print('8) Pontuação \n 9) Letra')
        value=''
        atributo= input()
        if atributo =='1':
            value = input('introduza o nome(ou parte do mesmo): ')
        elif atributo =='2':
            value = input('introduza o id da música: ')
        elif atributo =='3':
            value = input('introduza o nome do Artista(ou parte do mesmo): ')
        elif atributo =='4':
            value = input('introduza o id do artista: ')
        elif atributo =='5':
            value = input('introduza o título do album (ou parte do mesmo): ')
        elif atributo =='6':
            value = input('introduza o genero: ')
        elif atributo =='7':
            value = input('introduza a data: ')
        elif atributo =='8':
            value = input('introduza a pontuacao: ')
        elif atributo =='9':
            value = input('introduza a letra (ou parte da mesma): ')
        return atributo, value

    def search_menu():
        print('o que deseja procurar? ')
        print(""" Música - m  """)
        choice= input()
        return choice
