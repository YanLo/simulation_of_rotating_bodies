print("Hi, please choose the model you want to investigate\nEnter corresponding number:")
print("linear oscillator - 1, math pendulum - 2")

from rungekut import rungekut
from models import oscillation

def get_user_choice(list_of_variants):
    user_input = int(input())
    while not user_input in list_of_variants:
        print("Please, enter only one value from the list: ", list_of_variants)
        user_input = int(input())
    return user_input

model_num = get_user_choice([1, 2])
if(model_num == 1):
    print("Now we are going to investigate linear oscillator")


if(model_num == 2):
    print("Now we are going to investigate math pendulum")
