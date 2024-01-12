import tkinter as tk
import time
from datetime import datetime


# Function to change label color
def change_color():
    colors = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFF00",
        "#FF00FF",
        "#00FFFF",
    ]  # List of colors
    for color in colors:
        header_label.config(fg=color)  # Change header label color
        header_label.update()  # Update the label to show the change
        time.sleep(0.5)  # Pause for a short duration


# Function to update countdown clock
def update_clock():
    target_time = datetime(2024, 1, 1, 0, 0, 0)  # Target time: January 1st, 2024
    current_time = datetime.now()
    time_diff = target_time - current_time

    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_label.config(text=f"{days} days {hours:02d}:{minutes:02d}:{seconds:02d}")
    countdown_label.after(1000, update_clock)  # Update every second


# Function to start the animation after countdown
def start_animation():
    countdown_label.pack_forget()  # Hide countdown label
    header_label.config(
        text="Happy New Year 2024!", font=("Arial", 24)
    )  # Update header text
    change_color()  # Start the animation


# Create a tkinter window
root = tk.Tk()
root.title("Countdown to New Year 2024")

# Create a label for the header
header_label = tk.Label(root, text="Countdown to New Year 2024", font=("Arial", 18))
header_label.pack(padx=20, pady=10)

# Create a label for the countdown clock
countdown_label = tk.Label(root, text="", font=("Arial", 18))
countdown_label.pack(padx=20, pady=30)

# Start the countdown clock
update_clock()

# After some time, start the animation
root.after(
    8000, start_animation
)  # Adjust the time before starting the animation (in milliseconds)

root.mainloop()
