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
    
    def search_menu():
         print('o que deseja procurar? ')
         print('''Artista - ar \n Album - a 
              \n Concerto - c \n Música - m \n Upload - u 
              \n Playlist - p \n Outros user- us \n ''')
         choice= input()
         return choice
    

###########################################   
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
##########################################  ALBUM

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
        
    
            
################################################### 
#Music
    def alterMusic():
        print('alterar nome - t \n alterar data de lançamento - d \n alterar letra - l \n alterar duracao - du \n adicionar/remover artista - r \n adicionar/remover genero - a \n adicionar/remover concerto')
        print('voltar (v)')
        x=input()
        return x
    
    def searchMusic():
        print('Pesquisa por: \n 1) nome \n 2) id \n 3) Nome do Artista')
        print('\n 4) Id do Artista \n 5) Album \n 6) Genero \n 7) Data \n')
        print('8) Pontuação \n 9) Letra')
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
    

##################################################
#Artista    
    def showingArtista(): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print ('********************** \n Nomes (m) ')
        print ('********************** \n Biografia (b) \n')
        print ('********************** \n Local de nascimento/início (l) \n')
        print ('********************** \n Data de nascimento/início (i) \n')
        print ('********************** \n Data de óbito/fim (f) \n')
        #print ('********************** \n Id (id) \n')
        print ('back(b)')
        x=input()
        return x
    
    def alterArtist(): ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! alterar tipo não deveria ser opção, right? Se não mexe com as bases de dados todas
        print('''alterar nome - n \n alterar biografia - b 
              \n alterar tipo - t \n alterar data de nascimento/inicio - id 
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
    
    def addArtist(): ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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


#################################################
#Concerto
    def showingConcerto(): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print ('********************** \n Músicas (m) ')
        print ('********************** \n Artistas (a) \n')
        print ('********************** \n Ordem de atuação dos Artistas (pa) \n')
        print ('********************** \n Ordem de atuação das Músicas (pm))
        print ('back(b)')
        x=input()
        return x
    
    def alterConcerto(): ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! alterar tipo não deveria ser opção, right? Se não mexe com as bases de dados todas
        print('''alterar artistas - a \n alterar musicas - m 
              \n alterar ordem de atuaçao dos artistas - pa \n alterar ordem de atuaçao das músicas - pm 
              \n local - l \n tour - t''')
        print('voltar (v)')
        x=input()
        return x
    
    def addConcerto(): ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print('(*) campo de preenchimento obrigatório')
        tour=input('tour(*): ')
        local=input('local(*): ')
        print('artistas(*):')
        oo=input('+ artista (a)')
        artistas=[]
        
        ########!!!!!!!!!!!!!! falta a posição de atuacao dos artistas
        while oo=='a':
            artista=input('id do artista: ')
            c=i.verifyA(artista)

            if c:
                artistas.append(artista)
                
            oo=input('+ artista (a)')

        print('musicas (por ordem)(*):') ### SE FIZERMOS ASSIM ATE E MAIS FACIL BOTAR LA SERIAL NA BD
        o=input('+ musica (m)')
        musicas=[]
        
        
        ########!!!!!!!!!!!!!! falta a posição de atuacao das musicas
        while o=='m':
            musica=input('id da musica: ') ##### E SE ELE POE ESTES VALORES MAL?!
            c=i.verifyM(musica)

            if c:
                musicas.append(musica)

            o=input('+ musica (m)')

        return [titulo, data, estudio, editora, artistas, musicas]
    
################################################   
#Upload
    def addUpload(user): ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #print('(*) campo de preenchimento obrigatório')
        nome=input('nome: ')
        ficheiro_type=input('tipo de ficheiro: ')
        #ficheiro=input('ficheiro(*):')
        
        #o=input('+ musica (m)')
        #musicas=[]
        ########!!!!!!!!!!!!!! falta a posição de atuacao das musicas
        #while o=='m':
        #    musica=input('id da musica: ') ##### E SE ELE POE ESTES VALORES MAL?!
        #    c=i.verifyM(musica)

        #    if c:
        #        musicas.append(musica)

        #    o=input('+ musica (m)')

        return [nome, ficheiro_type]
            
########################################## EDITOR    
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
        
        print('artistas:') ####################!!!!!!!!!!!!!!! Não deveria ser obrigatório também???
        oo=input('+ artista (a)')
        artistas=[]

        while oo=='a':
            artista=input('id do artista: ')
            c=i.verifyA(artista)

            if c:
                artistas.append(artista)
                
            oo=input('+ artista (a)')
 
        ########!!!!!!!!!!!!!! não falta a posição de atuacao dos musicas??
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


    
