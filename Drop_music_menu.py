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






    
