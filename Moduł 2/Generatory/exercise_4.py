def sing():
    song = '''Wlazł kotek na płotek i mruga, ładna to piosenka, nie długa. Nie długa, nie krótka, lecz w sam raz,  zaśpiewaj koteczku, jeszcze raz.'''
    song_words = song.split()
    line_1 = song_words[0:4]
    line_2 = song_words[4:6]
    line_3 = song_words[6:9]
    line_4 = song_words[9:11]
    line_5 = song_words[11:15]
    line_6 = song_words[15:19]
    line_7 = song_words[19:21]
    line_8 = song_words[21:23]
    
    lines_list = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8]

    for line in lines_list:
        yield ' '.join(line)

a = sing()

for i in a:
    print(i)

#song = '''Wlazł kotek na płotek i mruga, ładna to piosenka, nie długa. Nie długa, nie krótka, lecz w sam raz,  zaśpiewaj koteczku, jeszcze raz.'''
#song_words = song.split()
#print(song_words)

