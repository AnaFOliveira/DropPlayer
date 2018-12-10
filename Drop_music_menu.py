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

    def mainMenu():
        aa.listaAlbum()
        ans=input()
        return ans
    def mainMenuM():
        mm.listMusic()
        ans=input()
        return ans
    def mainMenuC():
        cc.listaConcertos()
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
        print(atributo+'-'+value)
        return atributo, value

    def editorMenu():
        print(""""Adicionar Album - a \n Permissões - up \n Adicionar Música - m
        \n Adicionar Concerto (c) \n Adicionar Artista (ar) \n Adicionar Género (g)""")
        print('voltar (v)')
        x=input()
        return x

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

        print('musicas (por ordem):') 
        o=input('+ musica (m)')
        musicas=[]

        while o=='m':
            musica=input('id da musica: ') 
            c=mm.verifyM(musica)

            if c:
                musicas.append(musica)

            o=input('+ musica (m)')

        return [titulo, data, estudio, editora, artistas, musicas]
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



    def showingBanda(idAr):
        ar.detailBandas(idAr)
        print ('********************** \n Nomes (m) ')
        print ('back(b)')
        x=input()
        return x
    def showingMusico():
        x=input()
        return x
    def alterArtist():
        print('''alterar nome - n \n alterar biografia - b 
              \n \n alterar data de nascimento/inicio - id 
              \n alterar local de nascimento/inicio - l \n alterar data de óbito/fim - fd''')
        print('voltar (v)')
        x=input()
        return x
    
    def addArtistToBand():
        print('(*) campo de preenchimento obrigatório')
        papel=input('papel(*): ')
        banda=input('id da banda(*): ')
        artista=input('id músico(*): ')
        dataE=input('data de entrada: ')
        dataS=input('data de saida: ')
        return [papel,dataE,dataS,banda,artista]
    
    def addArtist(): 
            print('(*) campo de preenchimento obrigatório')
            nome=input('nome(*): ')
            biografia=input('biografia: ')
            tipo=input('Artista a solo (s) ou em banda(b)?')
            
            if tipo=='s':
                nasci_data=input('data de nascimento: ')
                nasci_local=input('local de nascimento: ')
                morte_data=input('data de óbito: ')
                
                return [nome, biografia, tipo, nasci_data,nasci_local,morte_data]
            elif tipo=='b':
                inicio_data=input('data de inicio: ')
                inicio_local=input('local de ínicio: ')
                fim_data=input('data de fim: ')
                return [nome, biografia, tipo, inicio_data,inicio_local,fim_data]

    
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

    
#################################################
#Concerto
    def showingConcerto(): 
        print ('********************** \n Ordem de atuação dos Artistas (pa) \n')
        print ('********************** \n Ordem de atuação das Músicas (pm)')
        print ('back(v)')
        x=input()
        return x
    
    def alterConcert():
        print(''' alterar:\ndata - m 
              \n local - l \n tour - t \n''')
        print('voltar (v)')
        x=input()
        return x
    
    def addConcerto(): 
        print('(*) campo de preenchimento obrigatório')
        tour=input('tour(*): ')
        data=input('data(*): ')
        local=input('local(*): ')
        print('artistas(*):')
        oo=input('+ artista (a)')
        artistas=[]
        
        while oo=='a':
            artista=input('id do artista: ')
            c=i.verifyA(artista)

            if c:
                artistas.append(artista)
                
            oo=input('+ artista (a)')

        print('musicas (por ordem)(*):') 
        o=input('+ musica (m)')
        musicas=[]
        
        
        while o=='m':
            musica=input('id da musica: ') 
            c=i.verifyM(musica)

            if c:
                musicas.append(musica)

            o=input('+ musica (m)')

        return [tour, data, local, artistas, musicas]
    
################################################   
#Upload
    def addUpload(user):
        nome=input('nome: ')
        ficheiro_type=input('tipo de ficheiro: ')
        ficheiro=input('ficheiro: ')
        music = True
        while music:
            musica=input('id da música: ')
            c=i.verifyM(musica)
            if c:
                music=False
        partilha=input('Deseja partilhar?  s/n')
        if partilha=='s':
            userShare=input('Introduza o id do user: ')
        else:
            userShare=''
        return [nome, ficheiro_type,ficheiro, musica,userShare]
    
    def selectUpload():
        print('voltar(v)')
        a=input('deseja partilhar este upload com outro utilizador? -s \n deseja fazer um upload? - cn')
        b=input('introduza o id da música: ')
        return a,b

    def chooseUpload(user):
        publica=None
        exists=None

        print('select a upload (s): ')
        up.showUploads(user)
        print ('create new (cn)? ')
        x=input()
        fnlist=input('nome: ')

        if x=='s':
            exists='Yes'

        elif x=='cn':
            publica=input('deseja partilhar? Se sim, user: ')
            exists='No'
        return [choosenlist, exists, publica]

    def addMusic():
        print('(*) campo de preenchimento obrigatório')
        titulo=input('titulo(*): ')
        data=input('data de lançamento(*): ')
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

        print('géneros musicais:')  
        o=input('+ genero (g)')
        generos=[]

        while o=='g':
            genero=input('género: ') 
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

        print('músicas (por ordem):') 
        o=input('+ musica (m)')
        musicas=[]
        while o=='m':
            musica=input('id da musica: ') 
            c=mm.verifyM(musica)

            if c:
                musicas.append(musica)

            o=input('+ musica (m)')

        return [titulo, data, localizacao, artistas, musicas]      
        



   
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

    def askPosicao():
        gen=input('posição: ')
        return gen


