# themoviedb.org => movie and series archive
# Use themoviedb's api in your app
# Search for keywords
# Most popular movie list
# In vision movie list

import requests


class TheMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "3fb930011599861922fc94ef0f760ecc"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keywords):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keywords}&page=1")
        return response.json()


movieApi = TheMovieDb()

while True:
    choice = input("1- Popular Movies\n2- Search Movies\n3- Exit\nChoice: ")

    if choice == "3":
        break

    else:
        if choice == "1":
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])

        elif choice == "2":
            keyword = input("Enter keywords: ")
            result = movieApi.getSearchResults(keyword)
            for movie in result["results"]:
                print(movie["name"])
