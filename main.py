import json
import re
import itertools
import time
import os
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Load JSON data
def load_json(file):
    try:
        with open(file, "r") as bot_responses:
            return json.load(bot_responses)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save JSON data
def save_json(file, data):
    with open(file, "w") as bot_responses:
        json.dump(data, bot_responses, indent=2)

# File containing chatbot responses
json_file = "bot.json"
response_data = load_json(json_file)
random_responses = [
    "Hmm, I'm not sure about that...", 
    "I don't understand yet!", 
    "Can you rephrase that?", 
    "That’s new to me!", 
    "Interesting... Tell me more!"
]

def get_response(input_string):
    input_string = input_string.lower()  # Convert input to lowercase
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string)  # Normalize input
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = [word.lower() for word in response["required_words"]]  # Ensure lowercase

        # Check required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):  # All required words must be present
            for word in split_message:
                if word in [w.lower() for w in response["user_input"]]:  # Normalize comparison
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if input_string.strip() == "":
        return Fore.WHITE + "Please type something so we can chat :("

    if best_response != 0:
        return Fore.WHITE + response_data[response_index]["bot_response"]
    
    random_response = random.choice(random_responses)
    print(Fore.YELLOW + random_response)
    
    train = input(Fore.GREEN + "Would you like to train this phrase? (yes/no): ").strip().lower()
    if train == "yes":
        required_words = input("Enter required words (comma-separated, leave blank if none): ").strip().lower()
        required_words = required_words.split(', ') if required_words else []  # Fix blank case
        bot_response = input("Enter bot response: ")

        new_response = {
            "response_type": "user_defined",
            "user_input": split_message,  # Store input in lowercase
            "bot_response": bot_response,
            "required_words": required_words
        }
        
        response_data.append(new_response)
        save_json(json_file, response_data)
        print(Fore.GREEN + "New response added successfully!")
    
    return ""


def loading_animation(duration=0.7):
    spinner = itertools.cycle(["-", "\\", "|", "/"])
    end_time = time.time() + duration
    while time.time() < end_time:
        print(Fore.GREEN + f"\r{next(spinner)}", end="", flush=True)
        time.sleep(0.09)
    print("\r", end="")

def animate_response(response, speed=0.05):
    words = response.split()
    for word in words:
        print(Fore.WHITE+word, end=' ', flush=True)
        time.sleep(speed)
    print()

def train_chatbot():
    print(Fore.YELLOW + "\nTraining mode: Add a new response")
    user_input = input("Enter user input (comma-separated words): ").strip().lower()
    required_words = input("Enter required words (comma-separated, leave blank if none): ").strip().lower()
    bot_response = input("Enter bot response: ")

    user_input_list = user_input.split(', ') if user_input else []
    required_words_list = required_words.split(', ') if required_words else []  # Handle empty case

    new_response = {
        "response_type": "user_defined",
        "user_input": user_input_list,
        "bot_response": bot_response,
        "required_words": required_words_list
    }

    response_data.append(new_response)
    save_json(json_file, response_data)
    print(Fore.GREEN + "New response added successfully!")


def main():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print(Fore.CYAN + "\n1. Chat with chatbot")
        print(Fore.MAGENTA + "2. Train chatbot")
        print(Fore.RED + "3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                user_input = input(Fore.LIGHTCYAN_EX + "You: " + Fore.WHITE)
                if user_input.lower() in ["exit", "quit", "bye"]:
                    break
                elif user_input.lower() == "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("wipe wipe.")
                
                loading_animation()
                response = get_response(user_input)
                if response:
                    animate_response(response)
        elif choice == "2":
            train_chatbot()
        elif choice == "3":
            print(Fore.RED + "Goodbye!")
            break
        else:
            print(Fore.YELLOW + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()