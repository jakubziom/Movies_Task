import random
from datetime import date
today = date.today()

#szablon do wyświetlania informacji o filmie

class Movie:
    def __init__(self,title,year,genre,numberOfPlays):
        self.title = title
        self.year = year
        self.genre = genre
        self.numberOfPlays = int(numberOfPlays)

    def __str__(self):
        return f'"{self.title}" ({self.year})'
        
    def play(self):
        self.numberOfPlays + 1
        return
    
    def showNumberOfPlays(self):
        return str(self.numberOfPlays)
    
#szablon do wyświetlania informacji o serialu

class Series(Movie):
    def __init__(self, numberOfEpisode, numberOfSeason, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numberOfEpisode = numberOfEpisode
        self.numberOfSeason = numberOfSeason

    def __str__(self):
        return f'"{self.title}" S{self.numberOfSeason} E{self.numberOfEpisode}'

    def play(self):
        self.numberOfPlays + 1
        return
    
    def showNumberOfPlays(self):
        return str(self.numberOfPlays)
    
#lista filmów i seriali | lp. 1 |[0]-filmy [1]-seriale | lp.2 |[n] = numer tytułu z danymi | lp.3 | [0] - Tytuł [1] - Rok [2] - Gatunek, (dla seriali: [3] - Nr epizodu [4] - Nr odcinka)
#np. wyciąganie tytułu filmu titles_list[0][2][0]
#np. wyciąganie tytułu serialu tiles_list[1][2][0]
    
titles_list=[[['Pulp Fiction',1994,'Action'],['Lost In Translation',2003,'Romance'],['Alien',1979,'Horror'],['Contact',1997,'Sci-fi'],['The Godfather',1972,'Drama']],
             [['Dr House',2004,'Drama','01','02'],['Breaking Bad',2008,'Drama','02','03'],['Squid Game',2021,'Thriller','02','01'],['Stranger Things',2016,'Horror','03','02'],['Battlestar Galactica',2004,'Sci-fi','03','01']]]    

get_movies_list=[]
get_series_list=[]
views_movies={}
views_series={}

#wyszukiwanie po tytule

def search():
    keyword = str(input('Proszę podać tytuł'))
    for i in range(0,len(titles_list[0])):
        if keyword == titles_list[0][i][0]:
            print('znalazłem film ' + str(Movie(title=(titles_list[0][i][0]),
                                                year=(titles_list[0][i][1]),
                                                genre=(titles_list[0][i][2]),
                                                numberOfPlays=0)))
    for i in range(0,len(titles_list[1])):
        if keyword == titles_list[1][i][0]:
            print('znalazłem serial ' + str(Series(title=(titles_list[1][i][0]),
                                                   year=(titles_list[1][i][1]),
                                                   genre=(titles_list[1][i][2]),
                                                   numberOfPlays=0,
                                                   numberOfEpisode=(titles_list[1][i][3]),
                                                   numberOfSeason=(titles_list[1][i][4])))) 
    return

#to zrobiłem dodatkowo:
#wyświetla 1 losowy tytuł i generuje mu losową liczbę wyświetleń

def random_views():
    movie_or_series=random.randint(0,1)
    if movie_or_series==0:
        r=random.randint(0,len(titles_list[0])-1)
        Random_title=Movie(title=(titles_list[0][r][0]),
                           year=(titles_list[0][r][1]),
                           genre=(titles_list[0][r][2]),
                           numberOfPlays=random.randint(0,100))
        print("LOSOWY FILM I WYŚWIETLENIA")
        print(str(Random_title) + ' liczba wyświetleń: ' + str(Random_title.showNumberOfPlays())) 
    if movie_or_series==1:
        r=random.randint(0,len(titles_list[1])-1)
        Random_title=Series(title=(titles_list[1][r][0]),
                            year=(titles_list[1][r][1]),
                            genre=(titles_list[1][r][2]),
                            numberOfPlays=random.randint(0,100),
                            numberOfEpisode=(titles_list[1][r][3]),
                            numberOfSeason=(titles_list[1][r][4]))
        print("LOSOWY SERIAL I WYŚWIETLENIA")
        print(str(Random_title) + ' liczba wyświetleń: ' + str(Random_title.showNumberOfPlays())) 
  
#tworzy nową listę z filmami / serialami ułożoną alfabetycznie

def get_movies():
    for i in range(0,len(titles_list[0])):
        get_movies_list.append((titles_list[0][i]))
    get_movies_list.sort()
    #print(get_movies_list)
    return

def get_series():
    for i in range(0,len(titles_list[1])):
        get_series_list.append((titles_list[1][i]))
    get_series_list.sort()
    #print(get_series_list)
    return

#szuka w jakim miejscu znajduje się tytuł na bazowej liście

def find_title_index(type,title):
    for i in range(len(titles_list[type])):
        for n in range(len(titles_list[type][i])):
            if titles_list[type][i][n] == title:
                return i

#tworzy bibliotekę filmów i seriali (słownik) z losowymi ilościami wyświetleń

def generate_views():

    for n in range(0,len(get_movies_list)): 
        views_movies[get_movies_list[n][0]]=random.randint(0,100)
        views_series[get_series_list[n][0]]=random.randint(0,100)
    
    print('')
    print('Generuję losową ilość wyświetleń dla wszystkich filmów i seriali...')
    print('-----------')
    print('Filmy:')
    print(views_movies)
    print('Seriale:')
    print(views_series)
    print('-----------')   
    #wyświetla najpopularniejszy film i serial wg dzisiejszej daty:  
    print("Najpopularniejszym filmem dnia " + str(today) + " był: " + str(Movie(title=(str(max(views_movies, key=views_movies.get))),
                                                                                #wyciąga rok z bazowej listy wg tytułu ze słownika
                                                                                year=titles_list[0][find_title_index(0,(str(max(views_movies, key=views_movies.get))))][1],
                                                                                #wyciąga gatunek z bazowej listy wg tytułu ze słownika
                                                                                genre=titles_list[0][find_title_index(0,(str(max(views_movies, key=views_movies.get))))][2],
                                                                                numberOfPlays=str(max(views_movies.values()))))
                                                                                 + " z ilością wyświetleń: " + str(max(views_movies.values())))
    print("Najpopularniejszym serialem dnia " + str(today) + " był: " + str(Series(title=(str(max(views_series, key=views_series.get))),
                                                                                #wyciąga rok z bazowej listy wg tytułu ze słownika
                                                                                year=titles_list[1][find_title_index(1,(str(max(views_series, key=views_series.get))))][1],
                                                                                #wyciąga gatunek z bazowej listy wg tytułu ze słownika
                                                                                genre=titles_list[1][find_title_index(1,(str(max(views_series, key=views_series.get))))][2],
                                                                                numberOfPlays=str(max(views_series.values())),
                                                                                #wyciąga number epizodu i sezonu z bazowej listy wg tytułu ze słownika
                                                                                numberOfEpisode=titles_list[1][find_title_index(1,(str(max(views_series, key=views_series.get))))][3],
                                                                                numberOfSeason=titles_list[1][find_title_index(1,(str(max(views_series, key=views_series.get))))][4]))
                                                                                  + " z ilością wyświetleń: " + str(max(views_series.values())))
    print('-----------')
    #łączy 2 słowniki w jeden zawierający wszystkie tytuły i wyświetlenia
    views={**views_movies,**views_series}
    print("Wszystkie tytuły i wyświetlenia:")
    print(views)
    print("Sortuję wg wyświetleń:")
    #sortuje elementy w słowniku wg ilości wyświetleń
    sorted_views = sorted(views.items(), key=lambda x:x[1])
    print("Top 3 Najbardziej oglądanych tytułów to:")
    top3=sorted_views[-3:]
    print(top3)

    print('===========')

print('=================')
print('Biblioteka Filmów')
print('=================')

#wprowadzanie informacji przez użytkownika

while True:
    try:
        selection=int(input('Co chcesz zrobić? 1-Wyszukiwanie Tytułów, 2-Losowy Tytuł i wyświetlenia, 3-Najpopularniejsze Filmy i Seriale dzisiaj, TOP 3'))
    except:
        print('Proszę podać cyfrę')
        continue
    if selection==1:
        search()
    if selection==2:
        random_views()
    if selection==3:
        get_movies()
        get_series()
        generate_views()