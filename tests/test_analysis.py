import pandas as pd
import pytest

from report_tools.analysis import (
    calculate_channel_kpis, 
    calculate_device_kpis,
    calculate_daily_kpis
)


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


def test_calculate_device_kpis(): 
    """Testar att KPI:er beräknas korrekt per enhet."""
    data = pd.DataFrame(
        {
            "device": ["Desktop", "Desktop"],
            "sessions": [200, 300],
            "users": [150, 220],
            "pageviews": [600, 900],
            "conversions": [20, 30],
            "revenue": [2000.0, 3000.0],
            "bounce_rate": [0.40, 0.60],
            "avg_session_duration": [100, 140]
        }
    )
    expected = pd.DataFrame(
        {
            "device": ["Desktop"],
            "sessions": [500],
            "users": [370],
            "pageviews": [1500],
            "conversions": [50],
            "revenue": [5000.0],
            "avg_bounce_rate": [0.50],
            "avg_session_duration": [120],
            "conversion_rate": [10.0],
            "revenue_per_session": [10.0]
        }
    )

    result = calculate_device_kpis(data)

    pd.testing.assert_frame_equal(result, expected)


def test_calculate_device_kpis_zero_sessions():
    """Testar att division med noll hanteras."""
    data = pd.DataFrame(
        {
            "device": ["Desktop"],
            "sessions": [0],
            "users": [0],
            "pageviews": [0],
            "conversions": [0],
            "revenue": [0],
            "bounce_rate": [0.50],
            "avg_session_duration": [100]
        }
    )

    result = calculate_device_kpis(data)

    assert pd.isna(result.loc[0, "conversion_rate"])
    assert pd.isna(result.loc[0, "revenue_per_session"])


def test_calculate_daily_kpis():
    """Testar att KPI:er beräknas korrekt per dag."""

    data = pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2026-01-01", "2026-01-01"]
            ),
            "sessions": [200, 300],
            "users": [150, 220],
            "pageviews": [600, 900],
            "conversions": [20, 30],
            "revenue": [2000, 3000],
            "marketing_cost": [200, 300],
        }
    )
    expected = pd.DataFrame(
        {
            "date": pd.to_datetime(["2026-01-01"]),
            "sessions": [500],
            "users": [370],
            "pageviews": [1500],
            "conversions": [50],
            "revenue": [5000.0],
            "marketing_cost": [500.0],
            "conversion_rate": [10.0],
            "revenue_per_session": [10.0],
            "roas": [10.0],
        }
    )

    result = calculate_daily_kpis(data)

    pd.testing.assert_frame_equal(result, expected)


def test_calculate_daily_kpis_zero_marketing_cost():
    """Testar att ROAS blir NaN när marketing_cost är 0."""

    data = pd.DataFrame(
        {
            "date": pd.to_datetime(["2026-01-01"]),
            "sessions": [100],
            "users": [50],
            "pageviews": [300],
            "conversions": [5],
            "revenue": [1000.0],
            "marketing_cost": [0.0],
        }
    )

    result = calculate_daily_kpis(data)

    assert pd.isna(result.loc[0, "roas"])