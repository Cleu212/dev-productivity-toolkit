import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a break!")

print("Pomodoro Timer")
minutes = int(input("Enter focus time in minutes: "))
countdown(minutes)
