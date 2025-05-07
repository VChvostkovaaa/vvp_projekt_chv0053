import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import HTML

def create_animation(history, names, figsize = (8, 8), zoom = 4.79e+12, save_path = None):
    """
    vytvoří animaci na základě historie pozit všech planet.

    Args:
        history: historie pozic planet
        names: jména planet
        figsize: velikost okna obrázku
        zoom: vzdalenost zoomu
        save_path: cesta k souboru, ke ho budeme chtít uložt

    Returns:
        Uloží animaci do souboru
    """
    fig, ax = plt.subplots(figsize=figsize)
    colors = plt.cm.tab10.colors  # přednastavené barvy z matplotlibu
    number_of_planets = len(history)

    # Vytvoření teček (scatter) a čar (trails) pro každou planetu
    scatters = [ax.plot([], [], 'o', color=colors[i % 10], label=names[i])[0] for i in range(number_of_planets)]
    trails = [ax.plot([], [], '-', color=colors[i % 10])[0] for i in range(number_of_planets)]

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
            trails[i].set_data(history[i][:frame + 1, 0], history[i][:frame + 1, 1])
        return scatters + trails

    # Vytvoření animace
    ani = FuncAnimation(fig, update, frames=len(history[0]), init_func=init, blit=True)

    if save_path:
        # Uložení animace do souboru (např. jako GIF)
        writer = PillowWriter(fps=30)
        ani.save(save_path, writer=writer)
    else:
        # Pokud se neukládá, zobrazí se v notebooku
        return HTML(ani.to_jshtml())