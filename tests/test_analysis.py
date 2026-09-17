import pandas as pd
import pytest

from report_tools.analysis import calculate_channel_kpis


def test_calculate_channel_kpis():
    """Testar att KPI:er beräknas korrekt per marknadsföringskanal."""
    data = pd.DataFrame(
        {
            "channel": ["Organic", "Paid"],
            "sessions": [100, 200],
            "users": [50, 30],
            "pageviews": [300, 100],
            "conversions": [5, 10],
            "revenue": [1000, 5000],
            "marketing_cost": [200, 500],
            "bounce_rate": [0.50, 0.70],
            "avg_session_duration": [120, 180]
        }
    )
    expected = pd.DataFrame(
        {
           "channel": ["Organic", "Paid"],
            "sessions": [100, 200],
            "users": [50, 30],
            "pageviews": [300, 100],
            "conversions": [5, 10],
            "revenue": [1000, 5000],
            "marketing_cost": [200, 500],
            "avg_bounce_rate": [0.50, 0.70],
            "avg_session_duration": [120, 180],
            "conversion_rate": [5.0, 5.0],
            "revenue_per_session": [10.0, 25.0],
            "roas": [5.0, 10.0]
        }
    )

    result = calculate_channel_kpis(data)

    pd.testing.assert_frame_equal(result, expected)


def test_calculate_channel_kpis_zero_marketing_cost():
    """Testar att ROAS blir NaN när marketing_cost är 0."""
    data = pd.DataFrame(
        {
            "channel": ["Organic"],
            "sessions": [100],
            "users": [50],
            "pageviews": [300],
            "conversions": [5],
            "revenue": [1000],
            "marketing_cost": [0],
            "bounce_rate": [0.50],
            "avg_session_duration": [120]
        }
    )

    result = calculate_channel_kpis(data)

    assert pd.isna(result.loc[0, "roas"])