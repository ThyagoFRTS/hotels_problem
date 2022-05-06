# Syngenta Challenge

This is an aplication for intership program from Syngenta

## The Challange

The chanllange is to optimize cost benefit in hotel's ticket (Lakewood, Bridgewood and Ridgewood). The next table will display status from each hotel.
- In week day

| User Type | Lakewood | Bridgewood | Ridgewood |
|-----------|----------|------------|-----------|
| Regular   | 110      | 160        | 220       |
| Rewards   | 80       | 110        | 100       |

- In weekend

| User Type | Lakewood | Bridgewood | Ridgewood |
|-----------|----------|------------|-----------|
| Regular   | 80       | 110        | 100       |
| Rewards   | 80       | 50         | 40        |

In case of a tie, the hotel with the most stars is selected
| Hotel Name | Stars |
|------------|-------|
| Lakewood   | 3     |
| Bridgewood | 4     |
| Ridgewood  | 5     |

## Installation

This app requires Python 3 to run.

- Download [Python](https://www.python.org/)

- Download zip code or git clone in your bash and enter on folder.

```sh
~/dev$ cd hotels_problem
```
- To install the required modules:
```
~/dev/hotels_problem$ pip install -r requirements.txt
```
- or
```
~/dev/hotels_problem$ pip3 install -r requirements.txt
```
## How to Use
- Run this command in your bash to use command line program
```sh
~/dev/hotels_problem$ python main.py
```
- To run the (failing) test:
```
~/dev/hotels_problem$ py.test
```

