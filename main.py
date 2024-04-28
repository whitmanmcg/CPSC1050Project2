"""
Author:         Whitman McGuckin
Date:           4/27/24
Assignment:     Project 2
Course:         CPSC1050
Course Section:    001
GitHub Link: https://github.com/whitmanmcg/CPSC1050Project2

CODE DESCRIPTION: A thrilling rpg game that takes you through 
different scenarios seeing if you can make it to class on 
time or not.

"""
import random
import time
from game_log import GameLog

# Function to get valid player names
def players_names(prompt):
    while True:
        name = input(prompt)  # Get player input
        if not name.isdigit():  # Check if the input is not a number
            return name  # Return the valid name
        print("Invalid name. Please enter a non-numeric name.")  # Show an error message

# Base class for different transportation methods
class Transport:
    def __init__(self, name):
        self.name = name  # Store the name of the transport

    def calculate_travel_time(self):
        pass  # Base class does not implement this method; derived classes will

# Derived class for Bike transport
class Bike(Transport):
    def __init__(self):
        super().__init__("Bike")  # Initialize with "Bike" as name

    def calculate_travel_time(self, game_log):
        weather = random.choice(["good", "bad"])  # Random weather condition
        travel_time = 15  # Base travel time by bike
        
        game_log.write(f"Chose transport: {self.name}")
        
        # Adjust travel time based on weather
        if weather == "bad":
            travel_time += 5  # Add time for bad weather
            game_log.write("Weather is bad, added 5 minutes to travel time.")
        
        # Let player choose the bike path with different risks
        print("Choose a bike path:")
        print("1. The longest and safest (15 minutes)")
        print("2. The medium length with a risk of falling (10 minutes)")
        print("3. The shortest but most dangerous (5 minutes)")
        
        while True:
            choice = input("Enter your choice (1, 2, or 3): ")  # Get player input
            if choice in ["1", "2", "3"]:
                break  # Valid choice, break loop
            print("Invalid input. Please choose 1, 2, or 3.")  # Invalid choice message
        
        game_log.write(f"Bike path choice: {choice}")
        
        # Adjust travel time based on chosen path
        if choice == "1":  # Safest path, additional base time
            travel_time += 15
        elif choice == "2":  # Medium length with risk
            if random.choice([True, False, False]):  # 1/3 chance of falling
                print("You fell! Adding 10 minutes.")
                travel_time += 10
                game_log.write("Fell on the bike path, added 10 minutes to travel time.")
            travel_time += 10  # Base time for this path
        elif choice == "3":  # Shortest but most dangerous
            if random.choice([False, True, True, True, True]):  # High risk of accident
                print("You got hit by a car! Game over.")
                game_log.write("Got hit by a car, game over.")
                return -1  # Special value indicating game over
            else:
                travel_time += 5
        
        return travel_time  # Return calculated travel time

# Derived class for Bus transport
class Bus(Transport):
    def __init__(self):
        super().__init__("Bus")  # Initialize with "Bus" as name
    
    def calculate_travel_time(self, game_log):
        bus_wait_time = random.randint(0, 15)  # Random waiting time for the bus
        print(f"Waiting time for the bus: {bus_wait_time} minutes.")
        game_log.write(f"Bus waiting time: {bus_wait_time} minutes.")
        
        traffic_time = random.randint(10, 15)  # Random traffic delay time
        print(f"Travel time due to traffic: {traffic_time} minutes.")
        game_log.write(f"Bus travel time due to traffic: {traffic_time} minutes.")
        
        # Random bus breakdown event
        if random.choice([False, False, False, True, False]):  # 1/5 chance of breakdown
            print("The bus broke down! Game over.")
            game_log.write("Bus broke down, game over.")
            return -1  # Special value indicating game over
        
        # Return total bus travel time
        return bus_wait_time + traffic_time

