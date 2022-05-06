from src.my_module import get_cheapest_hotel
def Menu():
    print("1 - New Entry")
    print("2 - Quit")


while (True):
    Menu()
    user_entry = int(input("Your option: "))
    if (user_entry == 2): break
    if (user_entry == 1):
        data = input("Write your entry: ")
        hotel = get_cheapest_hotel(data)
        print("Best hotel: {0}".format(hotel))