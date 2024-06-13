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

movies_list=[]
series_list=[]

#Wypełniam bibliotekę filmami:

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
movie_scores={}
series_scores={}
titles_list2=movies_list+series_list

def search():
    keyword = str(input('Proszę podać tytuł'))
    for i in range(0,len(movies_list)):
        if keyword == getattr(movies_list[i],'title'):
            print('znalazłem film ' + str(movies_list[i]))
    for i in range(0,len(series_list)):
        if keyword == getattr(series_list[i],'title'):
            print('znalazłem serial ' + str(series_list[i]))             
    return

def generate_views():
    for i in range(0,len(movies_list)):
        movies_list[i].numberOfPlays=random.randint(0,100)
        #print(movies_list[i].numberOfPlays) 
    for i in range(0,len(series_list)):
        series_list[i].numberOfPlays=random.randint(0,100) 
        #print(series_list[i].numberOfPlays)   

def best_score():
    for i in range(0,len(movies_list)):
        movie_scores[movies_list[i].title]=movies_list[i].numberOfPlays   
    best_movie_score = max(movie_scores.values())
    for i in range(0,len(series_list)):
        series_scores[series_list[i].title]=series_list[i].numberOfPlays 
    best_series_score = max(series_scores.values())  
    print("===WYNIKI OGLĄDALNOŚCI FILMÓW===")      
    print(movie_scores)
    #print(best_movie_score)
    print("===WYNIKI OGLĄDALNOŚCI SERIALI===")   
    print(series_scores)
    print("=================================")
    for i in range(0,len(movies_list)):
        if best_movie_score == getattr(movies_list[i],'numberOfPlays'):
            print('Najczęściej oglądany film dnia ' + str(today) + ' to: ' + str(movies_list[i]))
    for i in range(0,len(series_list)):
        if best_series_score == getattr(series_list[i],'numberOfPlays'):
            print('Najczęściej oglądany serial dnia ' + str(today) + ' to: ' + str(series_list[i]))
    print("=================================")

def top3():
    print("===WYNIKI OGLĄDALNOŚCI RAZEM===")
    scores={**movie_scores,**series_scores} 
    sorted_scores=sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(sorted_scores)   
    print("===TOP 3 OGLĄDALNOŚCI===")
    top1 = sorted_scores[0][0]
    top2 = sorted_scores[1][0]
    top3 = sorted_scores[2][0]
    for i in range(0,len(titles_list2)):
        if top1 == getattr(titles_list2[i],'title'):
            print('Miejsce 1: ' + str(titles_list2[i]))
    for i in range(0,len(titles_list2)):
        if top2 == getattr(titles_list2[i],'title'):
            print('Miejsce 2: ' + str(titles_list2[i]))
    for i in range(0,len(titles_list2)):
        if top3 == getattr(titles_list2[i],'title'):
            print('Miejsce 3: ' + str(titles_list2[i]))

print("==BIBLIOTEKA FILMÓW I SERIALI==")

while True:
    try:
        selection=int(input('Co chcesz zrobić? 1-Wyszukiwanie Tytułów, 2-Najpopularniejsze Filmy i Seriale dzisiaj, TOP 3'))
    except:
        print('Proszę podać cyfrę')
        continue
    if selection==1:
        print("Podpowiedź: Tytuły w bibliotece:")
        print(titles_list)
        print('================================')
        search()
    if selection==2:
        generate_views()
        best_score()
        top3()



