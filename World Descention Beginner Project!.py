# --- Some World's Descention Prototype, fam ---
# Upgraded version with Loops, Functions, and String Methods

# These things below are important - time for printing text slow, and random for usage in R.N.G within the main combat
import time
import random

# define = makes a function, the one below is to print text slow/with a delay in the main console - Sci-fi like feel yo
def print_slow(text, delay=0.05):
    """Prints text to the console one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the text

# --- This is the main terminal boot sequence ooo, a small prototype to help me with --
def boot_terminal():
    """Simulates the terminal activation sequence."""
    print_slow("--- Activating Terminal... ---", 1.0)
    print_slow(".....", 1.5)
    print_slow("....", 0.5)
    print_slow("...", 0.4)
    print_slow("--- Terminal Activated, opening... ---", 1.0)
    print_slow("--- Welcome to World's Descention First Project! Made by yours truly, Cooper ---", 2.0)

# --- the function is for names, future-me, use this as an example lmao --
def get_player_name():
    """Gets the player name and ensures it isn't blank."""
    while True:
        time.sleep(1.0)
        name = input("\nType (or just write) in your name in the terminal, and any name works: ").strip()
        if name != "":
            return name
        print("WARNING: System Error - Name cannot be blank. Please enter a name.")


# --- the function is for choosing an organization, also future-me, use this as an example too --
def choose_organization():
    """Forces the player to pick a valid organization using a loop and string cleaning."""
    time.sleep(1.0)
    print_slow("\nNow, new fella - pick a group that fits you the most:", 2.0)
    print_slow("--------------------------------------------------------", 1.5)
    print_slow(" 1. [Agency] - I will protect my people. (Frontier-Spec)", 0.5)
    print_slow(" 2. [UNEC] - Humanity is where I belong. (Hard Sci-Fi)", 0.5)
    print_slow(" 3. [Independent] - I choose my own belief. (Explorer)", 0.5)
    print_slow("--------------------------------------------------------", 1.5)


    # Loop function - helps one to pick an option without crashing the program completely
    # Strings - .strip() removes random/accidental spaces, .lower () converts text to lower case for a easy comparison
    while True:
        # .strip() removes accidental spaces. .lower() converts text to lowercase.
        choice = input("Enter Organization Name or Number: ").strip().lower()
        
        if choice in ["1", "agency"]:
            return "Agency"
        elif choice in ["2", "unec", "united nation's expeditionary corp"]:
            return "UNEC"
        elif choice in ["3", "independent", "i find my way"]:
            return "Independent"
        if choice in ["sans", "skeleton", "H", "hermann", "Hermann"]:
            return "Hermann, of The General Directorate"
           
        if choice in ["J.C", "Jack", "Jack Cooper", 'jack cooper', "Coordinator", "coordinator", "pilot", "Pilot"]:
            return "J. Cooper, The Hero of Solora"

        # If the input is invalid, the loop continues instead of crashing or giving a default path
        print("⚠️ Unrecognized choice. This terminal needs a clear alignment. Pick again, will you?")

# --- MAIN GAME LOOP ---
boot_terminal()
player_name = get_player_name()
organization = choose_organization()

# Setup base stats and gear based on organization choice
if organization == "Agency":
    player_organization = "I will protect my people. (Agency)"
    equipped_gear = "Standard Vanguard Outfit, Frontier-Spec Assault Rifle"
    health = 110
    max_posture = 300
    print_slow("\nPersonnel Detected. Initializing Profile...", 1.5)
    print_slow("Welcome back, operative.", 1.0)

elif organization == "UNEC":
    player_organization = "Humanity is where I belong. (UNEC)"
    equipped_gear = "Magnetic Exo-suit, Standard Expedition Rifle"
    health = 150
    max_posture = 200
    print_slow("\nRerouting to Expedition Corp's mainframe...", 1.5)

else:
    player_organization = "I find my way. (Independent)"
    equipped_gear = "Personalized Weapon, Explorer's Kit, Grappling"
    health = 100
    max_posture = 100
    print_slow("\nDeactivating personal identity, rerouting from terminal...", 1.5)

# Special cases for specific inputs - "Cooper" and "Hermann", easters eggs to the main story of Season 1 where you get to play protagonists woo!!
if organization == "Hermann, of The General Directorate":
    pass
if get_player_name() == "Hermann" or get_player_name() == "hermann" or get_player_name() == "H" or get_player_name() == "h" or get_player_name() == "Sans" or get_player_name() == "skeleton" or get_player_name() == "skeleton guy":
    player_organization = "Hermann, of The General Directorate"
    equipped_gear = "Specialized Kit \"Alpha\", Experimental Tuned Relay Band"
    health = 200
    max_posture = 1000
    print_slow("\n\"Decrypting.. Accessed. Welcome, H.", 0.5)

    print_slow("░░░░░░░░██████████████████")
    print_slow("░░░░████░░░░░░░░░░░░░░░░░░████")
    print_slow("░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print_slow("░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print_slow("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print_slow("██░░░░░░░░░░░░░░░░░░░░██████░░░░██")
    print_slow("██░░░░░░░░░░░░░░░░░░░░██████░░░░██")
    print_slow("██░░░░██████░░░░██░░░░██████░░░░██")
    print_slow("░░██░░░░░░░░░░██████░░░░░░░░░░██")
    print_slow("████░░██░░░░░░░░░░░░░░░░░░██░░████")
    print_slow("██░░░░██████████████████████░░░░██")
    print_slow("██░░░░░░██░░██░░██░░██░░██░░░░░░██")
    print_slow("░░████░░░░██████████████░░░░████░░")
    print_slow("░░░░░░████░░░░░░░░░░░░░░████░░░░░░")
    print_slow("░░░░░░░░░░██████████████░░░░░░░░░░")

elif organization == "J. Cooper, The Hero of Solora":
    pass
elif get_player_name() == "Jack Cooper" or get_player_name() == "cooper" or get_player_name() == "J.C" or get_player_name() == "jack" or get_player_name() == "J. Cooper":
    player_organization = "J. Cooper, The Hero of Solora"
    equipped_gear = "SEO's Jumpkit and Coordinator Helmet, SERE's Kit, Storm's Blade"
    health = 500
    max_posture = 500
    print_slow("\nInitializing Profile... Welcome back, Cooper.", 0.9)


# Display the finalized profile, hell yeah - Final part of the example, the combat system will be done in another file
print("\n--- IDENTITY PROFILE FINALIZED ---")
print("--------------------------------------------------------")
print_slow(f"Identity: {player_name}", 0.5)
print_slow(f"Path/Organization: {player_organization}", 0.5)
print_slow(f"Equipment: {equipped_gear}", 0.5)
print_slow(f"Vitality (Health): {health}", 1.5)
print_slow(f"Stability (Posture): {max_posture}", 1.5)
print("--------------------------------------------------------")
