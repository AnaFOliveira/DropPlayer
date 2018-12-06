from Drop_music_menu import menu as m
from Drop_music_interface import interface as i
class DropMusic:

    # ecra que mostra os detalhes de um album
    def album(idA, editor):
        options=['s','x','u','p']
        shown=i.showDetails(idA)
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
            if wish=='b':
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
                    if op in options:
                        return op
                        break


    # show music details
    def musica(shown,idM, editor):
        options=['s','x','u','p']
        while shown:
            wish=m.showingMusic()
            i.listgenres(idM)      
            if wish=='a':
                i.listArtistsInMusic(idM)
                ##possibilitar chamar artista
            if wish=='c':
                i.listConcertsInMusic(idM)
                ##possibilitar chamar concerto
            if wish=='b':
                shown=False
                break
            if wish in options:
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
                        i.alterMusicValue(dics[op], new,idM)
                   ### if op==''
#####################FALTA ADICONAR E REMOVER ARTISTAS GENEROS E CONCERTYOS
                        #####UPLOADS E PLAYLISTS!!!!!
                    if op in options:
                        return op
                        break


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
            if wish in options:
                return wish
                break
