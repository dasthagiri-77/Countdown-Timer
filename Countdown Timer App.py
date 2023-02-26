import time

def countdown_timer():
    try:
        # get timer duration from user
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))
        if minutes < 0 or seconds < 0:
            raise ValueError("Please enter positive values for minutes and seconds.")
        total_seconds = minutes * 60 + seconds

        # countdown timer
        while total_seconds:
            # format time remaining in minutes and seconds
            mins, secs = divmod(total_seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')

            # sleep for 1 second
            time.sleep(1)

            # decrement total_seconds
            total_seconds -= 1

        # print time's up
        print("Time's up!")
    except ValueError as e:
        print(e)

countdown_timer()
