import requests
from bs4 import BeautifulSoup
from tkinter import messagebox, filedialog

# Constants defined to store column widths for output file
RACE_WIDTH = 18
DATE_WIDTH = 18
DRIVER_WIDTH = 18
TEAM_WIDTH = 32
LAP_WIDTH = 8
TIME_WIDTH = 8


def race_results(year: int) -> None:
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

    # Save file to specific path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Save Race Results As",
                                             initialfile=f'{year}-race-results.txt')
    if not file_path:
        return

    # Print results to a new file
    with open(f'{year}-race-results.txt', 'w') as file:
        file.write(f'{year} FORMULA ONE RACE RESULTS\n\n')
        file.write(
            f'{"RACE":<{RACE_WIDTH}} {"DATE":<{DATE_WIDTH}} {"WINNER":<{DRIVER_WIDTH}} {"TEAM":<{TEAM_WIDTH}} {"LAPS":<{LAP_WIDTH}} {"TIME":<{TIME_WIDTH}}\n')
        for i in range(len(race)):
            file.write(
                f'{race[i]:<{RACE_WIDTH}} {date[i]:<{DATE_WIDTH}} {winner[i]:<{DRIVER_WIDTH}} {team[i]:<{TEAM_WIDTH}} {laps[i]:<{LAP_WIDTH}} {time[i]:<{TIME_WIDTH}}\n')

    # Show confirmation message
    messagebox.showinfo("Success", f'Race results for {year} have been saved to {file_path}')
