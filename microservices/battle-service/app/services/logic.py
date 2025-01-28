import random

def determine_winner(hero, villain):
    """Compare hero and villain attributes to determine the winner."""
    
    hero_power = len(hero.get("power", "")) * 2  # Example metric
    villain_power = len(villain.get("evil_power", "")) * 2  # Example metric

    if hero_power > villain_power:
        return hero["name"], f"{hero['name']} wins with superior power!"
    elif villain_power > hero_power:
        return villain["name"], f"{villain['name']} wins with a stronger attack!"
    else:
        winner = random.choice([hero["name"], villain["name"]])
        return winner, f"It was a close fight, but {winner} won!"
