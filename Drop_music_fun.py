from Drop_music_menu import menu as m
from Drop_music_interface import interface as i
class DropMusic:

    # ecra que mostra os detalhes de um album
    def album(shown, idA, editor):
        options=['s','x','u','p']

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
                        i.alterValue(dics[op], new,idA)
                    if op in options:
                        return op
                        break
    # show music details
    def musica(shown,idM, editor):
        options=['s','x','u','p']
        while shown:
            wish=m.showingMusic() ##    E PRECISO MOSTRAR OS GENEROS!!!!!
            i.listgenres(idM)      
            if wish=='a':
                i.listArtistsInMusic(idM)
                ##possibilitar chamar a musicaa
            if wish=='c':
                i.listConcertsInMusic(idM)
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
    ##                    if op=='v':
    ##                        edit=False
    ##                        break
    ##                    if op=='t' or op=='d' or op=='ed' or op=='as':
    ##                        dics={'d':'data_lancamento','ed':'editora_discografica','as':'estudio_gravacao','t':'titulo'}
    ##                        new=m.setValue()
    ##                        i.alterValue(dics[op], new,idA)
    ##                    if op in options:
    ##                        return op
    ##                        break




        
