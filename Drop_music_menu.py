import psycopg2
import sys
from Drop_music_interface import interface as i

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
    
    def appbar():
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n logout(x)   search(s)'
              + '\n *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n ')
    def sidebar():
        print('MENU: \n p- as minhas playlists \n u-Uploads \n ******')
##sidebar + listaAlbuns O QUE NAO FAZ MTO SENTIDO
    def mainMenu():
        i.listaAlbum()
        print('MENU: \n p- as minhas playlists \n u-Uploads \n ******')
        ans=input()
        return ans

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


###POR AQUI UM COMMIT THO?????
    def alterAlbum():
        print("""alterar título - t \n alterar data de lançamento - d
        \n alterar editora - ed \n alterar estúdio - as
        \n remover artista - r \n adicionar artista - a""")
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
        print('alterar nome - t \n alterar data de lançamento - d \n alterar letra - l \n alterar duracao - du \n adicionar/remover artista - r \n adicionar/remover genero - a \n adicionar/remover concerto')
        print('voltar (v)')
        x=input()
        return x

    def editorMenu():
        print('Adicionar Album - a')## a acrescentar opcoes
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
            c=i.verifyA(artista)
            if c:
                artistas.append(artista)
            oo=input('+ artista (a)')
        print('musicas (por ordem):') ### SE FIZERMOS ASSIM ATE E MAIS FACIL BOTAR LA SERIAL NA BD
        o=input('+ musica (m)')
        musicas=[]
        while o=='m':
            musica=input('id da musica: ') ##### E SE ELE POE ESTES VALORES MAL?!
            c=i.verifyM(musica)
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
        print("""artistas - a \n concerto - c""")
        x=input()
        return x

    def choosePlaylist(user):
        publica=None
        exists=None
        print('select a playlist (s): ')
        i.showPlaylists(user)
        print ('create new (cn)')
        x=input()
        choosenlist=input('nome: ')
        if x=='s':
            exists='Yes'
        elif x=='cn':
            publica=input('publica (True/False): ')
            exists='No'
        return [choosenlist, exists, publica]
