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
    print("--- Activating Terminal... ---")
    print(".....")
    print("....")
    print("...")
    print("--- Terminal Activated, opening... ---")
    print("--- Welcome to World's Descention First Project! Made by yours truly, Cooper ---")

# --- the function is for names, future-me, use this as an example lmao --
def get_player_name():
    """Gets the player name and ensures it isn't blank."""
    while True:
        time.sleep(0.5)
        name = input("\nType (or just write) in your name in the terminal, and any name works: ").strip()
        if name != "":
            return name
        print("WARNING: System Error - Name cannot be blank. Please enter a name.")


# --- the function is for choosing an organization, also future-me, use this as an example too --
def choose_organization():
    """Forces the player to pick a valid organization using a loop and string cleaning."""
    time.sleep(0.5)
    print("\nNow, new fella - pick a group that fits you the most:")
    print("--------------------------------------------------------")
    print(" 1. [Agency] - I will protect my people. (Frontier-Spec)")
    print(" 2. [UNEC] - Humanity is where I belong. (Hard Sci-Fi)")
    print(" 3. [Independent] - I choose my own belief. (Explorer)")
    print("--------------------------------------------------------")


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
            return "Renato H, The Red Wake of The General Directorate"
           
        if choice in ["J.C", "Jack", "Jack Cooper", 'jack cooper', "Coordinator", "coordinator", "pilot", "Pilot"]:
            return "J. Cooper, The Hero of Solora"

        # If the input is invalid, the loop continues instead of crashing or giving a default path
        print("⚠️ Unrecognized choice. This terminal needs a clear alignment. Pick again, will you?")

# --- MAIN LOOP --- 
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
if organization == "Renato H, The Red Wake of The General Directorate":
    pass
if player_name.lower() in ["Hermann", "hermann", "H", "h", "Sans", "skeleton", "skeleton guy"]:
    player_organization = "Renato H, The Red Wake of The General Directorate"
    equipped_gear = "Specialized Kit \"Alpha\", Experimental Tuned Relay Band"
    health = 200
    max_posture = 1000
    print("\n\"Decrypting.. Accessed. Welcome back, Renato.")

    print("░░░░░░░░██████████████████")
    print("░░░░████░░░░░░░░░░░░░░░░░░████")
    print("░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("██░░░░░░░░░░░░░░░░░░░░██████░░░░██")
    print("██░░░░░░░░░░░░░░░░░░░░██████░░░░██")
    print("██░░░░██████░░░░██░░░░██████░░░░██")
    print("░░██░░░░░░░░░░██████░░░░░░░░░░██")
    print("████░░██░░░░░░░░░░░░░░░░░░██░░████")
    print("██░░░░██████████████████████░░░░██")
    print("██░░░░░░██░░██░░██░░██░░██░░░░░░██")
    print("░░████░░░░██████████████░░░░████░░")
    print("░░░░░░████░░░░░░░░░░░░░░████░░░░░░")
    print("░░░░░░░░░░██████████████░░░░░░░░░░")

elif organization == "J. Cooper, The Hero of Solora":
    pass
elif player_name.lower() in ["jack cooper", "cooper", "j.c", "jack", "j. cooper"]:
    player_organization = "J. Cooper, The Hero of Solora"
    equipped_gear = "SEO's Jumpkit and Coordinator Helmet, SERE's Kit, Storm's Blade"
    health = 500
    max_posture = 500
    print_slow("\nInitializing Profile... Welcome back, Coordinator Cooper.", 0.9)

# Additional: player_name.lower() helps input with "case-insenstivity", so "cooper", "Cooper" works the same - "in" function checks if it's a valid name



# Display the finalized profile, hell yeah - Final part of the example, the combat system will be done in another file
print("\n--- IDENTITY PROFILE FINALIZED ---")
print("--------------------------------------------------------")
print(f"Identity: {player_name}")
print(f"Path/Organization: {player_organization}")
print(f"Equipment: {equipped_gear}")
print(f"Vitality (Health): {health}")
print(f"Stability (Posture): {max_posture}")
print("--------------------------------------------------------")
