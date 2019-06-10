print("Hi, please choose the model you want to investigate\nEnter corresponding number:")
print("linear oscillator - 1, math pendulum - 2")

from models import oscillation
from make_oscillation import create_video
import os

def get_number():
    user_input = input()
    while not user_input.isdigit():
        print("Please, try again and enter only a one number")
        user_input = input()
    return int(user_input)

model_num = get_number()

if(model_num == 1):
    print("Please, enter the duration of simulation video")
    duration = get_number()
    print("Now we are going to investigate linear oscillator, please wait ..")
    create_video(duration, oscillation)
    print("we are done!\nIf you want to run video press 1")
    if(get_number() == 1):
        os.system('xdg-open simulation_{}.avi'.format(oscillation.__name__))
    else:
        print('Ok, if you do not want to run video now, you can do it later manually. Bye!')

if(model_num == 2):
    print("Now we are going to investigate math pendulum")

if not(model_num in [1, 2]):
    print("Opps, you've failed to choose the model, rerun programm and look at model's numbers carefully")


