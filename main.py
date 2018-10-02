import sys
import time
import win32api

def move_mouse(movement_x, movement_y, velocity_x, velocity_y):
    """
    This function will move the mouse cursor back and forth until the Q button is pressed

    :param movement_x: if positive, move to the right. Negative, move to the left
    :param movement_y: if positive, move up. Negative, move down.
    :param velocity_x: How many pixels to move each second, left and right.
    :param velocity_y: how many pixels to move each second, up and down.
    :return:
    """

    current = win32api.GetCursorPos()
    current_x = start_x = current[0]
    current_y = start_y = current[1]

    print("Moving x={} y={} with velocity={} pixels per second".format(movement_x, movement_y, velocity_x))
    print("Press 'q' to quit")

    last = time.time()

    while (True):   # Infinite loop until Q is pressed
        if win32api.GetAsyncKeyState(ord('Q')):     # if the Q key is pressed, we exit
            sys.exit()

        current = time.time()
        tick = current - last
        last = current

        print("Current position {},{}".format(current_x,current_y)) #output the current position
        if movement_x > 0:
            current_x += velocity_x * tick;
            if current_x > movement_x + start_x or current_x < start_x:
                velocity_x = -velocity_x;   #change direction
                current_x = max(start_x, min(movement_x + start_x, current_x))
        if (movement_y > 0):
            current_y += velocity_y * tick;
            if current_y > movement_y + start_y or current_y < start_y:
                velocity_y = -velocity_y;   #change direction
                current_y = max(start_y, min(movement_y + start_y, current_y))

        print("New position {},{}".format(current_x, current_y))    #output the new position
        win32api.SetCursorPos((int(current_x), int(current_y)))     # set the cursor to the new position
        time.sleep(1)   # wait 1 second

if __name__=="__main__":
    move_mouse(10,10,10,10)
