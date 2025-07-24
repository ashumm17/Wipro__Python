import random

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}


print("Original facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

print("\n")


new_facts = ["Is afraid of heights.", "Loves climbing.", "Is afraid of spiders."]
people_facts["Jeff"] = random.choice(new_facts)


people_facts["Jill"] = "Can hula dance."


print("Updated facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
