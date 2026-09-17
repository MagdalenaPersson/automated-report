"""Sparar rapporter till filer."""

import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

def save_report(data: pd.DataFrame, path: Path) -> None:
    """Sparar rapport som CSV-fil."""

    path.parent.mkdir(parents=True, exist_ok=True)

    data.to_csv(path, index=False)

    logger.info("Rapport sparad till %s", path)