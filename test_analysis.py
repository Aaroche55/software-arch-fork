import unittest
from datetime import datetime

import analysis
from data_prep import EVA, find_unknown_countries, parse_year_range

# Small hand-made dataset so expected results are easy to work out
EVAS = [
    EVA("USA", datetime(2000, 1, 1), 2.0),
    EVA("USA", datetime(2001, 6, 1), 4.0),
    EVA("USA", datetime(2005, 1, 1), 10.0),
    EVA("Russia", datetime(2000, 3, 1), 3.0),
    EVA("Russia", datetime(2001, 12, 31), 3.0),
    EVA("Russia", None, 5.0),
]


class CompareCountriesTests(unittest.TestCase):
    def test_counts_totals_averages_and_leader(self):
        stats_a, stats_b, leader = analysis.compare_countries(EVAS, "USA", "Russia", 2000, 2001)
        self.assertEqual(stats_a, (2, 6.0, 3.0))
        self.assertEqual(stats_b, (2, 6.0, 3.0))
        self.assertIsNone(leader)  # tie

    def test_start_and_end_years_are_included(self):
        stats_a, stats_b, leader = analysis.compare_countries(EVAS, "USA", "Russia", 2001, 2005)
        self.assertEqual(stats_a, (2, 14.0, 7.0))
        self.assertEqual(stats_b, (1, 3.0, 3.0))
        self.assertEqual(leader, "USA")

    def test_no_matching_evas_gives_zero_and_no_average(self):
        stats_a, stats_b, leader = analysis.compare_countries(EVAS, "USA", "Russia", 2005, 2005)
        self.assertEqual(stats_b, (0, 0, None))
        self.assertEqual(leader, "USA")


class ExistingAnalysisTests(unittest.TestCase):
    def test_stats_for_year(self):
        self.assertEqual(analysis.stats_for_year(EVAS, "2001"), (2, 7.0))

    def test_total_hours_for_country_includes_undated(self):
        self.assertEqual(analysis.total_hours_for_country(EVAS, "Russia"), 11.0)


class InvalidInputTests(unittest.TestCase):
    def test_start_after_end_is_rejected(self):
        self.assertIsNone(parse_year_range("2005", "2000"))

    def test_non_numeric_year_is_rejected(self):
        self.assertIsNone(parse_year_range("abc", "2000"))

    def test_same_start_and_end_is_valid(self):
        self.assertEqual(parse_year_range("1985", "1985"), (1985, 1985))

    def test_unknown_country_is_found(self):
        self.assertEqual(find_unknown_countries(EVAS, "USA", "China"), ["China"])


if __name__ == "__main__":
    unittest.main()
