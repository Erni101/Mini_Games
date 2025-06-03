# main.py

from Clases.Civilization import Civilization

def main():
    # Create an instance of Civilization
    civilization_name = input("Enter the name of your civilization: ")
    initial_resources = 100
    initial_units = []
    
    civilization = Civilization(civilization_name, initial_resources, initial_units)

    print(civilization)

    # Game loop
    while True:
        action = input("Choose an action: (train/collect/exit): ").strip().lower()
        
        if action == "train":
            unit_type = input("Enter unit type to train (Archer, Cavalry, Infantry, Worker): ").strip()
            civilization.train_unit(unit_type)
            print(civilization)
        
        elif action == "collect":
            resources_collected = civilization.collect_resources()
            print(f"Resources after collection: {resources_collected}")
        
        elif action == "exit":
            print("Exiting the game.")
            break
        
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()