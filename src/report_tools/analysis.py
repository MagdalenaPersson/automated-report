import pandas as pd


def calculate_channel_kpis(data: pd.DataFrame) -> pd.DataFrame:
    """Beräknar KPI:er per marknadsföringskanal."""

    kpis = (
        data.groupby("channel")
        .agg(
            sessions = ("sessions", "sum"),
            users = ("users", "sum"),
            pageviews = ("pageviews", "sum"),
            conversions = ("conversions", "sum"),
            revenue = ("revenue", "sum"),
            marketing_cost = ("marketing_cost", "sum"),
            avg_bounce_rate  = ("bounce_rate", "mean"),
            avg_session_duration = ("avg_session_duration", "mean")
        )
        .reset_index()
    )

    kpis["conversion_rate"] = (
        kpis["conversions"] / kpis["sessions"] * 100
    )

    kpis["revenue_per_session"] = (
        kpis["revenue"] / kpis["sessions"]
    )

    kpis["roas"] = (
        kpis["revenue"] / kpis["marketing_cost"].replace(0, pd.NA)
    )

    kpis["avg_session_duration"] = (
        kpis["avg_session_duration"].round().astype(int)
    )

    return kpis


def calculate_device_kpis(data: pd.DataFrame) -> pd.DataFrame:
    """Beräknar KPI:er per enhet."""

    kpis = (
        data.groupby("device")
        .agg(
            sessions = ("sessions", "sum"),
            users = ("users", "sum"),
            pageviews = ("pageviews", "sum"),
            conversions = ("conversions", "sum"),
            revenue = ("revenue", "sum"),
            avg_bounce_rate  = ("bounce_rate", "mean"),
            avg_session_duration = ("avg_session_duration", "mean")
        )
        .reset_index()
    )

    kpis["conversion_rate"] = (
        kpis["conversions"] / kpis["sessions"] * 100
    )

    kpis["revenue_per_session"] = (
        kpis["revenue"] / kpis["sessions"]
    )

    kpis["avg_session_duration"] = (
        kpis["avg_session_duration"].round().astype(int)
    )

    return kpis


def calculate_daily_kpis(data: pd.DataFrame) -> pd.DataFrame:
    """Beräknar KPI:er per dag."""

    kpis = (
        data.groupby("date")
        .agg(
            sessions=("sessions", "sum"),
            users=("users", "sum"),
            pageviews=("pageviews", "sum"),
            conversions=("conversions", "sum"),
            revenue=("revenue", "sum"),
            marketing_cost=("marketing_cost", "sum")
        )
        .reset_index()
    )

    kpis["revenue"] = kpis["revenue"].astype(float)
    kpis["marketing_cost"] = kpis["marketing_cost"].astype(float)

    kpis["conversion_rate"] = (
        kpis["conversions"] / kpis["sessions"] * 100
    )
    
    kpis["revenue_per_session"] = (
        kpis["revenue"] / kpis["sessions"]
    )

    kpis["roas"] = (
        kpis["revenue"] / kpis["marketing_cost"].replace(0, pd.NA)
    )

    return kpis
    