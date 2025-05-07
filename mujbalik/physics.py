import numpy as np

G = 6.674e-11   # gravitační konstanta [m^3 kg^-1 s^-2]

def compute_accelerations(positions, masses):
    """
    Vypočítá celkové gravitační zrychlení způsobeného gravitační silou mezi všemi dvojcemi planet

    Args:
        positions: pozice planety v 2D prostoru (posicion_x, position_y)
        masses: hmotnost planet

    Returns:
        acceleration: zrychlení každé planty s ostatními plametami v 2D prostoru
    """
    number_of_planets = len(positions)
    acceleration = np.zeros_like(positions)
        # vytvoří nové pole plných nul stejného tvaru jako positions
        # protože neznáme žádné zrychnení -> inicializujeme na nuly -> podtupně budeme ukládat výsledky

    # pro každou dvojici planet spočítáme gravitační zrychlení (planet_1, planet_2)
    for planet_1 in range(number_of_planets):
        for planet_2 in range(number_of_planets):
            if planet_1 != planet_2:        # planeta se nepřitahuje sama sebou
                direction_vector = positions[planet_2] - positions[planet_1]    # směrový vektor
                distance = np.linalg.norm(direction_vector)            # vzdalenost mezi planetami

                # aby jsem se vyhnul dělení nulou
                if distance != 0:
                    # přičteme vysledelné zrychlení k planetě 1
                    acceleration[planet_1] += G * masses[planet_2] * direction_vector / distance**3

    return acceleration


