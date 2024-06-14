import random
from datetime import date
today = date.today()

#szablon filmu
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
    
#szablon serialu
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
    
#'surowa' lista filmów i seriali | lp. 1 |[0]-filmy [1]-seriale | lp.2 |[n] = numer tytułu z danymi | lp.3 | [0] - Tytuł [1] - Rok [2] - Gatunek, (dla seriali: [3] - Nr epizodu [4] - Nr odcinka)
#np. wyciąganie tytułu filmu titles_list[0][2][0]
#np. wyciąganie tytułu serialu tiles_list[1][2][0]
    
titles_list=[[['Pulp Fiction',1994,'Action'],['Lost In Translation',2003,'Romance'],['Alien',1979,'Horror'],['Contact',1997,'Sci-fi'],['The Godfather',1972,'Drama']],
             [['Dr House',2004,'Drama','01','02'],['Breaking Bad',2008,'Drama','02','03'],['Squid Game',2021,'Thriller','02','01'],['Stranger Things',2016,'Horror','03','02'],['Battlestar Galactica',2004,'Sci-fi','03','01']]]

movies_list=[]
series_list=[]

#Wypełniam bibliotekę filmami (tworzę instancje na listach):

for i in range(len(titles_list[0])):
    movies_list.append(Movie(title=(titles_list[0][i][0]),
                            year=(titles_list[0][i][1]),
                            genre=(titles_list[0][i][2]),
                            numberOfPlays=0))
    
for i in range(len(titles_list[1])):
    series_list.append(Series(title=(titles_list[1][i][0]),
                            year=(titles_list[1][i][1]),
                            genre=(titles_list[1][i][2]),
                            numberOfPlays=0,
                            numberOfEpisode=(titles_list[1][i][4]),
                            numberOfSeason=(titles_list[1][i][3])))
    
#print(movies_list)
#print(series_list)

#titles_list2 - lista ze wszystkimi instancjami filmów i seriali
titles_list2=movies_list+series_list 

get_movies_list=[]
get_series_list=[]

#search_list - lista tylko do podpowiedzi wyszukiwania (inna niż sortowana alfabetycznie)
search_list=movies_list+series_list

    #wyszukiwanie filmów/seriali
def search():
    print("==Podpowiedź: Tytuły w bibliotece:==")
    for i in range(0,len(search_list)):
        print(search_list[i])
    print('================================')
    #słowo do wyszukiwania
    keyword = str(input('Proszę podać tytuł'))
    for i in range(0,len(movies_list)):
        #szuka po atrybucie "title"
        if keyword == getattr(movies_list[i],'title'):
            #wyświetla "znalazłem tytuł"
            print('znalazłem film ' + str(movies_list[i]))
    for i in range(0,len(series_list)):
        if keyword == getattr(series_list[i],'title'):
            print('znalazłem serial ' + str(series_list[i]))             
    return

    #sortuje listę filmów po tytule 
def get_movies():
    sorted_movies_list = sorted(movies_list, key=lambda x: x.title)
    print('===FILMY===')
    for movie in sorted_movies_list:
        #wyświetla filmy alfabetycznie
        print(movie)
    
    #sortuje listę seriali po tytule
def get_series():
    sorted_series_list = sorted(series_list, key=lambda x: x.title)
    print('===SERIALE===')
    for series in sorted_series_list:
        #wyświetla seriale alfabetycznie
        print(series)   

    #przypisuje losową liczbę wyświetleń do instancji filmu i serialu
def generate_views():
    for i in range(0,len(movies_list)):
        movies_list[i].numberOfPlays=random.randint(0,100)
        #print(movies_list[i].numberOfPlays) 
    for i in range(0,len(series_list)):
        series_list[i].numberOfPlays=random.randint(0,100) 
        #print(series_list[i].numberOfPlays)   

def best_score():  
    print("===WYNIKI OGLĄDALNOŚCI FILMÓW===")
    #sortuje listę z instancjami filmów wg. liczby wyświetleń (malejąco) 
    movies_list.sort(key=lambda x: x.numberOfPlays, reverse=True)     
    for i in range(0,len(movies_list)):  
        #wyświetla filmy i liczbę wyświetleń
        print(str(movies_list[i]) + ': ' + str(getattr(movies_list[i],'numberOfPlays'))) 
    #print(best_movie_score)
    print("===WYNIKI OGLĄDALNOŚCI SERIALI===") 
    #sortuje listę z instancjami serialów wg. liczby wyświetleń (malejąco) 
    series_list.sort(key=lambda x: x.numberOfPlays, reverse=True)
    for i in range(0,len(series_list)):      
        #wyświetla seriale i liczbę wyświetleń
        print(str(series_list[i]) + ': ' + str(getattr(series_list[i],'numberOfPlays')))
    #wyświetla najczęściej oglądany film i serial
    print("=================================")
    print('Najczęściej oglądany film dnia ' + str(today) + ' to: ' + str(movies_list[0]) + ' | ilość wyświetleń: ' + str(getattr(movies_list[0],'numberOfPlays')))
    print('Najczęściej oglądany serial dnia ' + str(today) + ' to: ' + str(series_list[0]) + ' | ilość wyświetleń: ' + str(getattr(series_list[0],'numberOfPlays')))
    print("=================================")

def top3():
    print("===WYNIKI OGLĄDALNOŚCI RAZEM===")
    #sortuje listę ze wszystkimi instancjami filmów i seriali wg liczby wyświetleń
    titles_list2.sort(key=lambda x: x.numberOfPlays, reverse=True)
    for i in range(0,len(titles_list2)):
        #wyświetla filmy i seriale razem wg liczby wyświetleń
        print(str(titles_list2[i]) + ': ' + str(getattr(titles_list2[i],'numberOfPlays')))
    print("===TOP 3 OGLĄDALNOŚCI===")
    #wartości 3 tytułów z największą liczbą wyświetleń 
    print('Miejsce 1: ' + str(titles_list2[0]) + ' | ilość wyświetleń: ' + str(getattr(titles_list2[0],'numberOfPlays')))
    print('Miejsce 2: ' + str(titles_list2[1]) + ' | ilość wyświetleń: ' + str(getattr(titles_list2[1],'numberOfPlays')))
    print('Miejsce 3: ' + str(titles_list2[2]) + ' | ilość wyświetleń: ' + str(getattr(titles_list2[2],'numberOfPlays')))

print("==BIBLIOTEKA FILMÓW I SERIALI==")

#wprowadzanie informacji przez użytkownika
while True:
    try:
        selection=int(input('Co chcesz zrobić? 1-Wyszukiwanie Tytułów, 2-Alfabetyczna Lista Tytułów Filmów i Seriali, 3-Najpopularniejsze Filmy i Seriale dzisiaj, TOP 3'))
    except:
        print('Proszę podać cyfrę')
        continue
    if selection==1:
        search()
    if selection==2:
        get_movies()
        get_series()
    if selection==3:
        generate_views()
        best_score()
        top3()



