"""Validerar den rensade datan."""

import pandas as pd

def validate_clean_data(data: pd.DataFrame) -> None:
    """Validerar att städad data uppfyller reglerna."""

    if (data["sessions"] < 0).any():
        raise ValueError("Sessions kan inte vara negativt.")

    if (data["users"] < 0).any():
            raise ValueError("Users kan inte vara negativt.")

    if (data["conversions"] < 0).any():
            raise ValueError("Conversions kan inte vara negativt.")