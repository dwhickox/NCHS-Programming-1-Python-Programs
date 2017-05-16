#David Hickox
#May 2 17
#Chap 5 test EC
#sorts a list of movies and actors
#variables
#   movie, Stores the movie data
#   actors, stotes the actor data

print("Welcome to the (enter name here bumbblefack) Program\n")
movie = []
actors = []
for i in range(5):
    movie.append((input("Movie "+str(i+1)+"? ")).title())
    actors.append((input("Who stars in "+movie[i]+"? ")).title())


rng = len(movie)
sw = 1
while sw == 1:
    sw = 0
    for i in range(rng):
        if movie[i]<movie[i-1] and i != 0:
            sw = 1
            temp = movie[i]
            tempa = actors[i]
            movie[i] = movie[i-1]
            actors[i] = actors[i-1]
            movie[i-1] = temp
            actors[i-1] = tempa
            
    rng -= 1
print("\nMovies\t\tActor")
for i in range(len(movie)):
    if len(movie[i])>7:
        print(movie[i],actors[i],sep = "\t")
    else:
        print(movie[i],actors[i],sep = "\t\t")



input("\nPress Enter to Exit")
