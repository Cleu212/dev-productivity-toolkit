import time

def countdown(minutes, session_type):
    seconds = minutes * 60
    print(f"\n{session_type} session started for {minutes} minutes.")

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print(f"\n{session_type} session finished!")

def start_pomodoro(focus_time, break_time, cycles):
    for cycle in range(1, cycles + 1):
        print(f"\n--- Cycle {cycle} ---")

        countdown(focus_time, "Focus")

        if cycle < cycles:
            countdown(break_time, "Break")

    print("\nAll cycles completed! Great job! 🚀")

def main():
    print("Custom Pomodoro Timer")

    try:
        focus_time = int(input("Enter focus time (minutes): "))
        break_time = int(input("Enter break time (minutes): "))
        cycles = int(input("How many cycles do you want to complete? "))

        if focus_time <= 0 or break_time <= 0 or cycles <= 0:
            print("Values must be greater than 0.")
            return

        start_pomodoro(focus_time, break_time, cycles)

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