# Derived class for Car transport
class Car(Transport):
    def __init__(self):
        super().__init__("Car")  # Initialize with "Car" as name
    
    def calculate_travel_time(self, game_log):
        # Random car breakdown event
        if random.choice([False, False, False, True, False]):  # 1/5 chance of breakdown
            print("The car broke down! Game over.")
            game_log.write("Car broke down, game over.")
            return -1  # Special value indicating game over
        
        travel_time = 15  # Base travel time by car
        traffic_time = random.randint(10, 20)  # Random traffic delay time
        
        print(f"Travel time due to traffic: {traffic_time} minutes.")
        game_log.write(f"Car travel time due to traffic: {traffic_time} minutes.")
        print(f"Adding {traffic_time} minutes to overall time.")
        
        # Let player choose a driving path
        print("Choose a driving path:")
        print("1. The first row (chance of no parking spot)")
        print("2. Default parking (5 minutes)")
        
        while True:
            choice = input("Enter your choice (1 or 2): ")  # Get player input
            if choice in ["1", "2"]:
                break  # Valid choice, break loop
            print("Invalid input. Please choose 1 or 2.")  # Invalid choice message
        
        game_log.write(f"Car parking choice: {choice}")
        
        # Adjust travel time based on chosen parking option
        if choice == "1":  # First-row parking with risk of not finding a spot
            if random.choice([True, False, False]):  # 1/3 chance of finding a spot
                print("You found a parking spot in the first row!")  # No extra time
            else:
                print("No parking spot in the first row, adding 5 minutes.")  # Extra time
                travel_time += 5
                game_log.write("Could not find a parking spot, added 5 minutes.")
        elif choice == "2":  # Default parking, extra time
            travel_time += 5
        
        # Return total car travel time
        return travel_time + traffic_time

