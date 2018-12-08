from Drop_music_menu import menu as m
from Drop_music_interface import interface as i

class DropMusic:

    # show album details
    def album(idA, editor, credentials):
        options=['s','x','u','p']
        shown=True
        while shown:
            shown=i.showDetails(idA)
            i.listArtistsInAlbum(idA)  
        ###possibilitar chamar artista
            wish=m.showingAlbum() ##    E PRECISO MOSTRAR OS GENEROS!!!!!
            if wish=='m': 
                i.listMusic(idA)                    
        ##possibilitar chamar a musicaa
            if wish=='sc':
                i.listComents(idA)
            if wish=='c':
                comment=m.comment()
                i.addComent(comment, idA, credentials[0])
            if wish=='v':
                shown=False
                break
            if wish in options:
                return wish
                break
            if editor and wish=='e':
                edit=True
                while edit:
                    op=m.alterAlbum()
                    if op=='v':
                        edit=False
                        break
                    if op=='t' or op=='d' or op=='ed' or op=='as':
                        dics={'d':'data_lancamento','ed':'editora_discografica','as':'estudio_gravacao','t':'titulo'}
                        new=m.setValue()
                        if new!='q':
                            i.alterValue(dics[op], new,idA)
                    #elif op=
                    if op in options:
                        return op
                        break


    # show music details
    def musica(shown,idM, editor,user):
        options=['s','x','u','p']

        while True:

            shown=i.showingMusic(idM)
            i.listgenres(idM)
            choice=m.showmusic()
            if choice=='a':
                i.listArtistsInMusic(idM)
                print('this is art')#--------------------------
        ##possibilitar chamar artista

            if choice=='c':
                i.listConcertsInMusic(idM)
                print('this is con') #------------------------------
        ##possibilitar chamar concerto

            if choice=='ap':
                print('you want to add this to a list') ##------------------------------------
                listing=m.choosePlaylist(user)

                if listing[1]=='No':
                    i.createList(user, listing[0], idM, listing[2]) # user nome idM publica
                elif listing[1]=='Yes':
                    i.updateList(user, listing[0], idM)
                
            if choice=='v':
                print('this is leaving')
                break
            if choice in options:
                print('options')
                return wish
                break
            if editor and choice=='e':
                edit=True

                while edit:

                    op=m.alterMudic()
                    if op=='v':
                        edit=False
                        break
                    if op=='t' or op=='d' or op=='l' or op=='du':
                        dics={'d':'data_lancamento','l':'letra','du':'duracao','t':'titulo'}
                        new=m.setValue()
                        i.alterMusicValue(dics[op], new,idM)
                   ### if op==''
#####################FALTA ADICONAR E REMOVER ARTISTAS GENEROS E CONCERTYOS
                        #####UPLOADS
                    if op in options:
                        return op
                        break



    # shows edit options
    def editor(shown):
        options=['s','x','u','p']
        while shown:
            wish=m.editorMenu()
            if wish=='a':
                info=m.addAlbum()
                i.addAlbum(info[0],info[1],info[2],info[3])
                for a in range(0,len(info[4])):
                    i.addAlbumArtista(info[0],info[1],info[4][a])
                for o in range(0,len(info[5])):
                    i.addAlbumMusica(o,info[0],info[1],info[5][o])
            elif wish=='up':
                info=m.selectUser()
                if info=='v':
                    print('operacao cancelada')
                else:
                    i.setAdmin(info)
            elif wish=='m':
                info=m.addMusic()
                idM=i.addMusic(info[0],info[1],info[2],info[3])
                if idM is not None:
                    for a in range(0,len(info[5])):
                        i.addMusicArtista(idM,info[4][a],info[5][a])
                    for o in range(0,len(info[6])):
                        i.addAMucicGenre(idM,info[6][o])
            elif wish= 'c':
                info=m.addConcert()
                idC=i.addConcert(info[0],info[1],info[2])
                if idM is not None:
                    for a in range(0,len(info[3])):
                        i.addConcertArtista(a,idC,info[3][a])
                    for o in range(0,len(info[4])):
                        i.addConcertMucic(o,idC,info[4][o])
            
             elif wish= 'ar':
                arType=m.askType()
                info=m.addArtist()
                idAr=i.addArtist(info[0],info[1])
                if idAr is not None:
                    if arType=='b':
                        band=m.addBand()
                        i.addBand(band, idAr)
                        for a in range(0,len(band[3])):
                            i.addBandArtista(band[4][a], band[5][a], band[6][a], idAr, band[3][a])
                    elif arType=='a':
                        artist=m.addArt()
                        i.addMusico(artist, idAr)
                
            if wish=='v':
                shown=False
                break
            if wish in options:
                return wish
                break



    # shows all playlists
    def playlists(credentials,editor):
        options=['s','x','u','p']
        shown=True

        while shown:

            shown=i.showPlaylistsPerUser(credentials[0])
            wish=m.selectPlaylist()
            if wish=='v':
                shown=False
                break
               
            if wish in options:
                return wish
                break
                
            
            else:
                user=m.selectUser() # pode dar merda com input '' mas na interface era impossivel
                musicList=True

                while musicList:
                    musicList=i.getList(user,wish)
                    posicao=m.getSong()

                    if posicao=='v':
                        musicList=False
                        break
                    elif posicao in options:
                        return posicao
                        shown=False
                        break
                    else:
                        idM=i.getId( posicao, wish, user)

                        if idM is not None:
                            DropMusic.musica(True,idM, editor,credentials[0]) #####




    
