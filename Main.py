from Drop_music_menu import menu as m
from Drop_music_interface import interface as i
from Drop_music_fun import DropMusic as d


run=True;
options=['s','x','u','p']

while run==True:

    loged=False
    selected=m.inicial()

    #login
    if selected=='l':
        credentials=m.login()
        loged=i.checkPassword(credentials)

        #loged
        while loged:
            editor=i.edits(credentials[0]);
            m.appbar()
            m.sidebar()
            wish=m.mainMenu()

            # user selects an album to consult (POR AQUI REFERENCIA PA RELATORIO A EXPLICAR)
            if wish=='d':
                idA=m.details()
                # details of the album are shown             
                wish=d.album( idA, editor,credentials)


##devo precisar aqui de um while wish in options
            #while wish in options: 
    #escolhas da appbar (validas em qq momento)
            if wish=='s':
                while wish=='s':
                    parameter = m.search_menu()
                    if parameter = 'ar':
                        
                        
                    if parameter = 'a':
                        value, atributo=m.searchAlbum()
                        if atributo== '1':
                            results = i.searchAlbumByTitle(value)
                        if atributo== '2':
                            results = i.searchAlbumByYear(value)
                        
                    if parameter = 'c':
                    if parameter = 'm':
                    if parameter = 'u':
                    if parameter = 'p':
                    if parameter = 'us':

                        
                    
                   
            
            # considera-se x como botao de logout
            if wish=='x':
                print('logout')
                break
            
    # escolhas sidebar
            if wish=='u':
                print('upload')

            if editor and wish=='edit':
                d.editor(True)

            if wish=='p':
                wish=d.playlists(credentials,editor)


    #resgisto   
    elif selected=='r':
        credentials=m.login()
        check=i.validate(credentials)

        if check:
            i.insert_user(credentials)