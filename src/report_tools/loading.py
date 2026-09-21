"""Filinläsning av webbtrafik"""

import pandas as pd
from pathlib import Path


def load_web_traffic(path: Path) -> pd.DataFrame:
    """Läs in webbtrafik från en CSV-fil."""

    data = pd.read_csv(path)

    return data 