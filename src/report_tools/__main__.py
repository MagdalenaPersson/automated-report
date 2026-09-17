import logging

from . import (
    ReportConfig,
    load_web_traffic,
    clean_web_analytics,
    validate_clean_data
)

logger = logging.getLogger("automated_report")

def main() -> None:
    """Kör programmet"""

    config = ReportConfig

    data = load_web_traffic(config.input_path)

    cleaned_data = clean_web_analytics(data)

    validate_clean_data(cleaned_data)