"""Rensar och omvandlar webbtrafikdata inför analys."""

import pandas as pd

def clean_web_analytics(data: pd.DataFrame) -> pd.DataFrame:
    """Rensar och städar upp i datasetet."""
    data = data.copy() # skapa kopia

    data["date"] = pd.to_datetime(data["date"], errors="coerce") # konvertera datum

    text_columns = ["channel", "device"]

    for col in text_columns:
        data[col] = (
            data[col]
            .astype(str)
            .str.title()
            .str.strip()
        )

    numeric_columns = [
        "sessions", 
        "users", 
        "pageviews",
        "bounce_rate", 
        "avg_session_duration",
        "conversions", 
        "revenue", 
        "marketing_cost"]

    for col in numeric_columns: 
        data[col] = pd.to_numeric(data[col], errors="coerce")


    data["bounce_rate"] = data.groupby(
        ["channel", "device"]
    )["bounce_rate"].transform(lambda x: x.fillna(x.median())
    ) # fyller saknade värden i bounce_rate med median/channel + device

    data["avg_session_duration"] = data["avg_session_duration"].fillna(
        data["avg_session_duration"].median()
    ) # fyller saknade värden i avg_session_duration med medianen

    columns_replaced_with_zero = [
        "revenue", 
        "conversions", 
        "sessions", 
        "users", 
        "pageviews", 
        "marketing_cost"
    ]
    
    for column in columns_replaced_with_zero:
        if column in data.columns:
            data[column] = data[column].fillna(0) # kolumner som ska ersättas med 0 vid saknade värden

    data["conversions"] = data["conversions"].astype(int)
    data["avg_session_duration"] = data["avg_session_duration"].astype(int) # ändrar type till int

    data = data.drop_duplicates() # ta bort dubletter

    data = data.reset_index(drop=True) # reset index

    return data


def validate_clean_data(data: pd.DataFrame) -> None:
    """Validerar att städad data uppfyller reglerna."""

    if (data["sessions"] < 0).any():
        raise ValueError("Sessions kan inte vara negativt.")

    if (data["users"] < 0).any():
            raise ValueError("Users kan inte vara negativt.")

    if (data["conversions"] < 0).any():
            raise ValueError("Conversions kan inte vara negativt.")