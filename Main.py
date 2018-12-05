from Drop_music_menu import menu as m
from Drop_music_interface import interface as i
from Drop_music_fun import DropMusic as d

##### UM EDITOR PODER ADICIONAR OUTROS EDITORES!!!! ################################
run=True;


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
                wish=d.album(True, idA, editor)




#escolhas da appbar (validas em qq momento)
            if wish=='s':
                print('search')
            
            # considera-se x como botao de logout
            if wish=='x':
                print('logout')
                break
            
# escolhas sidebar
            if wish=='u':
                ###COMO E QUE SE POE QUI UM BLOB?!
                #m.upload()
                #i.upload()
                print('upload')
           # if editor and wish=='e':
            #    m.editorMenu()


    #resgisto   
    elif selected=='r':
        credentials=m.login()
        check=i.validate(credentials)
        if check:
            i.insert_user(credentials)




