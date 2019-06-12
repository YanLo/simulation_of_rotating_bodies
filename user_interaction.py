import os


def get_number():
    user_input = input()
    while not user_input.isdigit():
        print('Please, try again and enter only a one number')
        user_input = input()
    return int(user_input)


def get_model_properties() -> object:
    print('Please, enter frequency w')
    w = get_number()
    print('Now, please enter dissipation coefficient b')
    b = get_number()
    print('At last, enter the duration of a simulation video')
    duration = get_number()
    return [w, b, duration]


def run_video(properties, model_func):
    print('we are done!\nIf you want to run video press 1')
    if get_number() == 1:
        w = properties[0]
        b = properties[1]
        os.system('xdg-open simulation_{name}_omega_{omega}_dissip_{betta}.avi'.format(
            name=model_func.__name__, omega=w, betta=b))
    else:
        print('Ok, if you do not want to run video now, you can do it later manually. Bye!')
