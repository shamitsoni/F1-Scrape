import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from src.save_file import save_to_txt, export_to_excel


# Contains test cases that deal with writing and saving to .txt file
class TestWritingToTxtFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_race_results(self, mock_file):
        headers = ['RACE', 'DATE', 'WINNER', 'TEAM', 'LAPS', 'TIME']
        data = [['Race1', 'Race2'], ['Date1', 'Date2'], ['Winner1', 'Winner2'], ['Team1', 'Team2'], ['Laps1', 'Laps2'],
                ['Time1', 'Time2']]
        column_widths = [18, 18, 18, 32, 8, 8]
        file_path = 'test-race-results.txt'

        save_to_txt(file_path, headers, data, column_widths, 2024)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('2024 FORMULA ONE RESULTS\n\n')
        handle.write.assert_any_call(
            'RACE               DATE               WINNER             TEAM                             LAPS     TIME    \n')
        handle.write.assert_any_call(
            'Race1              Date1              Winner1            Team1                            Laps1    Time1   \n')
        handle.write.assert_any_call(
            'Race2              Date2              Winner2            Team2                            Laps2    Time2   \n')

    @patch("builtins.open", new_callable=mock_open)
    def test_driver_standings(self, mock_file):
        headers = ['POS', 'DRIVER', 'TEAM', 'PTS']
        data = [['1', '2'], ['Driver1', 'Driver2'], ['Team1', 'Team2'], ['100', '80']]
        column_widths = [5, 20, 30, 5]
        file_path = 'test-driver_standings.txt'

        save_to_txt(file_path, headers, data, column_widths, 2022)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('2022 FORMULA ONE RESULTS\n\n')
        handle.write.assert_any_call('POS   DRIVER               TEAM                           PTS  \n')
        handle.write.assert_any_call('1     Driver1              Team1                          100  \n')
        handle.write.assert_any_call('2     Driver2              Team2                          80   \n')

    @patch("builtins.open", new_callable=mock_open)
    def test_constructor_standings(self, mock_file):
        headers = ['POS', 'CONSTRUCTOR', 'PTS']
        data = [['1', '2'], ['Constructor1', 'Constructor2'], ['100', '80']]
        column_widths = [5, 20, 5]
        file_path = 'test-constructor_standings.txt'

        save_to_txt(file_path, headers, data, column_widths, 1967)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('1967 FORMULA ONE RESULTS\n\n')
        handle.write.assert_any_call('POS   CONSTRUCTOR          PTS  \n')
        handle.write.assert_any_call('1     Constructor1         100  \n')
        handle.write.assert_any_call('2     Constructor2         80   \n')


# Contains test case that deal with writing and saving to .xlsx file
class TestWritingToExcelFile(unittest.TestCase):

    @patch("pandas.DataFrame.to_excel")
    def test_export_to_excel(self, mock_to_excel):
        data = {
            'POS': [1, 2],
            'DRIVER': ['Driver1', 'Driver2'],
            'TEAM': ['Team1', 'Team2'],
            'PTS': [100, 80]
        }
        df = pd.DataFrame(data)
        file_path = 'test-driver_standings.xlsx'
        year = 2024

        export_to_excel(file_path, df, year)

        mock_to_excel.assert_called_once_with(file_path, index=False)
        pd.testing.assert_frame_equal(df, pd.DataFrame(data))
