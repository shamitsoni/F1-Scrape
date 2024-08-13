import os
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox, filedialog

# Constants defined to store column widths for output file
POS_WIDTH = 5
DRIVER_WIDTH = 20
TEAM_WIDTH = 30
POINTS_WIDTH = 5


def driver_standings(year: int) -> None:
    try:
        site = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html')
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'An exception occurred while fetching data: {e}')
        return

    d_standings = BeautifulSoup(site.text, 'html.parser')
    driver_names = []
    driver_teams = []
    driver_points = []

    driver_data = d_standings.find_all('span', class_='max-tablet:hidden')
    team_and_point_data = d_standings.find_all('p', class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')

    for i in range(len(driver_data)):
        driver_names.append(driver_data[i].text)

    for i in range(3, len(team_and_point_data), 5):
        driver_teams.append(team_and_point_data[i].text if team_and_point_data[i].text else 'N/A')

    for i in range(4, len(team_and_point_data), 5):
        driver_points.append(team_and_point_data[i].text)

    # Open file save dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Save Driver Standings As",
                                             initialfile=f'{year}-driver-standings.txt')
    if not file_path:
        return

    with open(file_path, 'w') as file:
        file.write(f'{year} FORMULA ONE DRIVER STANDINGS\n\n')
        file.write(f'{"POS":<{POS_WIDTH}} {"DRIVER":<{DRIVER_WIDTH}} {"TEAM":<{TEAM_WIDTH}} {"PTS":<{POINTS_WIDTH}}\n')
        for i in range(len(driver_names)):
            file.write(f'#{i + 1:<{POS_WIDTH - 1}} {driver_names[i]:<{DRIVER_WIDTH}} {driver_teams[i]:<{TEAM_WIDTH}} {driver_points[i]:<{POINTS_WIDTH}}\n')

    messagebox.showinfo("Success", f'Driver standings for {year} have been saved to {file_path}')


def constructor_standings(year: int) -> None:
    try:
        site = requests.get(f'https://www.formula1.com/en/results.html/{year}/team.html')
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'An exception occurred while fetching data: {e}')
        return

    c_standings = BeautifulSoup(site.text, 'html.parser')
    constructors = []
    constructor_points = []

    constructor_data = c_standings.find_all('p', class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')

    for i in range(1, len(constructor_data), 3):
        constructors.append(constructor_data[i].text)

    for i in range(2, len(constructor_data), 3):
        constructor_points.append(constructor_data[i].text)

    # Open file save dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Save Constructor Standings As",
                                             initialfile=f'{year}-constructor-standings.txt')
    if not file_path:
        return

    with open(file_path, 'w') as file:
        file.write(f'{year} FORMULA ONE CONSTRUCTOR STANDINGS\n\n')
        file.write(f'{"POS":<{POS_WIDTH}} {"CONSTRUCTOR":<{TEAM_WIDTH}}  {"PTS":<{POINTS_WIDTH}}\n')
        for i in range(len(constructors)):
            file.write(f'#{i + 1:<{POS_WIDTH - 1}} {constructors[i]:<{TEAM_WIDTH}}  {constructor_points[i]:<{POINTS_WIDTH}}\n')

    messagebox.showinfo("Success", f'Constructor standings for {year} have been saved to {file_path}')