import time
import emoji


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('BDAY SOON:) :)')
    print(emoji.emojize(":grinning_face_with_big_eyes:"))
    print(emoji.emojize(":winking_face_with_tongue:"))

t = input("enter the time in seconds:  ")

countdown(int(t))