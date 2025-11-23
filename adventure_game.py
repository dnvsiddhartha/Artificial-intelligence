# To build an adventure game using Python
print("hello")

def start_game() -> tuple[str, str]:
    """Show intro, prompt for player's name and an initial choice (forest or cave).

    Returns:
        (player_name, choice) where choice is 'forest' or 'cave'
    """
    print("Welcome to the Adventure Game!")
    print("You wake up at the edge of a mysterious land filled with dangers and wonders.")

    name = input("Enter your name: ").strip()
    if not name:
        name = "Adventurer"
    print(f"\nWelcome, {name}!\n")

    print("Your first choice:")
    print("  1) Explore the forest")
    print("  2) Enter the cave")

    valid_map = {"1": "forest", "2": "cave", "forest": "forest", "cave": "cave"}
    choice = None
    while choice not in ("forest", "cave"):
        resp = input("Choose 1 or 2 (or type 'forest' or 'cave'): ").strip().lower()
        choice = valid_map.get(resp)
        if choice is None:
            print("Please enter 1 or 2, or 'forest' or 'cave'.")

    print(f"\nYou chose to {choice}. Let the adventure begin, {name}!\n")
    return name, choice

def forest_path(player_name: str):
    """Describe the forest scenario and present two choices.

    Choices:
      1) Follow the river -> 'river'
      2) Climb a tree   -> 'tree'

    Uses an if-else structure to handle the player's decision.
    Returns the chosen path as a string.
    """
    print("You step into the forest. The canopy is dense and the air smells of pine.")
    print("Not far ahead you hear a babbling river; a tall tree stands nearby with low branches.")

    print("What will you do?")
    print("  1) Follow the river")
    print("  2) Climb the tree")

    choice = None
    while choice not in ("river", "tree"):
        resp = input("Choose 1 or 2 (or type 'river' or 'tree'): ").strip().lower()
        if resp in ("1", "river", "follow", "follow river"):
            choice = "river"
        elif resp in ("2", "tree", "climb", "climb tree"):
            choice = "tree"
        else:
            print("Please enter 1 or 2, or 'river' or 'tree'.")

    if choice == "river":
        print(f"\n{player_name}, you follow the river downstream. The water leads you to a peaceful clearing and a small wooden boat.")
        print("You can choose to rest by the water or use the boat to cross to the other side.")
    else:
        print(f"\n{player_name}, you climb the tree. From the top you can see the surrounding land — a faint trail leads toward a distant ruin.")
        print("You spot movement below but it's unclear what it is; your vantage point keeps you safe for now.")

    return choice


def cave_path(player_name: str):
    """Describe the cave scenario and present two choices.

    Choices:
      1) light a torch -> 'torch'
      2) proceed in the dark -> 'dark'

    Uses an if-else structure to handle the player's decision.
    Returns the chosen path as a string.
    """
    print("You enter a dark cave. The walls are damp and you can hear distant echoes.")
    print("What will you do?")
    print("  1) Light a torch")
    print("  2) Proceed in the dark")

    choice = None
    while choice not in ("torch", "dark"):
        resp = input("Choose 1 or 2 (or type 'torch' or 'dark'): ").strip().lower()
        if resp in ("1", "torch", "light", "light the torch"):
            choice = "torch"
        elif resp in ("2", "dark", "proceed", "proceed in the dark", "proceed in dark"):
            choice = "dark"
        else:
            print("Please enter 1 or 2, or 'torch' or 'dark'.")

    if choice == "torch":
        print(f"\n{player_name}, you light a torch and the cave reveals ancient carvings and a safe path forward.")
    else:
        print(f"\n{player_name}, you proceed in the dark and carefully feel your way forward, narrowly avoiding a hidden drop.")

    return choice

def play_once():
    """Run a single playthrough: start_game and follow the chosen path.

    Returns True if the playthrough completed normally.
    """
    player_name, first_choice = start_game()
    if first_choice == "forest":
        forest_path(player_name)
    else:
        # If cave_path is implemented, call it; otherwise show a message.
        try:
            cave_path(player_name)
        except NameError:
            print("\nCave path handler not found (cave_path is not defined). Please implement `cave_path(player_name)`.")
    return True


if __name__ == "__main__":
    while True:
        try:
            play_once()
        except KeyboardInterrupt:
            print("\nReceived interrupt. Exiting game.")
            break

        # Ask whether to restart
        resp = input("Would you like to play again? (y/n): ").strip().lower()
        if resp not in ("y", "yes"):
            print("Thanks for playing — goodbye!")
            break