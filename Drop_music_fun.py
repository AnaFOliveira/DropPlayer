from Drop_music_menu import menu as m
from DropMusic_Album import DropMusic_Album as aa
from DropMusic_Artista import DropMusic_artista as ar
from DropMusic_Musica import DropMusic_Musica as mm
from DropMusic_Concert import DropMusic_Concerto as cc
from DropMusic_User import DropMusic_User as us
from DropMusic_Genero import DropMusic_Genero as ge
from DropMusic_Playlist import DropMusic_Playlist as pl
from DropMusic_Upload import uploads as i



class DropMusic:

    # show album details
    def album(idA, editor, credentials):
        options=['s','x','u','p']
        shown=aa.showDetailsAlbum(idA)
        while shown:
            aa.listArtistsInAlbum(idA) 
            aa.listGenreInAlbum(idA)
            
            wish=m.showingAlbum()
            if wish=='seeAr':
                idAr=m.askId()
                DropMusic.artista(True, idAr, editor, credentials[0])

            if wish=='m': 
                mus=aa.listMusic(idA)
                if mus:
                    posicao=m.getSong()
                    if posicao!='v':
                        idM=aa.getIdA( posicao, idA)
                        if idM is not None:
                            wish=DropMusic.musica(True,idM, editor,credentials[0]) 

            if wish=='sc':
                aa.listComents(idA)
            if wish=='c':
                comment=m.comment()
                aa.addComent(comment, idA, credentials[0])
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
                        dics={'d':'data_lancamento','ed':'editora_discografica','as':'estudio_gravacao','t':'titulo'}  #### QUESTA DE NAO DEIXAR ALTERAR PK!!
                        new=m.setValue()
                        if new!='q':
                            aa.alterValue(dics[op], new,idA)
                    elif op=='rm':
                        posicao=m.getSong() 
                        if posicao=='v':
                            break
                        elif posicao in options:
                            return posicao
                            edit=False
                            break
                        else:
                            idM=aa.deleteMusica( posicao, idA)
                            
                    elif op=='am':
                        idM=m.askId()
                        aa.updateMusicAlbum(idA, idM)
                    elif op=='a':
                        idAr=m.askId()
                        aa.addAlbumArtista(idA[0],idA[1], idAr)
                    elif op=='r':
                        idAr=m.askId()
                        aa.removeAlbumArtista(idA[0],idA[1], idAr)

##                    elif op=='DELETE':
##                        confirm=m.delete()
##                        if confirm=='v':
##                            i.deleteAlbum(idA)

                    if op in options:
                        return op
                        break
            shown=aa.showDetailsAlbum(idA)


    # show music details
    def musica(shown,idM, editor,user):
        options=['s','x','u','p']

        while True:

            shown=mm.showingMusic(idM)
            mm.listgenres(idM)
            choice=m.showmusic()
            if choice=='a':
                mm.listArtistsInMusic(idM)
                print('this is art')#--------------------------
        ##possibilitar chamar artista

            if choice=='c':
                mm.listConcertsInMusic(idM)
                print('this is con') #------------------------------
        ##possibilitar chamar concerto

            if choice=='ap':
                print(user)
                listing=m.choosePlaylist(user)

                if listing[1]=='No':
                    pl.createList(user, listing[0], idM, listing[2]) # user nome idM publica
                elif listing[1]=='Yes':
                    pl.updateList(user, listing[0], idM)



                    
                
            if choice=='v':
                break
            if choice in options:
                print('options')
                return choice
                break
            if editor and choice=='e':
                edit=True

                while edit:

                    op=m.alterMusic()
                    if op=='v':
                        edit=False
                        break
                    if op=='t' or op=='d' or op=='l' or op=='du':
                        dics={'d':'data_lancamento','l':'letra','du':'duracao','t':'titulo'}
                        new=m.setValue()
                        if new!='q':
                            mm.alterMusicValue(dics[op], new,idM)
                            print('i was here')
                    
                    if op=='aa':
                        listing=m.details()
                        aa.updateMusicAlbum(listing, idM)

                    if op=='a':
                        d=m.addRemove()
                        gen=m.askGenero()
                        if d=='d':
                            mm.removeMusicGenre(idM,gen)
                        elif d=='a':
                            mm.addAMusicGenre(idM,gen)
                    elif op=='c':
                        add=m.addRemove()
                        concerto=m.askId()
                        if add=='a':
                            posicao=cc.getPosition(concerto)
                            cc.addConcertMusic(posicao, idM,concerto)
                        elif add=='d':
                            posicao=cc.getPosition(concerto)
                            cc.removeConcertMusic(posicao, idM,concerto)
                    elif op=='r':
                        add=m.addRemove()
                        artista=m.askId()
                        if add=='a':
                            funcao=m.askFuncao()
                            mm.addMusicArtista(idM,funcao,artista)
                        elif add=='d':
                            mm.removeMusicArtista(idM,artista)
        ##### chamar UPLOADS-----------------------------------------

                    if op in options:
                        return op
                        break

    def artista(shown, idAr, editor, user):
        options=['s','x','u','p']
    
        while shown:
            wish = ar.showDetailsArtist(idAr)
            ###possibilitar chamar artista
            banda=ar.getType(idAr) #############3
            if banda:
                choice=m.showingBanda(idAr) 

                if choice=='m':
                    ar.listMembers(idAr)
                    print('members only')
