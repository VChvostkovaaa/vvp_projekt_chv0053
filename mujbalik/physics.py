import numpy as np

G = 6.674e-11   # gravitační konstanta [m^3 kg^-1 s^-2]


def compute_accelerations(positions: np.ndarray,
                          masses: np.ndarray) -> np.ndarray:
    """
    Vypočítá celkové gravitační zrychlení způsobeného gravitační silou mezi všemi dvojcemi planet

    Args:
        positions (np.ndarray): pozice planety v 2D prostoru (posicion_x, position_y)
        masses (np.ndarray): hmotnost planet

    Returns:
        acceleration (np.ndarray): zrychlení každé planty s ostatními plametami v 2D prostoru
    """
    number_of_planets: int = len(positions)
    acceleration: np.ndarray = np.zeros_like(positions)
    # vytvoří nové pole plných nul stejného tvaru jako positions
    # protože neznáme žádné zrychnení -> inicializujeme na nuly -> podtupně budeme ukládat výsledky

    # pro každou dvojici planet spočítáme gravitační zrychlení (planet_1, planet_2)
    for planet_1 in range(number_of_planets):
        for planet_2 in range(number_of_planets):
            if planet_1 != planet_2:        # planeta se nepřitahuje sama sebou
                # směrový vektor
                direction_vector: np.ndarray = positions[planet_2] - \
                    positions[planet_1]
                # vzdalenost mezi planetami
                distance: float = np.linalg.norm(direction_vector)

                # aby jsem se vyhnul dělení nulou
                if distance != 0:
                    # přičteme vysledelné zrychlení k planetě 1
                    acceleration[planet_1] += G * masses[planet_2] * \
                        direction_vector / distance**3

    return acceleration
