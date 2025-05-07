import pandas as pd
import matplotlib.pyplot as plt
from mujbalik.simulation import run_simulation

def run_timestep_experiment(csv_path = 'data/planets.csv', n_steps = 365):
    """
    Spustí simulaci pro různé časové kroky a pro každé vykreslí výsledné dráhy planet.

    Args:
        csv_path: cesta k CSV souboru s planetami
        n_steps: počet kroků simulace
    """
    # načtení dat ze .csv souboru
    df = pd.read_csv(csv_path)
    positions_init = df[['position_x', 'position_y']].to_numpy()
    velocities_init = df[['velocity_x', 'velocity_y']].to_numpy()
    masses = df['mass'].to_numpy()

    # různé hodnoty dt
    dt_values = {
        '1 hour': 60 * 60,
        '1 day': 60 * 60 * 24,
        '1 week': 60 * 60 * 24 * 7,
        '1 month': 60 * 60 * 24 * 30,
    }

    for label, dt in dt_values.items():

        # zkopíruj počáteční podmínky pro každou simulaci
        positions = positions_init.copy()
        velocities = velocities_init.copy()

        history = run_simulation(positions, velocities, masses, dt, n_steps)

        # vykresli výsledky
        plt.figure(figsize=(6, 6))
        for i in range(len(history)):
            plt.plot(history[i][:, 0], history[i][:, 1], label=df['name'].iloc[i])


        plt.title(f'Dráhy planet s dt = {label}')
        plt.xlabel('x position')
        plt.ylabel('y position')
        plt.legend()
        plt.axis('equal')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
