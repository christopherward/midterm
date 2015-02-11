#movie_database.py
#Christopher Ward
#MPCS 50101 Midterm

import csv
import json
from urllib.request import urlopen

class Movie:

    def __init__(self, imdb_rating, title, director):
        #initialize title, rating, and director variables
        self.title = title
        self.imdb_rating = imdb_rating
        self.director = director

    def find_highest_rated(self):
        #open library of top 250 movies
        file = open(self)
        reader = csv.reader(file)

        #initialize highest_rating variable against which other ratings are compared
        highest_rating = 0.0

        #read from library and identify movie with highest rating
        for row in reader:
            if float(row[3]) > highest_rating:
                highest_rating = float(row[3])
                title = row[1]
                director = row[2]
                
        #return movie characteristics as object
        return Movie(highest_rating, title, director)

        #close CSV file
        file.close()

    def plot(self):
        #call API to retrieve all metadata for best movie
        webservice_url = "http://www.omdbapi.com/?t=" + self.title.replace(" ","+") + "&y=&plot=&r=json"
        data = urlopen(webservice_url).read().decode("utf8")
        result = json.loads(data)

        #returns plot metadata
        return(result['Plot'])
