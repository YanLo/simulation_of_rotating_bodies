from matplotlib import pylab as plt
from num_integration_methods import rungekut
import os

def create_frame(t, x):
    plt.clf()
    plt.plot([-3, 3], [0, 0], '-k')
    plt.plot(x[0], 0, 'ob', ms=20)
    plt.plot([0, x[0]], [0, 0], '-r', ms=10)

    plt.xlim([-3, 3])
    plt.title('t = {:.2f} c'.format(t))
    plt.savefig('frames/f_{:04.0f}.png'.format(t * 100), bbox_inches='tight', dpi=240)

def create_video(duration, model_func):
    frame_per_second = 25
    num_of_frames = duration * frame_per_second
    step = 1/frame_per_second

    if not os.path.exists('frames'):
        os.makedirs('frames')

    t = 0
    x = [1, 2]
    create_frame(t, x)
    for i in range(num_of_frames):
        x = rungekut(model_func, t, t+step, x)
        t = t + step
        create_frame(t, x)

    if os.path.exists('simulation_{}.avi'.format(model_func.__name__)):
        os.remove('simulation_{}.avi'.format(model_func.__name__))
    os.system('ffmpeg -f image2 -pattern_type glob -framerate 25 -i "frames/f_*.png" '
              '-s 1080x1080 simulation_{}.avi'.format(model_func.__name__))