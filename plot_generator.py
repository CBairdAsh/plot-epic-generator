from .character_generator import CharacterGenerator
import random
from faker import Faker
fake = Faker()

class PlotGenerator:
    objectives = [
        "uncover the truth behind {event}",
        "find the legendary {artifact}"
    ]
    locations = [
        "in the ruins of an ancient civilization beneath {place}",
        "within the labyrinthine {structure}"
    ]
    complications = [
        "but must first decrypt a {age} manuscript",
        "but is hindered by a rival's {curse}"
    ]
    conflicts = [
        "while evading a secretive order determined to keep {secret} hidden",
        "while confronting their own {personal_issue}",
        "antagonist"
    ]

    @staticmethod
    def generate_objective(cls):
        event = fake.word(ext_word_list=['city\'s sudden disappearance', 'ancient prophecy', 'king\'s assassination'])
        artifact = fake.word(ext_word_list=['Staff of Zalmoxis', 'Crown of Atlantis', 'Sword of Destiny'])
        return random.choice(cls.objectives).format(event=event, artifact=artifact)

    @staticmethod
    def generate_location(cls):
        place = fake.word(ext_word_list=['Antarctica', 'the Amazon jungle', 'the Sahara desert'])
        structure = fake.word(ext_word_list=['Library of Echoes', 'Tower of Shadows', 'Dungeon of Secrets'])
        return random.choice(cls.locations).format(place=place, structure=structure)

    @staticmethod
    def generate_complication(cls):
        age = fake.word(ext_word_list=['century-old', 'millennium-old', 'decade-old'])
        curse = fake.word(ext_word_list=['curse', 'spell', 'hex'])
        return random.choice(cls.complications).format(age=age, curse=curse)

    @staticmethod
    def generate_conflict(cls):
        secret = fake.word(ext_word_list=['city\'s secrets', 'ancient magic', 'forbidden knowledge'])
        personal_issue = fake.word(ext_word_list=['dark past', 'forgotten sin', 'hidden shame'])
        return random.choice(cls.conflicts).format(secret=secret, personal_issue=personal_issue)

    @staticmethod
    def generate_character(role):
        return CharacterGenerator(role)

    @staticmethod
    def generate_antagonist():
        antagonist = CharacterGenerator("antagonist")
        antagonist.nature = "person"
        return antagonist

    @classmethod
    def generate_plot(cls):
        hero = cls.generate_character("hero")
        antagonist = cls.generate_antagonist()

        objective = cls.generate_objective(cls)
        location = cls.generate_location(cls)
        complication = cls.generate_complication(cls)
        conflict = cls.generate_conflict(cls)

        conflict_description = str(conflict)
        if conflict == "antagonist":
            conflict_description = str(antagonist)

        premise = f"Premise: the hero, {str(hero)}, must {objective} at or in {location} {complication} while confronting {conflict_description}.\n"

        rival_info = "\n"
        if "rival" in complication:
            rival = cls.generate_antagonist()
            rival_info += f"The rival is {str(rival)}.\n\n"
        
        plot_summary = premise + rival_info
        plot_summary += "Plot Summary and Beats:\n"
        plot_summary += f"1. Introduction: {hero.full_name} faces a challenge...\n"
        plot_summary += f"2. Complication: Despite {hero.full_name}'s efforts...\n"
        plot_summary += "3. Revelation: A new discovery leads to...\n"
        plot_summary += "4. Climax: In a final confrontation...\n"

        return plot_summary