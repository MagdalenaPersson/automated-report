import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from .analysis import calculate_channel_kpis

project_palette = [
    "#315C5A",
    "#E8DED3",
    "#F7F3EE",
    "#303030",
    "#C58B7B"
]

sns.set_theme(
    style="whitegrid",
    palette=project_palette
)

from .analysis import (
    calculate_channel_kpis,
    calculate_device_kpis,
    calculate_daily_kpis
)


def plot_revenue_over_time(data):
    """Skapar ett linjediagram över revenue per månad."""

    monthly_revenue = (
        data.set_index("date")
        .resample("ME")["revenue"]
        .sum()
        .reset_index()
    )

    monthly_revenue["revenue_million"] = (
        monthly_revenue["revenue"] / 1_000_000
    )

    fig, ax = plt.subplots(figsize=(10,6))

    sns.lineplot(
        x=monthly_revenue["date"],
        y=monthly_revenue["revenue_million"],
        marker="o",
        ax=ax
    )

    ax.fill_between(
        monthly_revenue["date"],
        monthly_revenue["revenue_million"],
        alpha=0.15
    )

    ax.set_title("Revenue over time", fontsize=18)
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (million SEK)")

    fig.tight_layout()

    return fig


def plot_revenue_vs_cost_by_channel(channel_kpis):
    """Skapar ett horisontellt stapeldiagram över revenue vs. marketing_cost per marknadsföringskanal."""

    data = channel_kpis.copy()
    data = channel_kpis.sort_values("revenue")

    y = range(len(data))
    height = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    plt.barh(
        [i - height / 2 for i in y],
        data["revenue"],
        height=height,
        label="Revenue",
        color=project_palette[0]
    )

    plt.barh(
        [i + height / 2 for i in y],
        data["marketing_cost"],
        height=height,
        label="Marketing cost",
        color=project_palette[4]
    )

    plt.yticks(y, data["channel"])
    plt.xlabel("Amount (SEK)")
    plt.ylabel("Channel")
    plt.title("Revenue vs marketing cost per channel", fontsize=16)
    plt.legend()

    fig.tight_layout()

    return fig


def plot_roas_by_channel(channel_kpis):
    """Skapar ett horisontellt stapeldiagram över ROAS per kanal."""

    data = channel_kpis.copy()
    data["roas"] = pd.to_numeric(data["roas"], errors="coerce")
    data = data.dropna(subset=["roas"]).sort_values("roas")

    fig = plt.figure(figsize=(10, 6))

    plt.barh(
        data["channel"],
        data["roas"],
        color=project_palette[0]
    )

    plt.title("ROAS per Channel", fontsize=16)
    plt.xlabel("ROAS (Revenue generated per SEK spent)")
    plt.ylabel("Channel")

    plt.tight_layout()

    return fig


def save_chart(fig, path): 
    """Sparar ett diagram som PNG."""
    fig.savefig(
        path,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(fig)