class restaurant:
        def __init__(self):
                self.score = None
                self.name = None
                self.type = None
                self.address = None
                
        def __str__(self):
                str = "{0} serves {1} food, it has a score of {2} and it's on {3}\n".format(self.name, self.type, self.score, self.address)
                return str
        
        def getScore(self, score1=0, score2=0):
                score = int(score1) + int(score2)
                return score
        
        def makeRestaurant(self, score=0, name="", type="", address=""):
                self.score = score
                self.name = name
                self.type = type
                self.address = address