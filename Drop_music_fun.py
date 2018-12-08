from Drop_music_menu import menu as m
from Drop_music_interface import interface as i

class DropMusic:

    # ecra que mostra os detalhes de um album
    def album(idA, editor, credentials):
        
        options=['s','x','u','p']
        shown=True

        while shown:
            shown=i.showDetails(idA)
            i.listArtistsInAlbum(idA)  ###falta tb o album em si xp
            ###possibilitar chamar artista
            wish=m.showingAlbum() ##    E PRECISO MOSTRAR OS GENEROS!!!!!
            if wish=='m':
                i.listMusic(idA)
                ##possibilitar chamar a musicaa
            if wish=='sc':
                i.listComents(idA)
                ##ver comentários
            if wish=='c':
                comment=m.comment()
                i.addComent(comment, idA, credentials[0])
                ## adicionar comentários
            if wish=='v':
                shown=False
                break
            
            if wish in options:
                return wish
                break
            
            if editor and wish=='e': #editar album
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
                    if op in options:
                        return op
                        break
    # show music details
    def musica(shown,idM, editor, user):
        options=['s','x','u','p']
        
        while shown:
            wish=i.showingMusic(idM) ##    E PRECISO MOSTRAR OS GENEROS!!!!!
            i.listgenres(idM)
            choice=m.showMusic()
            if choice=='a':
                i.listArtistsInMusic(idM) #mostrar artista nA música
                print('this is art')#
                ##possibilitar chamar a musicaa
            if choice=='c':
                i.listConcertsInMusic(idM)
                print('this is con') 
                
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
            if editor and wish=='e':
                edit=True
                
                while edit:
                    op=m.alterMudic()
                    if op=='v':
                        edit=False
                        break
                    if op=='t' or op=='d' or op=='l' or op=='du':
                        dics={'d':'data_lancamento','l':'letra','du':'duracao','t':'titulo'}
                        new=m.setValue()
                        i.alterMusicValue(dics[op], new, idM)
                   ### if op==''
#####################FALTA ADICONAR E REMOVER ARTISTAS GENEROS E CONCERTYOS
                        #####UPLOADS E PLAYLISTS!!!!!
                    if op in options:
                        return op
                        break

    
    
    def artista(shown, idAr, editor, user):
        options=['s','x','u','p']
    
        while shown:
            wish = i.showArtist(idAr)
            ###possibilitar chamar artista
            choice=m.showingArtist() ##   
            if choice=='m':
                i.listMembers(idAr)
                print('members only')
            if choice=='b':
                i.showBiography(idAr)
            if choice=='l': #trocar sc? ver local de começo
                i.showLocal(idAr)
                print('locals')
            if choice=='i': #trocar c? ver data inicio/nascimento
                i.showInitalDate(idAr)
                print('initial date')
            if choice=='f': #trocar d? ver data fim/morte
                i.showFinalDate(idAr)
                print('final')
            #if choice=='id':
                
            if choice=='b':
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
                        i.addBandArtista(papel, dataE, dataS,idAr,banda)
                    if change== 'e':
                        op = m.alterArtistDetails()
                        if op == 'v':
                            edit=False
                            break
                        if op=='n' or op=='b' or op=='t' or op=='l' or op=='id' or op=='fd':
                            dics={'n':'nome','b':'biografia','t':'artist_type', 'l':'local', 'id':'inital_date', 'fd':'final_date'}
                            new=m.setValue()
                            i.alterArtistDetails(dics[op], new,idAr)
                        if op in options:
                            return op
                            break
    # show music details
    def concerto(shown, idC, editor, user):
        options=['s','x','u','p']
        
        while shown:
            wish=i.showingConcert(idC)
            i.listArtistsInConcert(idC)  ###falta tb o album em si xp
            ###possibilitar chamar artista
            choice=m.showConcert() ##  
            if choice=='m':
                i.listMusicsInConcert(idC)
                ##possibilitar chamar a musicaa
            if choice=='a':
                i.listArtistsInConcert()
            if choice=='pa': #trocar sc? ver posição artistas
                i.listArtPos(idC)
            if choice=='pm': #trocar c? ver posicao musicas
                i.listMusPos(idC)
            if choice=='b':
                shown=False
                print('leaving')
                break
            if choice in options:
                print('options')
                return wish
                break
            if editor and wish=='e':
                edit=True
                while edit:
                    op=m.alterConcert()
                    if op=='v':
                        edit=False
                        break
                    if op=='a' or op=='m' or op=='pa' or op=='pm' or op=='l' or op=='t':
                        dics={'a':'artistas','m':'musicas','pa':'posicao_artistas','pm':'posicao_musicas', 'l':'local', 't':'tour'}
                        new=m.setValue()
                        i.alterConcertDetails(dics[op], new,idC)
                    if op in options:
                        return op
                        break
    # show music details
    
    def upload(shown, editor, user, idM):
        options=['s','x','u','p']
        
        while shown:
            wish=i.showingUploads(user,idM)
            i.listUploads(user)  ###falta tb o album em si xp
            ###possibilitar chamar artista
            choice=m.showUpload(user, idM) ##  
            if choice=='u':
                i.listUsersShared(user,idM)
                ##possibilitar chamar a musicaa
            if choice=='s':
                print('do you wish to share this upload with another user? ')
                listing=m.chooseUser()
                if listing[1]=='No':
                    i.createList(user, listing[0], idM, listing[2]) ## alterar para?
                elif listing[1]=='Yes':
                    i.updateList(user, listing[0], idM)## alterar para?
                i.partilharUpload() ####Sim?
            if choice=='p':
                print('you want to add this to a playlist') ##------------------------------------
                listing=m.choosePlaylist(user)

                if listing[1]=='No':
                    i.createList(user, listing[0], idM, listing[2]) # user nome idM publica
                elif listing[1]=='Yes':
                    i.updateList(user, listing[0], idM)
            
            if choice=='b':
                shown=False
                print('leaving')
                break
            if choice in options:
                print('options')
                return wish
                break
            if editor and wish=='e':
                edit=True
                while edit:
                    op=m.alterConcert()
                    if op=='v':
                        edit=False
                        break
                    if op=='a' or op=='m' or op=='pa' or op=='pm' or op=='l' or op=='t':
                        dics={'a':'artistas','m':'musicas','pa':'posicao_artistas','pm':'posicao_musicas', 'l':'local', 't':'tour'}
                        new=m.setValue()
                        i.alterValue(dics[op], new, user, idM)
                    if op in options:
                        return op
                        break
    # show music details
    
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
            elif wish== 'c':
                 info=m.addConcert()
                 idC=i.addConcert(info[0],info[1],info[2])
                 if idM is not None:
                     for a in range(0,len(info[3])):
                        i.addConcertArtista(a,idC,info[3][a])
                     for o in range(0,len(info[4])):
                        i.addConcertMucic(o,idC,info[4][o])
            
            elif wish== 'ar':
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