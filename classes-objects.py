class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)

film_1 = Movie("life of Brian",1979,8.1,True)
film_2 = Movie("spiderman",2026,8.1,True)

films = [film_1,film_2]
print(films[1].title,films[0].title)
films[0].nice_print()