import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import HTML
from typing import List, Tuple, Optional, Union


def create_animation(history: List[np.ndarray],
                     names: List[str],
                     figsize: Tuple[float, float] = (8, 8),
                     zoom: float = 4.79e+12,
                     save_path=None) -> Union[None, HTML]:
    """
    vytvoří animaci na základě historie pozit všech planet.

    Args:
        history (List[mp.ndarray): historie pozic planet
        names (List[str]): jména planet
        figsize (Tuple[float, float]): velikost okna obrázku
        zoom (float): vzdalenost zoomu
        save_path (Optional[str]): cesta k souboru, ke ho budeme chtít uložt

    Returns:
        Union[HTML, None]: Vrací HTML animaci, pokud není zadán save_path, jinak None.
    """
    fig, ax = plt.subplots(figsize=figsize)
    colors = plt.cm.tab10.colors  # přednastavené barvy z matplotlibu
    number_of_planets: int = len(history)

    # Vytvoření teček (scatter) a čar (trails) pro každou planetu
    scatters = [ax.plot([], [], 'o', color=colors[i % 10], label=names[i])[
        0] for i in range(number_of_planets)]
    trails = [ax.plot([], [], '-', color=colors[i % 10])[0]
              for i in range(number_of_planets)]

    # Nastavení velikosti okna a legendy
    ax.set_xlim(-zoom, zoom)
    ax.set_ylim(-zoom, zoom)
    ax.legend()

    plt.axis('equal')
    plt.grid(True)
    plt.tight_layout()

    def init():
        # Inicializace prázdných dat před začátkem animace
        for scatter, trail in zip(scatters, trails):
            scatter.set_data([], [])
            trail.set_data([], [])
        return scatters + trails

    def update(frame):
        # Aktualizace poloh a drah při každém snímku
        for i in range(number_of_planets):
            x, y = history[i][frame]
            scatters[i].set_data([x], [y])
            trails[i].set_data(history[i][:frame + 1, 0],
                               history[i][:frame + 1, 1])
        return scatters + trails

    # Vytvoření animace
    ani: FuncAnimation = FuncAnimation(
        fig, update, frames=len(history[0]), init_func=init, blit=True)

    if save_path:
        # Uložení animace do souboru (např. jako GIF)
        writer = PillowWriter(fps=30)
        ani.save(save_path, writer=writer)
    else:
        # Pokud se neukládá, zobrazí se v notebooku
        return HTML(ani.to_jshtml())
