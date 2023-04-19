# import data and library
from game_data import data
import random

# create list of all existing indexes from the data
num_list = []
for i in range(0, len(data)):
    num_list.append(i)


# function to randomly select new item from the data list
# (if list is already finished, it will be restored), returns index
def select():
    global selected
    if len(num_list) - len(selected) < options:
        selected = []
    num = random.choice(num_list)
    while num in selected:
        num = random.choice(num_list)
    selected.append(num)
    return num


# function to identify article "a"/"an" for the description
def article(word):
    if word[0] == "a":
        return "an"
    else:
        return "a"

    # function to create a description for selected item


def descr(num):
    x_name = data[num]["name"]
    x_desc = data[num]["description"].lower()
    x_country = data[num]["country"]
    x_article = article(x_desc)
    return f"{x_name}, {x_article} {x_desc} from {x_country}."


# function which returns amount of followers for selected index
def followers(num):
    x_fol = data[num]["follower_count"]
    return x_fol


# function which identifies max value in selected library and returns correct answer A/B/C/D etc
def correct_response(library):
    max_value = 0
    correct_answer = ""
    for key in library:
        if library[key] > max_value:
            max_value = library[key]
            correct_answer = key
        elif library[key] == max_value:
            correct_answer = correct_answer + ", " + key
    return correct_answer


# function which returns list of options in format: "A, B or C?""
def text(list_of_options):
    question = ""
    for num in list_of_options:
        if list_of_options.index(num) == 0:
            question += num
        elif list_of_options.index(num) == len(list_of_options) - 1:
            question += " or "
            question += num
            question += "?"
        else:
            question += ", "
            question += num
    return question


# function to identify final wording
def level(score):
    if score > 30:
        return "You are Wizard of knowledge!"
    elif score > 20:
        return "Your mind is supernatural!"
    elif score > 10:
        return "Wow! You are cool!"
    elif score > 5:
        return "Very good!"
    else:
        return "Good!"


# welcome words and selection of level
print("Welcome to the Lower Higher game!")
options = int(input("\nPlease select number of choices from 2 to 20 (the highest is the hardest). "))

# to create options list according to selected level
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
option_list = alphabet[0:options]

# to create empty list of selected items (to avoid duplicates in future)
selected = []

# parameter to decide if game should be continued and counter of correct answers
cont_game = True
counter_win = 0

# game loop, the game is finished after first incorrect answer
while cont_game is True:

    print("\nThere is a list of Instagram profiles:")

    # empty library
    compare_lib = {}

    # library which saves option name and amount of followers
    for X in option_list:
        index = select()
        print(f"{X}: {descr(index)}")
        compare_lib[X] = followers(index)

    # to identify and save correct response in variable
    correct = correct_response(compare_lib)

    # to ask player about his opinion
    player_choice = input(
        f"\nHow do you think, who has the highest amount of followers in instagram?\n{text(option_list)} ").upper()

    # to check if player's answer correct, if no -> game over
    if player_choice in correct:
        counter_win += 1
        print(
            f"\nIt is correct! You have total of {counter_win} correct response(s).\n{level(counter_win)}"
            f"\n\n----------------------------------------------------------------")
    else:
        print(
            f"\nIt is wrong! Correct response was {correct}. Game over. "
            f"You have total of {counter_win} correct response(s).")
        cont_game = False

# final words
print("\nThank you for playing this game!")
