import pandas as pd
import matplotlib.pyplot as plt


def current_positions(csv_path: str) -> None:
    """
    Tahle funkce vzeme aktuální pozice planet z .csv souboru a vykreslí je do grafu.

    Args:
        csv_path (str): cesta k .csv souboru s daty planet
    """

    # načteme data z .csv souboru do tamulda DataFrame
    df: pd.DataFrame = pd.read_csv(csv_path)

    # udělame si okno pro graf a nastavime velikost
    plt.figure(figsize=(8, 8))
    plt.title(f"Aktuální polohy planet", fontsize=15)

    for index, row in df.iterrows():    # iterrows: pandas -> umožnujemi procházet řádek po řádku
        # z každého řadku si vytáhneme potřebné informace
        x: float = row['position_x']
        y: float = row['position_y']
        name: int = row['name']

        # planeta -> jako tečka, label -> jméno planety, s -> velikost tečky
        plt.scatter(x, y, label=name, s=50)
        # text -> jméno planety, fontsize -> velikost písma, ha/va -> zarovnání textu
        plt.text(x, y, name, fontsize=9, ha='right', va='bottom')

    # vypíšeme si popisky os a mřížku
    plt.xlabel("x position")
    plt.ylabel("y position")
    plt.grid(True)
    plt.axis('equal')
    plt.tight_layout()      # upraví rozložení grafu, aby se vešel do okna
    plt.show()
