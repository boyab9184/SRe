import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

import unittest
import pandas as pd
from src.calculations import total_bytes_exchanged, least_frequent_ip, most_frequent_ip, events_per_second


class TestAssessment(unittest.TestCase):

    df = pd.DataFrame({
        "Response size in bytes": [1, 2, 3, 4, 5, 1],
        "Response header size in bytes": [1, 2, 3, 4, 5, 1],
        "Client IP address": ["192.168.0.1", "192.168.0.2", "192.168.0.2", "192.168.0.3", "192.168.0.3", "192.168.0.3"],
        "Timestamp in seconds since the epoch": [10, 10, 10, 10, 10, 11]
    })


    def test_total_bytes_exchanged_should_return_sum_of_two_column(self):

        #arrange
        expected = 32
        #act
        actual = total_bytes_exchanged(self.df)
        #assert
        self.assertEqual(expected, actual)


    def test_most_frequent_ip_should_return_ip_that_occurs_most(self):

        #arrange
        expected = "192.168.0.3"
        #act
        actual = most_frequent_ip(self.df)
        #assert
        self.assertEqual(expected, actual)


    def test_most_frequent_ip_should_return_ip_that_occurs_least(self):

        #arrange
        expected = "192.168.0.1"
        #act
        actual = least_frequent_ip(self.df)
        #assert
        self.assertEqual(expected, actual)


    def test_events_per_second_should_return_events_devided_by_delta_sec(self):

        #arrange
        expected = 3
        #act
        actual = events_per_second(self.df)
        #assert
        self.assertEqual(expected, actual)


    def test_events_should_return_total_events_if_all_happend_at_the_same_time(self):

        #arrange
        df = pd.DataFrame({
            "Timestamp in seconds since the epoch": [10, 10, 10, 10, 10, 10]
        })
        expected = 6
        #act
        actual = events_per_second(df)
        #assert
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()