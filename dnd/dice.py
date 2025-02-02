import random


def dice_roller(num_dice, sides_per_die):
    """
    Simulates rolling dice for D&D.

    Args:
        num_dice: The number of dice to roll (e.g., 3 for 3d6).
        sides_per_die: The number of sides each die has (e.g., 6 for 3d6).

    Returns:
        A tuple containing:
            - A list of the individual rolls.
            - The total sum of the rolls.
    """

    if not isinstance(num_dice, int) or num_dice <= 0:
        raise ValueError("Number of dice must be a positive integer.")

    if not isinstance(sides_per_die, int) or sides_per_die <= 0:
        raise ValueError("Number of sides must be a positive integer.")


    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, sides_per_die)
        rolls.append(roll)

    total = sum(rolls)
    return rolls, total



# Examples
try:
    rolls, total = dice_roller(3, 6)  # 3d6
    print(f"Rolls: {rolls}, Total: {total}")

    rolls, total = dice_roller(2, 10) # 2d10
    print(f"Rolls: {rolls}, Total: {total}")

    rolls, total = dice_roller(1, 20) # 1d20
    print(f"Rolls: {rolls}, Total: {total}")

    rolls, total = dice_roller(4, 4) # 4d4
    print(f"Rolls: {rolls}, Total: {total}")

    # Example of error handling
    #rolls, total = dice_roller(-1, 6)  # This will raise a ValueError
    #print(f"Rolls: {rolls}, Total: {total}")

except ValueError as e:
    print(f"Error: {e}")


def generate_attribute():
    """Generates a single character attribute using 4d6 drop lowest."""

    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))  # Remove the lowest roll
    # rolls.remove(min(rolls))  # remove the second lowest
    return rolls, sum(rolls)


def generate_character_attributes():
    """Generates all character attributes."""

    attributes = {
        "Strength": None,
        "Dexterity": None,
        "Constitution": None,
        "Intelligence": None,
        "Wisdom": None,
        "Charisma": None,
    }

    for attribute_name in attributes:
        rolls, total = generate_attribute()
        attributes[attribute_name] = {"rolls": rolls, "total": total}

    return attributes
