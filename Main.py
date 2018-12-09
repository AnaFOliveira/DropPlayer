from Drop_music_menu import menu as m
from Drop_music_fun import DropMusic as d
from DropMusic_Album import DropMusic_Album as aa
from DropMusic_Artista import DropMusic_artista as ar
from DropMusic_Musica import DropMusic_Musica as mm
from DropMusic_Concert import DropMusic_Concerto as cc
from DropMusic_User import DropMusic_User as us
from DropMusic_Genero import DropMusic_Genero as ge
from DropMusic_Playlist import DropMusic_Playlist as pl
from DropMusic_Search import search as ss
run=True;
options=['s','x','u','p', 'edit']
op=''
while run==True:

    loged=False
    selected=m.inicial()

    #login
    if selected=='l':
        credentials=m.login()
        loged=us.checkPassword(credentials)

        #loged
        while loged:
            editor=us.edits(credentials[0]);
            m.appbar()
            m.sidebar(editor)
            wish=m.mainMenu()

            # user selects an album to consult (POR AQUI REFERENCIA PA RELATORIO A EXPLICAR)
            if wish=='d':
                idA=m.details()
                # details of the album are shown             
                wish=d.album( idA, editor,credentials)                
            elif wish=='sm':
                
                wish=m.mainMenuM()

                if wish=='d':
                    idM=m.askId()
                    # details of the album are shown             
                    wish=d.musica( True, idM, editor,credentials)
                    
            if wish in options:
                op=wish

            while wish in options:
    #escolhas da appbar (validas em qq momento)
                if wish=='s':
                #######while wish=='s':
                        value, atributo = m.searchMusic()
                        if atributo=='1':
                            results = ss.searchMusicByName(value)
                        if atributo=='2':
                            results = ss.searchMusicById(value)
                        if atributo=='3':
                            results = ss.searchMusicByArtistName(value)
                        if atributo=='4':
                            results = ss.searchMusicByArtistId(value)
                        if atributo=='5':
                            results = ss.searchMusicByAlbum(value)
                        if atributo=='6':
                            results = ss.searchMusicByGenero(value)
                        if atributo=='7':
                            results = ss.searchMusicByData(value)
                        if atributo=='8':
                            results = ss.searchMusicByPontuacao(value)
                        if atributo=='9':
                            results = ss.searchMusicByLetra(value)
                        else:
                            wish=atributo
                  
                        
                       
        
                # considera-se x como botao de logout
                elif wish=='x':
                    print('logout')
                    loged=False
                    break
                
        # escolhas sidebar
                elif wish=='u':
                    print('upload')
                    wish=input('oi: ') #------------------------------------------------------------
                elif editor and wish=='edit':
                    wish=d.editor(True)
                elif wish=='p':
                    wish=d.playlists(credentials,editor)
                else:
                    wish=input()


    #resgisto   
    elif selected=='r':
        credentials=m.login()
        check=us.validate(credentials)

        if check:
            us.insert_user(credentials)






