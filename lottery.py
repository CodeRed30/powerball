import random

white_possibles = list(range(1, 70))
red_possibles = list(range(1,27))

tickets_per_draw = 1
num_draws = 1

total_spent = 0
earnings = 0

times_won = {
    "5 Balls + Powerball": 0,
    "5 Balls": 0,
    "4 Balls + Powerball": 0,
    "4 Balls": 0,
    "3 Balls + Powerball": 0,
    "3 Balls": 0,
    "2 Balls + Powerball": 0,
    "1 Ball + Powerball": 0,
    "0 Balls + Powerball": 0,
    "0 Balls": 0,
}

def winning_calc(my_numbers, winning_numbers):
    win_amount = 0
    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_match = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5:
        if power_match:
            win_amount = 2000000
            times_won["5 Balls + Powerball"] += 1
        else:
            win_amount = 1000000
            times_won["5 Balls"] += 1
    elif white_matches == 4:
        if power_match:
            win_amount = 50000
            times_won["4 Balls + Powerball"] += 1
        else:
            win_amount = 100
            times_won["4 Balls"] += 1
    elif white_matches == 3:
        if power_match:
            win_amount = 100
            times_won["3 Balls + Powerball"] += 1
        else:
            win_amount = 7
            times_won["3 Balls"] += 1
    elif white_matches == 2 and power_match:
        win_amount = 7
        times_won["2 Balls + Powerball"] += 1
    elif white_matches == 1 and power_match:
        win_amount = 4
        times_won["1 Ball + Powerball"] += 1
    elif power_match:
        win_amount = 4
        times_won["0 Balls + Powerball"] += 1
    else:
        times_won["0 Balls"] += 1


    return win_amount

for draw in range(num_draws):
    white_draw = set(random.sample(white_possibles, k=5))
    red_draw = random.choice(red_possibles)

    winning_numbers = {
        "whites": white_draw, "red": red_draw
        }
    for ticket in range(tickets_per_draw):
        total_spent += 2
        white_choices = set(random.sample(white_possibles, k=5))
        red_choice = random.choice(red_possibles)
        my_numbers = {
        "whites": white_choices, "red": red_choice
        }
    
    # winning_calc(my_numbers)

