class Movie:
    name = ""
    yearLaunch = 0 
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro filme
movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130

#Segundo filme
movie2 = Movie()
movie2.name = "De Volta pro Futuro"
movie2.yearLaunch = 1970
movie2.includedPlan = True
movie2.note = 5.0
movie2.durationMinutes = 120


print("#Dados do Filme##")
print(f"1 - Nome do filme: {movie.name}\nAno de Lançamento: {movie.yearLaunch      } ")
print(f"2 - Nome do filme: {movie2.name}\nAno de Lançamento: {movie2.yearLaunch      } ")