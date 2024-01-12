class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name    
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"\nMovie: {self.name}\nYear: {self.yearLaunch}\nIncludedPlan: {self.includedPlan}\nNote: {self.note}\nDuration: {self.durationMinutes}"


movie = Movie("Super Mario Bros",2023,False,5.0,130)
print(movie)
movie2 = Movie("De Volta pro Futuro",1970,True,5.0,120)
print(movie2)