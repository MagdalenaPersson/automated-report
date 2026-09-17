"""Filinläsning av webbtrafik"""

import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def load_web_traffic(path: Path) -> pd.DataFrame:
    """Läs in webbtrafik från en CSV-fil."""

    data = pd.read_csv(path)

    logger.info(
        "Läste in %s rader från datasetet %s",
        len(data),
        path.name
    )

    return data 