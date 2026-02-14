import time

FOCUS_TIME = 25
BREAK_TIME = 5

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

def start_pomodoro(cycles):
    for cycle in range(1, cycles + 1):
        print(f"\n--- Cycle {cycle} ---")
        
        countdown(FOCUS_TIME, "Focus")
        
        if cycle < cycles:
            countdown(BREAK_TIME, "Break")
    
    print("\nAll cycles completed! Great job! 🚀")

def main():
    print("Pomodoro Timer (25/5 Mode)")
    try:
        cycles = int(input("How many cycles do you want to complete? "))
        start_pomodoro(cycles)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
