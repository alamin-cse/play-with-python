from datetime import datetime
import time
import random
odds = [ 1, 3,  5,  7,  9,  11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]
for num in range(5):
    right_this_minutes = datetime.today().minute

    if right_this_minutes in odds:
        print("this minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1,10)
    print("you have to wait ", wait_time, "seconds")
    for num in range(wait_time):
        new_wait_time = wait_time
        print(new_wait_time)
        new_wait_time = new_wait_time - 1
    time.sleep(wait_time)
