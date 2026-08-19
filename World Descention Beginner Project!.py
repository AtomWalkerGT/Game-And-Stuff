# --- Some World's Descention Prototype, fam ---
# Upgraded version with Loops, Functions, and String Methods
import time
import random

def print_slow(text, delay=1.0):
    """A custom function to print text and pause automatically to control pacing."""
    print(text)
    time.sleep(delay)

def boot_terminal():
    """Simulates the terminal activation sequence."""
    print_slow("--- Activating Terminal... ---", 1.0)
    print_slow(".....", 1.5)
    print_slow("....", 0.5)
    print_slow("...", 0.4)
    print_slow("--- Terminal Activated, opening... ---", 1.0)
    print_slow("--- Welcome to World's Descention First Project! Made by yours truly, Cooper ---", 2.0)

def get_player_name():
    """Gets the player name and ensures it isn't blank."""
    while True:
        time.sleep(1.0)
        name = input("\nType (or just write) in your name in the terminal, and any name works: ").strip()
        if name != "":
            return name
        print("WARNING: System Error - Name cannot be blank. Please enter a name.")

def choose_faction():
    """Forces the player to pick a valid organization using a loop and string cleaning."""
    time.sleep(1.0)
    print_slow("\nNow, new fella - pick a group that fits you the most:", 2.0)
    print_slow("--------------------------------------------------------", 1.5)
    print_slow(" 1. [Agency] - I will protect my people. (Frontier-Spec)", 0.5)
    print_slow(" 2. [UNEC] - Humanity is where I belong. (Hard Sci-Fi)", 0.5)
    print_slow(" 3. [Independent] - I choose my own belief. (Explorer)", 0.5)
    print_slow("--------------------------------------------------------", 1.5)
    
    while True:
        # .strip() removes accidental spaces. .lower() converts text to lowercase.
        choice = input("Enter Organization Name or Number: ").strip().lower()
        
        if choice in ["1", "agency"]:
            return "Agency"
        elif choice in ["2", "unec", "united nation's expeditionary corp"]:
            return "UNEC"
        elif choice in ["3", "independent", "i find my way"]:
            return "Independent"
        
        # If the input is invalid, the loop continues instead of crashing or giving a default path
        print("⚠️ Unrecognized choice. The terminal needs a clear alignment. Pick again, will you?")

# --- MAIN GAME LOOP ---
boot_terminal()
player_name = get_player_name()
faction = choose_faction()

# Setup base stats and gear based on faction choice
if faction == "Agency":
    player_organization = "I will protect my people. (Agency)"
    equipped_gear = "Standard Vanguard Outfit, Frontier-Spec Assault Rifle"
    health = 110
    max_posture = 300
    print_slow("\nPersonnel Detected. Initializing Profile...", 1.5)
    print_slow("Welcome back, operative.", 1.0)

elif faction == "UNEC":
    player_organization = "Humanity is where I belong. (UNEC)"
    equipped_gear = "Magnetic Exo-suit, Standard Expedition Rifle"
    health = 150
    max_posture = 200
    print_slow("\nRerouting to Expedition Corp's mainframe...", 1.5)

else:
    player_organization = "I find my way. (Independent)"
    equipped_gear = "Personalized Weapon, Explorer's Kit"
    health = 100
    max_posture = 100
    print_slow("\nDeactivating personal identity, rerouting from terminal...", 1.5)

# Display finalized profile
print("\n--- IDENTITY PROFILE FINALIZED ---")
print("--------------------------------------------------------")
print_slow(f"Identity: {player_name}", 0.5)
print_slow(f"Path/Organization: {player_organization}", 0.5)
print_slow(f"Equipment: {equipped_gear}", 0.5)
print_slow(f"Vitality (Health): {health}", 1.5)
print_slow(f"Stability (Posture): {max_posture}", 1.5)
print("--------------------------------------------------------")
