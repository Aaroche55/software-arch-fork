import matplotlib.pyplot as plt


def ask_country():
    return input("Enter a country (USA or Russia): ").strip()


def ask_year():
    return input("Enter a year: ").strip()


def show_country_total(country, total_hours):
    print(f"Total EVA hours for {country} is: {total_hours}")


def show_year_stats(year, count, total_hours):
    print(f"Total EVAs in {year} was: {count}")
    print(f"Total duration of EVAs in {year} was: {total_hours}")


def plot_cumulative(dates, cumulative_hours, output_path):
    plt.plot(dates, cumulative_hours)
    plt.xlabel("Year")
    plt.ylabel("Cumulative EVA duration (hours)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
