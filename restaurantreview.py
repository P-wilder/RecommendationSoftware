from restaurantlist import restaurantlist as RL
from restaurantData import restaurant_data

def makeRestaurantList(data):
        rl = RL()
        for i in data:
                rl.add(rl.makeRestaurant(i[3], i[2], i[1], i[0], i[4]))
        return rl

def main():
        restaurants = makeRestaurantList(restaurant_data)
        print(restaurants)
 
if __name__ == '__main__':
        main()