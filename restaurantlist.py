from linkedlist import linkedlist as LL
from restaurant import restaurant

class restaurantlist(LL):
        def __init__(self):
                LL.__init__(self)
                
        def makeRestaurant(self, score1=0, score2=0, name="", type="", address=""):
                r = restaurant()
                score = r.getScore(score1, score2)
                r.makeRestaurant(score, name, type, address)
                return r
        