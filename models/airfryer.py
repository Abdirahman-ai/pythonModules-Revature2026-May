"""""
Airfryer module for practicing Python modules, logging, exceptions,
regular expressions, and math operations.
"""""

import logging
import math
import re
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("airfryer.log"),
        logging.StreamHandler(sys.stdout),
    ],
)


class Airfryer:
    """""
    Represents an air fryer with methods for frying food,
    setting temperature, registering users, and calculating tips.
    """""

    def fry(self):
        """""
        Fry food using the air fryer.
        """""
        logging.info("Airfryer is frying")
        return "Chips is frying food"

    def set_temperature(self, temperature):
        """""
        Set the air fryer temperature between 0 and 100 degrees Celsius.
        """""
        if temperature < 0 or temperature > 100:
            logging.warning(
                "Attempting to set temperature outside range %s",
                temperature,
            )
            raise ValueError("Temperature must be between 0 and 100")

        logging.info("Setting temperature to %s", temperature)
        return f"Airfrying temperature set to {temperature} degrees C"

    def register_user(self, username):
        """""
        Register a user after checking the username for blocked words.
        """""
        if re.search(r"javascript", username, re.IGNORECASE):
            logging.warning("User tried to use a blocked word")
            raise ValueError("Username cannot contain vulgarity")

        logging.info("Registering user %s", username)
        return f"User {username} registered successfully"

    def calculate_tip(self, weight):
        """""
        Calculate a suggested tip based on weight.
        """""
        if weight < 0 or weight > 100:
            logging.warning(
                "Attempting to set weight outside range %s",
                weight,
            )
            raise ValueError("Weight must be between 0 and 100")

        tip = math.pow(weight, 1.2) * 0.18

        print(f"Suggested tip of {tip:.2f} will be charged automatically")
        print(f"You may round up to {math.ceil(tip)} cents if you'd like")
        print(f"or you may round down to {math.floor(tip)} cents if you watch an ad")

        logging.info("Calculating tip for weight %s", weight)
        return tip