# Main game class that manages the gameplay and interactions
class Game:
    def __init__(self, player_name, friend_name):
        self.player_name = player_name  # Store player name
        self.friend_name = friend_name  # Store friend name
        self.game_log = GameLog()  # Initialize game logging
        self.overall_time = 0  # Keep track of total travel time
    
    # Display the current overall travel time
    def show_overall_time(self):
        print(f"Overall travel time: {self.overall_time} minutes.")
        self.game_log.write(f"Overall travel time: {self.overall_time} minutes.")
    
    # Start the game and manage the gameplay
    def start(self):
        self.overall_time = 0  # Reset overall time at the start
        
        # Welcome the player
        print(f"Welcome to 'Can You Make it to 1050 on Time?', {self.player_name}!")
        self.game_log.write(f"Game started with player: {self.player_name}")
        
        class_start_time = 60  # Time limit to reach the class
        
        ready_time = random.randint(10, 20)  # Random time taken to get ready
        print(f"It took you {ready_time} minutes to get ready.")
        self.game_log.write(f"Getting ready took {ready_time} minutes.")
        
        self.overall_time += ready_time  # Add the time taken to get ready
        self.show_overall_time()  # Display the current overall time
        
        self.game_log.write(f"Overall time after getting ready: {self.overall_time} minutes.")

        # Let player choose a mode of transport
        print("Choose a mode of transport:")
        print("1. Bike")
        print("2. Bus")
        print("3. Car")
        
        while True:
            transport_choice = input("Enter your choice (1, 2, or 3): ")  # Get player input
            if transport_choice in ["1", "2", "3"]:  # Check for valid choice
                break
            print("Invalid choice. Please choose 1, 2, or 3.")  # Invalid choice message
        
        # Log transport choice
        self.game_log.write(f"Chose mode of transport: {transport_choice}")
        
        # Instantiate the chosen mode of transport
        if transport_choice == "1":
            transport = Bike()
        elif transport_choice == "2":
            transport = Bus()
        elif transport_choice == "3":
            transport = Car()

        # Calculate travel time and check for game-over scenarios
        travel_time = transport.calculate_travel_time(self.game_log)  # Calculate travel time
        if travel_time == -1:  # Check if the game is over due to a breakdown or accident
            self.game_log.write("Game over. Transport event ended the game.")  # Log the event
            return
        
        self.overall_time += travel_time  # Add travel time to the overall time
        self.show_overall_time()  # Display the current overall time
        
        print("You've arrived on campus.")  # Player arrives on campus
        self.game_log.write("Arrived on campus.")

        # Check if the player trips while walking to class
        if random.choice([False, True, False]):  # 1/3 chance of tripping
            print("You tripped and fell! Adding 5 minutes.")  # Add time due to tripping
            self.game_log.write("Tripped and fell, added 5 minutes.")
            self.overall_time += 5
            self.show_overall_time()  # Display the current overall time
        
        # Interaction with a friend and resulting scenarios
        print(f"Your friend, {self.friend_name}, approaches you to talk.")  # Friend interaction
        print("Do you want to ignore them or talk to them?")
        print("1. Ignore")
        print("2. Talk")

        while True:
            friend_choice = input("Enter your choice (1 or 2): ")  # Get player input
            if friend_choice in ["1", "2"]:  # Check for valid choice
                break
            print("Invalid choice. Please choose 1 or 2.")  # Invalid choice message
        
        self.game_log.write(f"Friend interaction choice: {friend_choice}")
        
        if friend_choice == "1":  # Player chooses to ignore the friend
            print(f"You ignored {self.friend_name}. They will hate you forever.")  # Negative outcome
            self.show_overall_time()  # Display the current overall time
            self.game_log.write(f"Ignored friend: {self.friend_name}.")
        elif friend_choice == "2":  # Player chooses to talk to the friend
            print(f"{self.friend_name}: 'Hey, have you seen that documentary on Bohemian Grove?'")
            print("1. 'Yes, George Bush is an illuminati agent.'")
            print("2. 'No, have you been skipping your schizophrenia meds?'")
            
            while True:
                response_choice = input("Enter your response (1 or 2): ")  # Get player input
                if response_choice in ["1", "2"]:  # Check for valid choice
                    break
                print("Invalid choice. Please choose 1 or 2.")  # Invalid choice message
        
            self.game_log.write(f"Response to friend: {response_choice}")
            
            # Based on the player's response, determine the outcome of the conversation
            if response_choice == "1":  # Conspiracy-based response
                print(f"{self.friend_name}: 'Yes, my brother, we must be vigilant. I hear them in my walls.'")
                print(f"{self.friend_name} runs off screaming unknown words. Conversation over. Adding 5 minutes to overall time.")  # Add time due to friend's reaction
                self.game_log.write(f"Friend reacted with conspiracy, added 5 minutes.")
                self.overall_time += 5
                self.show_overall_time()  # Display the current overall time
            elif response_choice == "2":  # Mocking response
                print(f"{self.friend_name}: 'Ah, so they've gotten to you.' {self.friend_name} throws sand in your eyes!")
                print("Sand got in your eyes. Adding 10 minutes to overall time.")  # Add time due to sand throwing
                self.game_log.write(f"Friend threw sand, added 10 minutes.")
                self.overall_time += 10
        
        # Final stretch to class, adding more time to the overall time
        print("It takes you 5 minutes to finish walking to class.")  # Additional time for walking to class
        self.overall_time += 5  
        self.show_overall_time()  # Display the current overall time
        self.game_log.write("Finished walking to class, added 5 minutes.")
        
        # Check if the player made it to class on time
        if self.overall_time <= class_start_time:  # If within time limit
            print("You made it to class on time!")  # Positive outcome
            self.game_log.write("Made it to class on time.")
        else:
            print("You didn't make it to class on time!")  # Negative outcome
            self.game_log.write("Did not make it to class on time.")
        
        # Log the final outcome and overall travel time
        self.game_log.write(f"Game ended. Final overall time: {self.overall_time} minutes.")  # Log the outcome

        # Ask if the player would like to play again
        print("Would you like to play again? (yes or no)")  
        while True:
            play_again = input("Enter your choice: ")  # Get player input
            if play_again.lower() in ["yes", "no"]:  # Check for valid choice
                break
            print("Invalid choice. Please answer with 'yes' or 'no'.")  # Invalid choice message
        
        # Restart or end the game based on player's choice
        if play_again.lower() == "yes":  # If player wants to play again
            self.start()  # Restart the game
            self.game_log.write("Game restarted.")
        else:
            print("Thank you for playing!")  # End the game
            self.game_log.write("Game ended by user choice.")

# Run the game if the script is executed directly
if __name__ == "__main__":
    player_name = players_names("Enter your name: ")  # Get player name
    friend_name = players_names("Enter your best friend's name: ")  # Get friend's name
    game = Game(player_name, friend_name)  # Instantiate the game with player and friend names
    game.start()  # Start the game
