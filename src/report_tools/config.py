"""Innehåller konfiguration och sökvägar för rapportgenereringen."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ReportConfig:
    """Sökvägar som behövs för att skapa rapporten"""
    input_path: Path = Path("data/web_traffic_marketing_data_2026.csv")
    output_dir: Path = Path("output")
    template_dir: Path = Path("templates")