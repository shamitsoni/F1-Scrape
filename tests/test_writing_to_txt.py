import unittest
from unittest.mock import patch, mock_open
from src.save_file import save_to_txt


class TestWritingToTxtFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_race_results(self, mock_file):
        headers = ['RACE', 'DATE', 'WINNER', 'TEAM', 'LAPS', 'TIME']
        data = [['Race1', 'Race2'], ['Date1', 'Date2'], ['Winner1', 'Winner2'], ['Team1', 'Team2'], ['Laps1', 'Laps2'],
                ['Time1', 'Time2']]
        column_widths = [18, 18, 18, 32, 8, 8]
        file_path = 'text-race-results.txt'

        save_to_txt(file_path, headers, data, column_widths, 2024)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('RACE FORMULA ONE RESULTS\n\n')
        handle.write.assert_any_call(
            'RACE               DATE               WINNER             TEAM                             LAPS     TIME    \n')
        handle.write.assert_any_call(
            'Race1              Date1              Winner1            Team1                            Laps1    Time1   \n')

    @patch("builtins.open", new_callable=mock_open)
    def test_driver_standings(self, mock_file):
        headers = ['POS', 'CONSTRUCTOR', 'PTS']
        data = [['1', '2'], ['Constructor1', 'Constructor2'], ['100', '80']]
        column_widths = [5, 20, 5]
        file_path = 'driver_standings.txt'

        save_to_txt(file_path, headers, data, column_widths, 2024)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('POS FORMULA ONE RESULTS\n\n')
        handle.write.assert_any_call('POS   CONSTRUCTOR          PTS  \n')
        handle.write.assert_any_call('1     Constructor1         100  \n')
        handle.write.assert_any_call('2     Constructor2         80   \n')

    @patch("builtins.open", new_callable=mock_open)
    def test_constructor_standings(self, mock_file):
        headers = ['POS', 'CONSTRUCTOR', 'PTS']
        data = [['1', '2'], ['Constructor1', 'Constructor2'], ['100', '80']]
        column_widths = [5, 20, 5]
        file_path = 'constructor_standings.txt'

        save_to_txt(file_path, headers, data, column_widths, 2024)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('POS FORMULA ONE RESULTS\n\n')
        handle.write.assert_any_call('POS   CONSTRUCTOR          PTS  \n')
        handle.write.assert_any_call('1     Constructor1         100  \n')
        handle.write.assert_any_call('2     Constructor2         80   \n')
