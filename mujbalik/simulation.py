from .physics import compute_accelerations
import numpy as np

def run_simulation(positions, velocities, masses, dt, numbers_of_steps):
    """
    Tahle funkce spouští simulaci pohybu planet na zadaný počet kroků. Spočítá, jak se planety hýbou podle gravitace.

    Args:
        positions: počateční pozice planet
        velocities: počáteční rychlosti planet
        masses: hmotnosti planet
        dt: časové kroky
        numbers_of_steps: kolik kroků má simulace udělat

    Returns:
        history: seznam pozic všech planet v každém kroku simulace
    """
    numbers_planets = len(positions)
    
    # pro ukládání pozic každé planety v každém kroku simulace
    history = [[] for steps in range(numbers_planets)]


    for steps in range(numbers_of_steps):
        # spočítám zrychlení pro každou planetu
        acc = compute_accelerations(positions, masses)

        velocities += acc * dt                          # v = v + a⋅Δt; aktualizace rychlosti
        positions += velocities * dt                    # x = x + v⋅Δt; aktualizce pozice

        # uložení pozicí do historie
        for i in range(numbers_planets):
            history[i].append(positions[i].copy())

    # převedeme historii na numpy array pro každou planetu
    history = np.array([np.array(h) for h in history])
    return history
