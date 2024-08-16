
class Character:
    def __init__(self, name, vocation):
        self.name = name
        self.vocation = vocation
        self.inventory = []
        self.journal = []
        self.rewards = 0
        self.blacklist = ["steal", "cheat"]

    def receive_work_order(self, work_order):
        self.journal.append(work_order)
        print(f"{self.name} received a work order: {work_order}")

    def complete_work_order(self, work_order):
        if work_order in self.journal:
            self.journal.remove(work_order)
            self.inventory.append(f"Reward for {work_order}")
            self.rewards += 1
            print(f"{self.name} completed the work order: {work_order}")
            print(f"{self.name} received a reward. Total rewards: {self.rewards}")
        else:
            print(f"{self.name} does not have the work order: {work_order}")

    def perform_action(self, action):
        if action in self.blacklist:
            print(f"Action '{action}' is not allowed!")
        else:
            print(f"{self.name} performed the action: {action}")

class Township:
    def __init__(self):
        self.workplaces = {
            "blacksmith": "Forge and create tools",
            "library": "Research and write books",
            "farm": "Grow and harvest crops"
        }

    def list_workplaces(self):
        for place, description in self.workplaces.items():
            print(f"{place.capitalize()}: {description}")

# Example usage
township = Township()
character = Character(name="Alex", vocation="Blacksmith")

township.list_workplaces()
character.receive_work_order("Forge a sword")
character.complete_work_order("Forge a sword")
character.perform_action("steal")
character.perform_action("read a book")

# Transcript the event
print("\n--- Transcript ---")
print(f"Character: {character.name}")
print(f"Vocation: {character.vocation}")
print(f"Inventory: {character.inventory}")
print(f"Journal: {character.journal}")
print(f"Rewards: {character.rewards}")
