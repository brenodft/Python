class Movie:
    platform = "OneBitFilmes"
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name    
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.durationMinutes = durationMinutes
        self.users = 0
        self.usernote = 0
        self.note_media = 0

    def __str__(self):
        return f"\nMovie: {self.name}\nYear: {self.yearLaunch}\nIncludedPlan: {self.includedPlan}\nNote: {self.note_media}\nDuration: {self.durationMinutes}"

    def technical_sheet(self):
        print("#Dados do Filme##")
        print(f"Plataforma: {Movie.platform}")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano?: {self.includedPlan}")
        print(f"Avaliação do filme: {self.note_media}")
        print(f"Duração do filme: {self.durationMinutes}")

    def review(self):
        temporarynote = float(input("Digite uma nota para o filme: "))
        self.usernote += temporarynote
        self.users = self.users + 1
        self.note_media = self.usernote/self.users



matrix = Movie("Matrix",2023,True,150)
topgun = Movie("Top Gun: Maverick",2022,True,160)


matrix.technical_sheet()

#Modificando a plataforma
Movie.platform = "OneBitCodePRO"
topgun.technical_sheet()