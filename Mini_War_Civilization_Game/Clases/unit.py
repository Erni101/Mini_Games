class Archer:
    def __init__(self, name: str):
        self.name = name
        self.unit_type = "Archer"
        self.hp = 100  # Example health points
        self.attack_power = 15  # Example attack power

    def collect(self):
        return 0  # Archers do not collect resources

class Cavalry:
    def __init__(self, name: str):
        self.name = name
        self.unit_type = "Cavalry"
        self.hp = 120  # Example health points
        self.attack_power = 20  # Example attack power

    def collect(self):
        return 0  # Cavalry do not collect resources

class Infantry:
    def __init__(self, name: str):
        self.name = name
        self.unit_type = "Infantry"
        self.hp = 150  # Example health points
        self.attack_power = 10  # Example attack power

    def collect(self):
        return 0  # Infantry do not collect resources

class Worker:
    def __init__(self, name: str):
        self.name = name
        self.unit_type = "Worker"
        self.hp = 80  # Example health points
        self.collecting_power = 10  # Example resource collection power

    def collect(self):
        return self.collecting_power  # Workers collect resources based on their power