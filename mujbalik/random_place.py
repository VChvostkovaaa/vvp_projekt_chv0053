import numpy as np
from typing import Tuple, List


def generate_random_scenario(number_of_bodies: int,
                             position_range: Tuple[float, float],
                             velocity_range: Tuple[float, float],
                             mass_range: Tuple[float, float]) \
        -> Tuple[List[str], np.ndarray, np.ndarray, np.ndarray]:
    """
    Funkce generuje náhodné scénáře pro simulaci, která bude náhodně generovat počáteční podmínky planet (polohy, rychlosti a hmotnosti)
    pro daný počet planet.

    Args:
        number_of_bodies (int): kolik planet chci vygenerovat
        position_range (Tuple[float, float]): dvojice čísel (min, max) pro generování pozic planet
        velocity_range (Tuple[float, float]): dvojice čísel (min, max) pro generování rychlostí planet
        mass_range (Tuple[float, float])): dvojice čísel (min, max) pro generování hmotností planet

    Returns:
        names (List[str]): seznam názvů těles
        positions (Tuple[float, float]): numpy pole s pozicemi planet
        velocities (Tuple[float, float]): numpy pole s rychlostmi planet
        masses (Tuple[float, float]): numpy pole s hmotnostmi planet

    """
    # generování názvů těles podle pořadí
    names: List[str] = [f"Planetka {i + 1}" for i in range(number_of_bodies)]

    # generování náhodných pozic planet
    positions: np.ndarray = np.random.uniform(
        low=position_range[0], high=position_range[1], size=(number_of_bodies, 2))

    # generování náhodných rychlostí planet
    velocities: np.ndarray = np.random.uniform(
        low=velocity_range[0], high=velocity_range[1], size=(number_of_bodies, 2))

    # generování náhodných hmotností planet
    masses: np.ndarray = np.random.uniform(
        low=mass_range[0], high=mass_range[1], size=(number_of_bodies, 1))

    return names, positions, velocities, masses
