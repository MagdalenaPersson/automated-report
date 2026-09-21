from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from . import (
    ReportConfig,
    load_web_traffic,
    clean_web_analytics,
    validate_clean_data,
    calculate_channel_kpis,
    calculate_device_kpis,
    calculate_daily_kpis,
    plot_revenue_over_time,
    plot_revenue_vs_cost_by_channel,
    plot_roas_by_channel, 
    save_chart
)

def main() -> None:
    """Kör programmet"""

    config = ReportConfig()

    data = load_web_traffic(config.input_path)

    cleaned_data = clean_web_analytics(data)

    validate_clean_data(cleaned_data)

    channel_kpis = calculate_channel_kpis(cleaned_data)
    device_kpis = calculate_device_kpis(cleaned_data)
    daily_kpis = calculate_daily_kpis(cleaned_data)

    device_kpis_display = device_kpis.copy()

    device_kpis_display["conversion_rate"] = (
        device_kpis_display["conversion_rate"].round(2)
    )

    device_kpis_display["revenue"] = (
        device_kpis_display["revenue"].round(2)
    )


    chart_dir = config.output_dir / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)

    revenue_vs_cost_fig = plot_revenue_vs_cost_by_channel(channel_kpis)
    save_chart(
        revenue_vs_cost_fig,
        chart_dir / "revenue_vs_cost_by_channel.png"
    )

    roas_fig = plot_roas_by_channel(channel_kpis)

    save_chart(
        roas_fig,
        chart_dir / "roas_by_channel.png"
    )

    revenue_over_time_fig = plot_revenue_over_time(daily_kpis)

    save_chart(
        revenue_over_time_fig,
        chart_dir / "revenue_over_time.png"
    )


    total_sessions = cleaned_data["sessions"].sum()
    total_conversions = cleaned_data["conversions"].sum()
    total_revenue = cleaned_data["revenue"].sum()

    overall_conversion_rate = (
        total_conversions / total_sessions * 100
    )

    total_sessions_display = f"{total_sessions / 1_000_000:.2f} M"
    total_revenue_display = f"{total_revenue / 1_000_000:.2f} MSEK"
    overall_conversion_rate_display = f"{overall_conversion_rate:.2f} "

    revenue_vs_cost_chart = "charts/revenue_vs_cost_by_channel.png"
    roas_chart = "charts/roas_by_channel.png"
    revenue_over_time_chart = "charts/revenue_over_time.png"

    env = Environment(
        loader=FileSystemLoader(config.template_dir)
    )

    template = env.get_template("report.html")

    html = template.render(
        total_sessions=total_sessions_display,
        total_conversions=total_conversions,
        total_revenue=total_revenue_display,
        overall_conversion_rate=overall_conversion_rate_display,
        channel_kpis=channel_kpis.to_dict("records"),
        device_kpis=device_kpis_display.to_dict("records"),

        revenue_vs_cost_chart=revenue_vs_cost_chart,
        roas_chart=roas_chart,
        revenue_over_time_chart=revenue_over_time_chart
    )

    output_file = config.output_dir / "report.html"

    config.output_dir.mkdir(exist_ok=True)

    output_file.write_text(
        html,
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()