"""Publikt API för paketet automated_report."""

from .config import ReportConfig
from .loading import load_web_traffic
from .cleaning import clean_web_analytics
from .validation import validate_clean_data

from .analysis import (
    calculate_channel_kpis, 
    calculate_daily_kpis, 
    calculate_device_kpis
)

from .visualization import (
    plot_revenue_over_time,
    plot_revenue_vs_cost_by_channel,
    plot_roas_by_channel,
    save_chart
)

from .output import save_report