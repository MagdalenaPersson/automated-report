import pandas as pd
import pytest

from report_tools.cleaning import clean_web_analytics


def test_clean_web_analytics() -> None:
    """Testar att datan rensas korrekt."""

    data = pd.DataFrame(
        {
            "date": ["2024-01-01", "2024-01-02"],
            "channel": [" Organic ", "ORGANIC"],
            "device": [" Mobile ", "MOBILE"],
            "sessions": ["100", "50"],
            "users": ["80", "40"],
            "pageviews": ["200", "120"],
            "bounce_rate": [0.45, None],
            "avg_session_duration": [300, None],
            "conversions": [None, 2],
            "revenue": [None, 150],
            "marketing_cost": [None, 50],
        }
    ) 
    expected = pd.DataFrame(
        {
            "date": pd.to_datetime(["2024-01-01", "2024-01-02"]),
            "channel": ["Organic", "Organic"],
            "device": ["Mobile", "Mobile"],
            "sessions": [100, 50],
            "users": [80, 40],
            "pageviews": [200, 120],
            "bounce_rate": [0.45, 0.45],
            "avg_session_duration": [300, 300],
            "conversions": [0, 2],
            "revenue": [0.0, 150.0],
            "marketing_cost": [0.0, 50.0],
        }
    )

    result = clean_web_analytics(data)

    pd.testing.assert_frame_equal(
        result[expected.columns], 
        expected
    )

