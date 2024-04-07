import random
from faker import Faker
fake = Faker()

class CharacterGenerator:
    jobs = [
        "detective", "scientist", "mage", "astronaut", "test pilot", "software engineer"
    ]
    traits = [
        "disgraced", "brave", "curious", "cunning", "loyal", "reckless", "wise", "compassionate", "arrogant", "mysterious", "resourceful", "stoic", "charismatic", "melancholic"
    ]

    villain_traits = [
        "disgraced", "greedy", "power hungry", "amoral", "vengeful", "trecherous", "vain", "corrupt", "bloodthirsty", "murderous"
    ]

    def __init__(self, role):
        self.role = role
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.job = random.choice(self.jobs)
        self.trait = random.choice(self.traits if role != 'antagonist' else self.villain_traits)
        self.full_name = f"{self.first_name} {self.last_name}"
        self.description = f"{self.trait} {self.job}"

    def __str__(self):
        return f"{self.full_name}, a {self.description}"