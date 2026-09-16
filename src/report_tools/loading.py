"""Filinläsning av webbtrafik"""

import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def load_web_traffic(path: Path) -> pd.DataFrame:
    """Läs in webbtrafik från en CSV-fil."""

    logger.info("Läser in data för webbtrafik från %s", path)

    data = pd.read_csv(path)

    logger.info("Läste in %s rader", len(data))

    return data 