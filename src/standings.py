import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import messagebox, filedialog
from save_file import save_to_txt, export_to_excel

# Constants defined to store column widths for output file
POS_WIDTH = 5
DRIVER_WIDTH = 20
TEAM_WIDTH = 30
POINTS_WIDTH = 5


def driver_standings(year: int, save_type: str) -> None:
    # Attempt to retrieve data from site
    try:
        site = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html')
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'An exception occurred while fetching data: {e}')
        return

    # Parser instance
    d_standings = BeautifulSoup(site.text, 'html.parser')

    # Lists to store all relevant data
    driver_names = []
    driver_teams = []
    driver_points = []

    # Driver data to be parsed
    driver_data = d_standings.find_all('span', class_='max-tablet:hidden')
    team_and_point_data = d_standings.find_all('p', class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')

    # Parse data
    for i in range(len(driver_data)):
        driver_names.append(driver_data[i].text)

    for i in range(3, len(team_and_point_data), 5):
        driver_teams.append(team_and_point_data[i].text if team_and_point_data[i].text else 'N/A')

    for i in range(4, len(team_and_point_data), 5):
        driver_points.append(team_and_point_data[i].text)

    driver_pos = [i for i in range(1, len(driver_names) + 1)]

    if save_type == 'download':
        # Set up arguments
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")],
                                                 title="Save Driver Standings As",
                                                 initialfile=f'{year}-driver-standings.txt')
        headers = ['POS', 'DRIVER', 'TEAM', 'PTS']
        data = [driver_pos, driver_names, driver_teams, driver_points]
        column_widths = [POS_WIDTH, DRIVER_WIDTH, TEAM_WIDTH, POS_WIDTH]

        # Call to function
        save_to_txt(file_path, headers, data, column_widths, year)

    else:
        # Set up arguments
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")],
                                                 title="Save Race Results As",
                                                 initialfile=f'{year}-race-results.xlsx')
        data = {'POS': driver_pos, 'DRIVER': driver_names, 'TEAM': driver_teams, 'PTS': driver_points}
        df = pd.DataFrame(data)

        # Call to function
        export_to_excel(file_path, df, year)


def constructor_standings(year: int, save_type: str) -> None:
    # Attempt to retrieve data from site
    try:
        site = requests.get(f'https://www.formula1.com/en/results.html/{year}/team.html')
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'An exception occurred while fetching data: {e}')
        return

    # Parser instance
    c_standings = BeautifulSoup(site.text, 'html.parser')

    # Lists to store all relevant data
    constructors = []
    constructor_points = []

    # Constructor data to be parsed through
    constructor_data = c_standings.find_all('p', class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')

    # Parse data
    for i in range(1, len(constructor_data), 3):
        constructors.append(constructor_data[i].text)

    for i in range(2, len(constructor_data), 3):
        constructor_points.append(constructor_data[i].text)

    constructor_pos = [i for i in range(1, len(constructors) + 1)]

    if save_type == 'download':
        # Set up arguments
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")],
                                                 title="Save Constructor Standings As",
                                                 initialfile=f'{year}-constructor-standings.txt')
        headers = ['POS', 'CONSTRUCTOR', 'PTS']
        data = [constructor_pos, constructors, constructor_points]
        column_widths = [POS_WIDTH, TEAM_WIDTH, POINTS_WIDTH]

        # Call to function
        save_to_txt(file_path, headers, data, column_widths, year)
    else:
        # Set up arguments
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")],
                                                 title="Save Constructor Standings As",
                                                 initialfile=f'{year}-constructor-standings.xlsx')
        data = {'POS': constructor_pos, 'CONSTRUCTOR': constructors, 'PTS': constructor_points}
        df = pd.DataFrame(data)

        # Call to function
        export_to_excel(file_path, df, year)
