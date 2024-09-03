import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import messagebox, filedialog
from save_file import save_to_txt, export_to_excel

# Constants defined to store column widths for output file
RACE_WIDTH = 18
DATE_WIDTH = 18
DRIVER_WIDTH = 18
TEAM_WIDTH = 32
LAP_WIDTH = 8
TIME_WIDTH = 8


def race_results(year: int, save_type: str) -> None:
    # Attempt to retrieve data from site
    try:
        site = requests.get(f'https://www.formula1.com/en/results/{year}/races')
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'An exception occurred while fetching data: {e}')
        return

    # Parser instance
    soup = BeautifulSoup(site.text, 'html.parser')

    # Race data to be parsed
    all_data = soup.find_all('p',
                             class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')
    winner_data = soup.find_all('span', class_='max-tablet:hidden')

    # Lists to store all relevant data
    race, date, winner, team, laps, time = [], [], [], [], [], []

    # Parse data
    for i in range(len(all_data)):
        if i % 6 == 0:
            race.append(all_data[i].text)
        elif i % 6 == 1:
            date.append(all_data[i].text)
        elif i % 6 == 3:
            team.append(all_data[i].text)
        elif i % 6 == 4:
            laps.append(all_data[i].text)
        elif i % 6 == 5:
            time.append(all_data[i].text)

    for i in range(len(winner_data)):
        winner.append(winner_data[i].text)

    # If the user wishes to save the file to their PC
    if save_type == 'download':
        # Set up arguments
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")],
                                                 title="Save Race Results As",
                                                 initialfile=f'{year}-race-results.txt')
        headers = ['RACE', 'DATE', 'WINNER', 'TEAM', 'LAPS', 'TIME']
        data = [race, date, winner, team, laps, time]
        column_widths = [RACE_WIDTH, DATE_WIDTH, DRIVER_WIDTH, TEAM_WIDTH, LAP_WIDTH, TIME_WIDTH]

        # Call to function
        save_to_txt(file_path, headers, data, column_widths, year)

    # If the user wishes to export the file to a spreadsheet
    else:
        # Set up arguments
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")],
                                                 title="Save Race Results As",
                                                 initialfile=f'{year}-race-results.xlsx')
        data = {'Race': race, 'Date': date, 'Winner': winner, 'Team': team, 'Laps': laps, 'Time': time}
        df = pd.DataFrame(data)

        # Call to function
        export_to_excel(file_path, df, year)
