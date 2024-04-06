import random

# Example databases/lists for each element
first_names = ["Alice", "Bob", "Cassandra", "David"]
last_names = ["Smith", "Johnson", "Doe", "Brown"]
jobs = ["detective", "scientist", "mage", "astronaut", "test pilot", "software engineer"]
traits = ["disgraced", "brave", "curious"]
objectives = ["uncover the truth behind the city's sudden disappearance", "find the legendary Staff of Zalmoxis"]
locations = ["in the ruins of an ancient civilization beneath Antarctica", "within the labyrinthine Library of Echoes"]
complications = ["but must first decrypt a century-old manuscript", "but is hindered by a rival's curse"]
conflicts = ["while evading a secretive order determined to keep the city's secrets hidden", "while confronting their own dark past", "antagonist"]

def generate_character(role):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    job = random.choice(jobs)
    trait = random.choice(traits)
    # Return a dictionary with all character details
    return {
        "role": role,
        "first_name": first_name,
        "last_name": last_name,
        "trait": trait,
        "job": job,
        "full_name": f"{first_name} {last_name}",
        "description": f"{trait} {job}"
    }

def generate_antagonist():
    description = random.choice(conflicts)
    if description == 'antagonist':
        # Generate a villain character
        villain = generate_character("villain")
        villain["nature"] = "person"
        villain["description"] = f"{villain['trait']} {villain['job']}"
        return villain
    else:
        # Non-person antagonist
        return {
            "nature": "force", 
            "description": description, 
            "full_name": ""
        }

def generate_plot():
    hero = generate_character("hero")
    antagonist = generate_antagonist()

    objective = random.choice(objectives)
    location = random.choice(locations)
    complication = random.choice(complications)
    conflict = antagonist["description"] 
    if antagonist["nature"] == "person": 
        conflict = f"{antagonist["full_name"]}, who is a {antagonist["description"]}"
                
    # Use full description only in the premise
    premise = f"Premise: the {hero['role']}, {hero['full_name']} who is a {hero['description']}, must {objective} at or in {location} {complication} while confronting {conflict}.\n"
    plot_summary = premise + "Plot Summary and Beats:\n"
    plot_summary += f"1. Introduction: {hero['full_name']} faces a challenge...\n"
    plot_summary += f"2. Complication: Despite {hero['full_name']}'s efforts...\n"
    plot_summary += "3. Revelation: A new discovery leads to...\n"
    plot_summary += "4. Climax: In a final confrontation...\n"

    return plot_summary

# Example usage
print(generate_plot())
