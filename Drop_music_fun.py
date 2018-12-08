from Drop_music_menu import menu as m
#from Drop_music_interface import interface as i
from DropMusic_Album import DropMusic_Album as aa
from DropMusic_Artista import DropMusic_artista as ar
from DropMusic_Musica import DropMusic_Musica as mm
from DropMusic_Concert import DropMusic_Concerto as cc
from DropMusic_User import DropMusic_User as us
from DropMusic_Genero import DropMusic_Genero as ge
from DropMusic_Playlist import DropMusic_Playlist as pl



class DropMusic:

    # show album details
    def album(idA, editor, credentials):
        options=['s','x','u','p']
        shown=True
        while shown:
            shown=aa.showDetails(idA)
            aa.listArtistsInAlbum(idA)
            aa.listGenreInAlbum(idA)
            
        ###possibilitar chamar artista

            wish=m.showingAlbum()
            if wish=='m': 
                mus=aa.listMusic(idA)
                if mus:
                    posicao=m.getSong()
                    if posicao!='v':
                        idM=aa.getIdA( posicao, idA)
                        if idM is not None:
                            DropMusic.musica(True,idM, editor,credentials[0]) #####

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
                        dics={'d':'data_lancamento','ed':'editora_discografica','as':'estudio_gravacao','t':'titulo'}
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
                            


                        
##                    elif op=='DELETE':
##                        confirm=m.delete()
##                        if confirm=='v':
##                            i.deleteAlbum(idA)

                    if op in options:
                        return op
                        break


    # show music details
    def musica(shown,idM, editor,user):
        options=['s','x','u','p']

        while True:

            shown=i.showingMusic(idM)
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
                print('you want to add this to a list') ##------------------------------------
                listing=m.choosePlaylist(user)

                if listing[1]=='No':
                    pl.createList(user, listing[0], idM, listing[2]) # user nome idM publica
                elif listing[1]=='Yes':
                    pl.updateList(user, listing[0], idM)


            if choice=='aa':
                print('you want to add this to an album') ##------------------------------------
                listing=m.details()
                aa.updateMusicAlbum(listing, idM)

                    
                
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
                        mm.alterMusicValue(dics[op], new,idM)

                    if op=='a':
                        d=m.addRemove()
                        gen=m.askGenero()
                        if d=='d':
                            mm.removeMusicGenre(idM,gen)
                        elif d=='a':
                            mm.addAMucicGenre(idM,gen)
                   ### if op==''
#####################FALTA ADICONAR E REMOVER ARTISTAS CONCERTYOS
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
                aa.addAlbum(info[0],info[1],info[2],info[3])
                for a in range(0,len(info[4])):
                    aa.addAlbumArtista(info[0],info[1],info[4][a])
                for o in range(0,len(info[5])):
                    aa.addAlbumMusica(o,info[0],info[1],info[5][o])
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
                        mm.addAMucicGenre(idM,info[6][o])
            elif wish=='c':
                info=m.addConcert()
                idC=cc.addConcert(info[0],info[1],info[2])
                if idC is not None:
                    for a in range(0,len(info[3])):
                        cc.addConcertArtista(a,idC,info[3][a])
                    for o in range(0,len(info[4])):
                        cc.addConcertMusic(o,idC,info[4][o])
            
            elif wish=='ar':
                arType=m.askType()
                info=m.addArtist()
                idAr=ar.addArtist(info[0],info[1])
                if idAr is not None:
                    if arType=='b':
                        band=m.addBand()
                        ar.addBand(info[0],info[1],band, idAr)
                        for a in range(0,len(band[3])):
                            ar.addBandArtista(band[4][a], band[5][a], band[6][a], idAr, band[3][a])
                    elif arType=='a':
                        artist=m.addArt()
                        ar.addMusico(info[0], info[1],artist[0],artist[1],artist[2], idAr)
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
                        idM=pl.deleteMusica( posicao, wish,user)




                    else:
                        idM=pl.getId( posicao, wish, user)

                        if idM is not None:
                            DropMusic.musica(True,idM, editor,credentials[0]) #####




    
