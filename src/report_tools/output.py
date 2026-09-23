"""Hanterar sparning av genererade rapporter."""

from pathlib import Path
import pandas as pd


def save_report(data: pd.DataFrame, path: Path) -> None:
    """Sparar rapport som CSV-fil."""

    path.parent.mkdir(parents=True, exist_ok=True)

    data.to_csv(path, index=False)
