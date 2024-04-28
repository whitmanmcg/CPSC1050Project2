# game_log.py
import datetime

# Game logging class that handles logging of game events to a file
class GameLog:
    # Initialize the GameLog class with a default or specified log file name
    def __init__(self, file_name="game_log.txt"):  # Default log file is "game_log.txt"
        self.file_name = file_name  # Store the file name for the log

        # Create or overwrite the log file with initial content
        with open(self.file_name, "w") as file:  # Open the file in write mode (creates or clears the file)
            file.write("Game Log\n")  # Write the header for the log
            file.write(f"Created at: {datetime.datetime.now()}\n")  # Record the creation time
            file.write("-" * 20 + "\n")  # Separator line for visual clarity

    # Method to write a new message to the log file with a timestamp
    def write(self, message):
        with open(self.file_name, "a") as file:  # Open the file in append mode (to add new content without erasing existing content)
            file.write(f"{datetime.datetime.now()}: {message}\n")  # Write the message with a timestamp
