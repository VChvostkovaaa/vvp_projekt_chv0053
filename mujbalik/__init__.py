"""
Tento balíček poskytuje nástroje a funkce pro simulaci pohybu planet v gravitačním poli.

ZÁKLADNÍ FUNKCE:
-------------------
- load_data: načítaní .json souboru a pote převedení na .csv soubor
- physics: výpočet gravitačního zrychlení mezi dvojcemi planet
- drawing: vykreslení aktuální polohy planet
- simulacion: hlavní funcke pro simulaci pohybu planet, a ukladání do "historie" pro vizualizaci
- visualization: vytvořeni animace z "historie" a uložení do .gif souboru
- random_place: generuje nahodne počateční podmínky pro simulaci planet (posicion, velocity, mass)
- experiments: různé délky časového kroku (u planet např. hodina, den, týden, ...)

"""

from .simulation import run_simulation
from .physics import compute_accelerations
from .current_position import current_positions
from .visualization import create_animation
from .random_place import generate_random_scenario
from .load_data import load_json_data, convert_json_to_csv, save_scenario_to_csv
from .experiments import run_timestep_experiment

__all__ = [
    "run_simulation",
    "compute_accelerations",
    "current_positions",
    "create_animation",
    "generate_random_scenario",
    "load_json_data",
    "convert_json_to_csv",
    "run_timestep_experiment",
]