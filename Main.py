from Drop_music_menu import menu as m
from Drop_music_fun import DropMusic as d
from DropMusic_User import DropMusic_User as us
from DropMusic_Search import search as ss

run=True;
options=['s','x','u','p', 'edit']
op=''
while run==True:

    logged=False
    selected=m.inicial()

    #login
    if selected=='l':
        credentials=m.login()
        logged=us.checkPassword(credentials)

        #logged
        while logged:
            editor=us.edits(credentials[0]);
            m.appbar()
            m.sidebar(editor)
            wish=m.mainMenu()

            # user selects an album to consult 
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
            elif wish=='sc':
                wish=m.mainMenuC()

                if wish=='d':
                    idC=m.askId()
                    # details of the album are shown             
                    wish=d.concerto( True, idC, editor,credentials)

            if wish in options:
                op=wish

            while wish in options:
    #escolhas da appbar (validas em qq momento)
                if wish=='s':
                        atributo, value = m.searchMusic()
                        if atributo=='1':
                            results = ss.searchMusicByName(value)
                        elif atributo=='2':
                            results = ss.searchMusicById(value)
                        elif atributo=='3':
                            results = ss.searchMusicByArtistName(value)
                        elif atributo=='4':
                            results = ss.searchMusicByArtistId(value)
                        elif atributo=='5':
                            results = ss.searchMusicByAlbum(value)
                        elif atributo=='6':
                            results = ss.searchMusicByGenero(value)
                        elif atributo=='7':
                            results = ss.searchMusicByData(value)
                        elif atributo=='8':
                            results = ss.searchMusicByPontuacao(value)
                        elif atributo=='9':
                            results = ss.searchMusicByLetra(value)
                        else:
                            wish=atributo       
        
                # considera-se x como botao de logout
                elif wish=='x':
                    print('logout')
                    logged=False
                    break
                
        # escolhas sidebar
                elif wish=='u':
                    wish=d.upload(True, editor, credentials[0])    ###################dEFINIR IDM?????
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
    elif selected=='x':
        run=False