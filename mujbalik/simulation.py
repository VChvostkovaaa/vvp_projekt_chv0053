from .physics import compute_accelerations
import numpy as np


def run_simulation(positions: np.ndarray,
                   velocities: np.ndarray,
                   masses: np.ndarray,
                   dt: int,
                   numbers_of_steps: int) -> np.ndarray:
    """
    Tahle funkce spouští simulaci pohybu planet na zadaný počet kroků. Spočítá, jak se planety hýbou podle gravitace.

    Args:
        positions (np.ndarray): počateční pozice planet
        velocities (np.ndarray): počáteční rychlosti planet
        masses (np.ndarray): hmotnosti planet
        dt (int): časové kroky
        numbers_of_steps (int): kolik kroků má simulace udělat

    Returns:
        history (np.ndarray): seznam pozic všech planet v každém kroku simulace
    """
    numbers_planets: int = len(positions)

    # pro ukládání pozic každé planety v každém kroku simulace
    history: list[list[np.ndarray]] = [[] for steps in range(numbers_planets)]

    for steps in range(numbers_of_steps):
        # spočítám zrychlení pro každou planetu
        acc: np.ndarray = compute_accelerations(positions, masses)

        # v = v + a⋅Δt; aktualizace rychlosti
        velocities += acc * dt
        # x = x + v⋅Δt; aktualizce pozice
        positions += velocities * dt

        # uložení pozicí do historie
        for i in range(numbers_planets):
            history[i].append(positions[i].copy())

    # převedeme historii na numpy array pro každou planetu
    history: np.ndarray = np.array([np.array(h) for h in history])
    return history
