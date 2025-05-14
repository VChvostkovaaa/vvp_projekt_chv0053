import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mujbalik.simulation import run_simulation


def run_timestep_experiment(csv_path: str = 'data/planets.csv',
                            n_steps: int = 365) -> None:
    """
    Spustí simulaci pro různé časové kroky a pro každé vykreslí výsledné dráhy planet.

    Args:
        csv_path (str): cesta k CSV souboru s planetami
        n_steps (int): počet kroků simulace
    """
    # načtení dat ze .csv souboru
    df: pd.DataFrame = pd.read_csv(csv_path)
    positions_init: np.ndarray = df[['position_x', 'position_y']].to_numpy()
    velocities_init: np.ndarray = df[['velocity_x', 'velocity_y']].to_numpy()
    masses: np.ndarray = df['mass'].to_numpy()

    # různé hodnoty dt
    dt_values: dict[str, int] = {
        '1 hour': 60 * 60,
        '1 day': 60 * 60 * 24,
        '1 week': 60 * 60 * 24 * 7,
        '1 month': 60 * 60 * 24 * 30,
    }

    for label, dt in dt_values.items():

        # zkopíruj počáteční podmínky pro každou simulaci
        positions: np.ndarray = positions_init.copy()
        velocities: np.ndarray = velocities_init.copy()

        history: np.ndarray = run_simulation(
            positions, velocities, masses, dt, n_steps)

        # vykresli výsledky
        plt.figure(figsize=(6, 6))
        for i in range(len(history)):
            plt.plot(history[i][:, 0], history[i]
                     [:, 1], label=df['name'].iloc[i])

        plt.title(f'Dráhy planet s dt = {label}')
        plt.xlabel('x position')
        plt.ylabel('y position')
        plt.legend()
        plt.axis('equal')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
