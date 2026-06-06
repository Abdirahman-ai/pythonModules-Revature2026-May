import logging
import sys
# Configuring a Logger with the ptthon Logging Module

logging.basicConfig(
    level=logging.INFO, # allows all levels of logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("airfryer.log"), # logs will get stored in a file
        logging.StreamHandler(sys.stdout), # they will also get printed to the console
    ],
)

class Airfryer:
    # logging.info("Info message")
    # logging.warning("Warning message")
    # logging.error("Error message")

    def fry(self):
        logging.info("Airfryer is frying ")

        return "Chips is frying food"

    # This method has something that can go wrong

    def set_temperature(self, temperature):
        if temperature < 0 or temperature > 100:
            logging.warning(f"Attempting to set temperature outside range {temperature}")
            raise ValueError("Temperature must be between 0 and 100")

        logging.info(f"Setting temperature to {temperature}")
        return f"Airfrying  temperature set to {temperature} degrees C"

    # User Regisration method - will use the regex module ato validate username
    def register_user(self, username):
        """"
            Importing python's regex module
            Regex (Regular Expression module) is a way to pattern match, search, and change strings
        """""
        import re # python's regex module
        if re.search(r"javascript", username, re.IGNORECASE):
            logging.warning("User tried to say a nono word")

            raise ValueError("Username cannot contain vulgarity")

        logging.info(f"Registering user {username}")
        return f"User {username} registered successfully"

    def calculate_tip(self, weight):
        """""
        importing the python module
        this module contains tons of useful math operations and constant (like pi)
        we'll just use a couple functions
        """""
        import math
        if weight < 0 or weight > 100:
            logging.warning(f"Attempting to set weight outside range {weight}")
            raise ValueError("Weight must be between 0 and 100")

        tip = math.pow(weight, 1.2) * .18

        print(f"Suggested tip of {tip:.2f} will be charged automatically")
        print(f"You may round up to {math.ceil(tip)} cents if you'd like ")
        print(f"or you may round down to {math.floor(tip)} cents if you watch an ad")

        logging.info(f"Calculating tip of {weight}")
        return tip




