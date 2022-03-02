mylist = [1,2,3]
# myString = "my string"


# print(len(mylist))
# print(len(myString))

class Movie():
    def __init__(self, title, director, duracation):
        self.title = title
        self.director = director
        self.duracation = duracation
        print("Movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duracation

    def __del__(self):
        print("movie deleted")



m = Movie("film adı", "yönetmen adı", 120)

# print(str(mylist))
print(str(m))

# print(len(mylist))
# print(len(m))

del m


