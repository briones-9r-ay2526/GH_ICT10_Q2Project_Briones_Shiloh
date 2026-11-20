# Q2 Project: Student Showcase
from pyscript import display, document


# Seatwork #1: Nickname Atlas
def get_nickname(e):
    document.getElementById('output').innerHTML = " " # Clears previous answer

    # Set variables: countries and their corresponding nicknames
    country_nicknames = {
        "germany": "The Land of Poets and Thinkers",
        "france": "The Hexagon",
        "switzerland": "The Land of Milk and Honey",
        "belgium": "The Battlefield of Europe",
        "netherlands": "The Low Countries",
        "austria": "The Land of Beauty and Music",
        "luxembourg": "The Grand Duchy",
        "monaco": "The Billionaire's Playground",
        "liechtenstein": "The Principality"
    }

    country = document.getElementById('country_input').value.lower()

    # Looks up nickname; Default message if not available
    nicknames = country_nicknames.get(country, "Sorry, can't seem to find a nickname for that country. Please try again!")

    display(f"Nickname: {nicknames}", target='output')


# Skills Test: Element Checker
non_metals = { # Set variables: chemical symbols and their corresponding element name, atomic number, and atomic mass
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.07),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.9),
    "Se": ("Selenium", 34, 78.96),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.905),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222),
}

def get_element (e):
    document.getElementById('result').innerHTML = " " # Clears previous answer

    element = document.getElementById('element_symbol').value.title().strip() # Allows user input not to be case sensitive

    result = non_metals.get( # Uses .get() to find element
    element, ("Element not found", "-", "-")
    )

    # Displays information
    document.getElementById('result').innerHTML = f""" 
    <b>Chemical Symbol:</b> {element}<br>
    <b>Element Name:</b> {result[0]}<br>
    <b>Atomic Number:</b> {result[1]}<br>
    <b>Atomic Mass:</b> {result[2]}
    """


# Participation Activity: School Club Members
def add_name(e):
    document.getElementById('output').innerHTML = ' '

    #  Set variables
    seven = {'Adarna Ibon', 'Don Juan de la Cruz', 'Don Diego de la Cruz', 'Don Pedro de la Cruz'}
    eight = {'Florante Flores', 'Laura Lopez', 'Aladin Alcaraz', 'Adolfo Adecer'}
    nine = {'Crisostomo Ibarra', 'Maria Clara de los Santos', 'Elias Esguerra'}
    ten = {'Simoun Ibarra', 'Basilio Briones', 'Isagani Irinco', 'Juli Hernandez'}

    fname = document.getElementById('fname').value.title().strip()
    lname = document.getElementById('lname').value.title().strip()

    # Create master list and adds user input
    members = (seven | eight | nine | ten)
    members.add(fname + lname)

    # Displays
    display(f'Congratulations {fname} {lname}! Welcome to the OBMC Social Studies Club.', target='output')

    display(f'List of members: {members}.', target='output')
    display(f'Total number of members: {len(members)}', target='output')