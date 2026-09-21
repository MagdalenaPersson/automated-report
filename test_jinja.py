from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src.report_tools.loading import load_data
from src.report_tools.cleaning import clean_web_analytics
from src.report_tools.analysis import calculate_channel_kpis

project_root = Path(__file__).parent
template_dir = project_root / "templates"

env = Environment(
    loader=FileSystemLoader(template_dir)
)

template = env.get_template("report.html")

data = load_data(project_root / "data" / "web_traffic_marketing_data_2026.csv")

clean_data = clean_web_analytics(data)

channel_kpis = calculate_channel_kpis(clean_data)

html = template.render(
    channel_kpis=channel_kpis.to_dict("records")
)

output_file = project_root / "output" / "test_report.html"
output_file.write_text(html, encoding="utf-8")

print(f"Report created: {output_file}")