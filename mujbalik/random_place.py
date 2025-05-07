import numpy as np

def generate_random_scenario(number_of_bodies, position_range, velocity_range, mass_range):
    """
    Funkce generuje náhodné scénáře pro simulaci, která bude náhodně generovat počáteční podmínky planet (polohy, rychlosti a hmotnosti)
    pro daný počet planet.


    Args:
        number_of_bodies: kolik planet chci vygenerovat
        position_range: dvojice čísel (min, max) pro generování pozic planet
        velocity_range: dvojice čísel (min, max) pro generování rychlostí planet
        mass_range: dvojice čísel (min, max) pro generování hmotností planet

    Returns:
        names: seznam názvů těles
        positions: numpy pole s pozicemi planet
        velocities: numpy pole s rychlostmi planet
        masses: numpy pole s hmotnostmi planet

    """
    # generování názvů těles podle pořadí
    names = [f"Planetka {i + 1}" for i in range(number_of_bodies)]

    # generování náhodných pozic planet
    positions = np.random.uniform(low = position_range[0], high = position_range[1], size = (number_of_bodies, 2))
    
    # generování náhodných rychlostí planet
    velocities = np.random.uniform(low = velocity_range[0], high = velocity_range[1], size = (number_of_bodies, 2))
    
    # generování náhodných hmotností planet
    masses = np.random.uniform(low = mass_range[0], high = mass_range[1], size = (number_of_bodies, 1))
    
    return names, positions, velocities, masses
