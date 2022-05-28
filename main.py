class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("My name is", name, "and i am", age, "years old. The tracks i registered for are ", tracks," and my score so far is", score, "percent." )
        pass
    def change_name(self, name):
        print("Initial name", self.name, "has been replaced. User's new name is", name,".")
    def change_age(self, age):
        print( "Initial age of user", self.age, "has been replaced. User's new age is", age," years.")    
    def add_track(self, track):
        print("Additional track to the initial list of tracks", self.tracks, "is", track, ".")
    def get_score(self):
        print("User's score is", self.score ," percent.")



Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

#trial
Tonye = Student(name="Tonye", age=29, tracks=["nodeJS", "Figma"], score=89.6)

#Methods
Tonye.change_name("Ndiana")
Tonye.change_age(26)
Tonye.get_score()
