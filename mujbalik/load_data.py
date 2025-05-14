import json
import numpy as np
import pandas as pd
from typing import Dict, Any


def load_json_data(file_path: str) -> Dict[str, Any]:
    """
    Funkce slouží k načteni dat z .json souboru (který nam byl poskytnut).
    Soubor obsahuje informace o planetách, jako jsou jejich pozice, rychlosti a hmotnosti.

    Args:
        file_path (str): cesta k .json souboru, který chci přečíst (třeba "data/planets.json")

    Returns:
        data (Dict[str, Any]: vrací data, která se nacházela v souboru, jako Python slovník
    """
    # pouzijeme 'with open', aby se soubor hned po otevření sám zavřel
    with open(file_path, 'r') as file:
        # převedení z .json souboru na Python slovník
        data: Dict[str, any] = json.load(file)
    return data


def convert_json_to_csv(json_data: Dict[str, Any],
                        output_csv: str) -> None:
    """
    Funkce na převedení dat ze souboru .json -> .csv tabulky

    Args:
        json_data (Dist[str, Any]): slovnik s informacemi o planetách,
        output_csv (str): cesta k .csv souboru, kde chci uložit data

    """
    # prázdné seznamy pro uložení dat
    names: list[str] = []
    position_x: list[float] = []
    position_y: list[float] = []
    velocity_x: list[float] = []
    velocity_y: list[float] = []
    masses: list[float] = []

    # procházíme vsechny data o planetách, aby jsme si je mohli uložit
    # integrujeme pomoci kliče (název planety) a hodnoty (informace o planetě)
    for planet_name, planet_info in json_data.items():
        names.append(planet_name)
        pos: list[float] = planet_info['position']
        velocity: list[float] = planet_info['velocity']

        # rozdelíme si pozici a rychlost na x a y složku
        position_x.append(pos[0])
        position_y.append(pos[1])
        velocity_x.append(velocity[0])
        velocity_y.append(velocity[1])
        masses.append(planet_info['mass'])

    # vytvoříme si tabulku "DataFrame" s daty
    df: pd.DataFrame = pd.DataFrame({
        'name': names,
        'position_x': position_x,
        'position_y': position_y,
        'velocity_x': velocity_x,
        'velocity_y': velocity_y,
        'mass': masses
    })

    # uložíme si tabulku jako .csv soubor
    # ondex=False znamená, že nechceme mít cisla v CSV souboru
    df.to_csv(output_csv, index=False)
    print(f"Data úspěsně převedena do souboru: {output_csv}")


def save_scenario_to_csv(names: list[str],
                         positions: np.ndarray,
                         velocities: np.ndarray,
                         masses: np.ndarray,
                         filename="scenario_data.csv") -> None:
    """
    Uloží data vygenerovaného scénáře (pozice, rychlosti, hmotnosti) do CSV souboru.

    Args:
        names (list[str]): Seznam názvů těles
        positions (np.ndarray): Numpy pole s pozicemi těles
        velocities (np.ndarray): Numpy pole s rychlostmi těles
        masses (np.ndarray): Numpy pole s hmotnostmi těles
        filename (str, optional): Název souboru pro uložení dat (výchozí je "scenario_data.csv")

    """

    # Zajistíme, že všechny vstupní seznamy/pole mají stejný počet prvků/řádků
    if not (len(names) == positions.shape[0] == velocities.shape[0] == masses.shape[0]):
        raise ValueError(
            "Počet prvků v seznamech/polích (názvy, pozice, rychlosti, hmotnosti) se neshoduje.")

    # Vytvoření slovníku pro DataFrame
    data: Dict[str, np.ndarray] = {
        'name': np.array(names),
        'position_x': positions[:, 0],
        'position_y': positions[:, 1],
        'velocity_x': velocities[:, 0],
        'velocity_y': velocities[:, 1],
        'mass': masses[:, 0]  # Použijeme pouze první sloupec z masses
    }

    # Vytvoření Pandas DataFrame
    df: pd.DataFrame = pd.DataFrame(data)

    # Uložení DataFrame do CSV souboru
    df.to_csv(filename, index=False)
    print(f"Data úspěsně převedena do souboru: {filename}")
