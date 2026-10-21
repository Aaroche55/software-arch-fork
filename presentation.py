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


def ask_comparison():
    country_a = input("Enter country A: ").strip()
    country_b = input("Enter country B: ").strip()
    start_year = input("Enter start year: ").strip()
    end_year = input("Enter end year: ").strip()
    return country_a, country_b, start_year, end_year


def show_error(message):
    print(f"Error: {message}")


def show_comparison(country_a, country_b, start_year, end_year, stats_a, stats_b, leader):
    print(f"EVA comparison {start_year}-{end_year}:")
    for country, (count, total, average) in ((country_a, stats_a), (country_b, stats_b)):
        average_text = f"{average:.2f} hours" if average is not None else "unavailable"
        print(f"  {country}: {count} EVAs, {total:.2f} hours total, average {average_text}")

    if leader:
        print(f"{leader} has the greater total EVA duration")
    else:
        print("It's a tie")


def plot_cumulative(dates, cumulative_hours, output_path):
    plt.plot(dates, cumulative_hours)
    plt.xlabel("Year")
    plt.ylabel("Cumulative EVA duration (hours)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