##               
            else:
                choice=m.showingMusico()
                ar.detailMusico(idAr)

            
            
                
            if choice=='v':
                shown=False
                print('leaving menu')
                break
            if choice in options:
                print('options')
                return wish
                break
            if editor and choice=='e':
                edit=True
                while edit:
                    change= m.alterArtist()
                    if change== 'a':
                        papel, dataE, dataS, banda, idAr= m.addArtistToBand()
                        ar.addBandArtista(papel, dataE, dataS,idAr,banda)
                    if change== 'e':
                        op = m.alterArtistDetails()
                        if op == 'v':
                            edit=False
                            break
                        if op=='n' or op=='b' or op=='l' or op=='id' or op=='fd':
                            dics={'n':'nome','b':'biografia','t':'artist_type', 'l':'local', 'id':'inital_date', 'fd':'final_date'}
                            new=m.setValue()
                            ar.alterArtistDetails(dics[op], new,idAr)
                        if op in options:
                            return op
                            break
    # show music details
    def concerto(shown, idC, editor, user):
        options=['s','x','u','p']
        
        while shown:
            wish=cc.showDetailsConcerto(idC)
            ###possibilitar chamar artista
            choice=m.showingConcerto() ##  
            if choice=='pm':
                cc.listMusicsInConcerts(idC)
                ##possibilitar chamar a musicaa
            if choice=='pa':
                cc.listArtistsInConcerts(idC)
            
            if choice=='v':
                shown=False
                print('leaving')
                break
           
            if editor and choice=='e':
                edit=True
                while edit:
                    op=m.alterConcert()
                    if op=='v':
                        edit=False
                        break
                    if  op=='m' or op=='l' or op=='t':
                        dics={'m':'data', 'l':'localizacao', 't':'tour'}
                        new=m.setValue()
                        cc.alterConcertDetails(dics[op], new,idC)
                    elif op=='aa':
                        idAr=m.askId()
                        cc.addConArtista(idC,idAr)
                    elif op=='am':
                        idM=m.askId()
                        cc.addConMusica(idC,idM)
                    elif op=='ra':
                        idAr=m.askId()
                        posicao=m.askPosicao()

                        cc.deleteArtistaC(posicao,idC,idAr)
                    elif op=='rm':
                        idM=m.askId()
                        posicao=m.askPosicao()
                        cc.deleteMusicaC(posicao,idC,idM)

                    if op in options:
                        choice=op
                        return op
                        break
            if choice in options:
                print('options')
                return choice
                break    

    def upload(credentials):
        options=['s','x','u','p']
        shown=True
        while shown:
            print('\n')
            wish=i.showUploadsDetailsPerUser(credentials[0]) #Mostra os uploads do user
            choice=m.showUpload() # Opções dos Uploads
            if choice=='a': #Ver users com quem partilhou
                idM = m.askId()
                i.listUsersShared(credentials[0],idM)
                
            if choice=='b': #Partilhar um upload
                idM = input('Qual a música que pretende partilhar? ')
                username = input('nome do user: ')
                i.shareUpload(credentials[0],idM, username) 
                
            if choice=='c': #Adicionar um upload
                nome, ficheiro_type,ficheiro, musica,userShare = m.addUpload(credentials[0])
                i.addUpload(credentials[0], musica,ficheiro_type,nome,ficheiro)
                if userShare!='':
                    i.shareUpload(credentials[0],musica, userShare)
            
            if choice=='v':
                shown=False
                break
            if choice in options:
                print('options')
                return wish
                break
           

    # show music details

    # shows edit options
    def editor(shown):
        options=['s','x','u','p']
        while shown:
            wish=m.editorMenu()
            if wish=='a':
                info=m.addAlbum()
                aa.addAlbum(info[0],info[1],info[2],info[3])
                for a in range(0,len(info[4])):
                    aa.addAlbumArtista(info[0],info[1],info[4][a])
                for o in range(0,len(info[5])):
                    aa.addAlbumMusica(o+1,info[0],info[1],info[5][o])
            elif wish=='up':
                info=m.selectUser()
                if info=='v':
                    print('operacao cancelada')
                else:
                    us.setAdmin(info)
            elif wish=='m':
                info=m.addMusic()
                idM=mm.addMusic(info[0],info[1],info[2],info[3])
                if idM is not None:
                    for a in range(0,len(info[5])):
                        mm.addMusicArtista(idM,info[4][a],info[5][a])
                    for o in range(0,len(info[6])):
                        mm.addAMusicGenre(idM,info[6][o])
            elif wish=='c':
                info=m.addConcert()
                idC=cc.addConcert(info[0],info[1],info[2])
                if idC is not None:
                    for a in range(0,len(info[3])):
                        cc.addConcertArtista(a+1,idC,info[3][a])
                    for o in range(0,len(info[4])):
                        cc.addConcertMusic(o+1,idC,info[4][o])
            
            elif wish=='ar':
                arType=m.askType()
                info=m.addArtist()
                idAr=ar.addArtist(info[0],info[1])
                if idAr is not None:
                    if arType=='b':
                        band=m.addBand()
                        ar.addBand(band, band[2],idAr)
                        
                        for a in range(0,len(band[3])):
                            ar.addBandArtista(band[4][a], band[5][a], band[6][a], idAr, band[3][a])
                    elif arType=='a':
                        artist=m.addArt()
                        ar.addMusico(artist[0],artist[1],artist[2],idAr)
            elif wish=='g':
                gen=m.askGenero()
                ge.addGenero(gen)
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

            shown=pl.showPlaylistsPerUser(credentials[0])
            wish=m.menuPlaylist()

        ###wish=m.selectPlaylist()
            #devia se verifyP
            if wish=='v':
                shown=False
                break
               
            if wish in options:
                return wish
                break

            elif wish=='c':
                nome,musicas,publica = m.addPlaylist()
                if publica=='pub': 
                    pub =True
                elif publica=='pri':
                    pub = False 
                pl.createList(credentials[0],nome,musicas[0],pub)
                ##posicao=int(pl.getLastPosition(credentials[0],nome)[0])
                for o in range(1,len(musicas)):
                    pl.updateList(credentials[0],nome,musicas[o])
                    
            elif wish=='d':
                wish=m.selectPlaylist()
                user=m.selectUser()
                musicList=True

                while musicList:
                    musicList=pl.getList(user,wish)
                    posicao=m.getSong()

                    if posicao=='v':
                        musicList=False
                        break
                    elif posicao in options:
                        return posicao
                        shown=False
                        break

                    elif user==credentials[0] and posicao=='r':
                        posicao=m.getSong()
                        idM=pl.deleteMusicaP( posicao, wish,user)
                    elif user==credentials[0] and posicao=='a':
                        idM = m.askId()
                        pl.updateList(credentials[0],wish,idM)


                    else:
                        idM=pl.getId( posicao, wish, user)

                        if idM is not None:
                            DropMusic.musica(True,idM, editor,credentials[0]) #####




    
