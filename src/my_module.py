import re
import copy

hotels_info = {
    "Lakewood": {
        "num_stars": 3,
        "Regular": {
            "day": 110,
            "weekend": 90,
        },
        "Rewards": {
            "day": 80,
            "weekend": 80
        },
    },
    "Bridgewood": {
        "num_stars": 4,
        "Regular": {
            "day": 160,
            "weekend": 60,
        },
        "Rewards": {
            "day": 110,
            "weekend": 50
        },
    },
    "Ridgewood": {
        "num_stars": 5,
        "Regular": {
            "day": 220,
            "weekend": 150,
        },
        "Rewards": {
            "day": 100,
            "weekend": 40
        },
    },
}

hotel_values = [
    {
        "name": "Lakewood",
        "stars": 3,
        "amount": 0,
    },
    {
        "name": "Bridgewood",
        "stars": 4,
        "amount": 0,
    },
    {
        "name": "Ridgewood",
        "stars": 5,
        "amount": 0,
    }
]


class HandleDate ():
    def __init__(self, string):
        self.data = [x for x in re.split("(\\d+)", string) if x != ""]
        self.extract_variables(self.data)

    def extract_variables(self, dates_in_list):
        self.day = dates_in_list[0]
        self.month = dates_in_list[1]
        self.year = dates_in_list[2]
        self.day_week = dates_in_list[3].replace("(", "").replace(")", "")


def splitData(string):
    return string.split(": ")[0], string.split(": ")[1].split(", ")


def is_weekend(string):
    return True if string in ["fri", "sat"] else False


def get_cheapest_hotel(number):  # DO NOT change the function's name
    userType, data = splitData(number)
    hotel_stats = copy.deepcopy(hotel_values)
    for hotel in  hotel_stats:
        for days in data:
            date = HandleDate(days)
            hotel["amount"] += hotels_info[hotel["name"]][userType]["weekend" if is_weekend(date.day_week) else "day" ]
    hotel_stats.sort(key=lambda x: (x["amount"], -x["stars"]))
    cheapest_hotel = hotel_stats[0]["name"]
    return cheapest_hotel
