import requests
from InvalidYearException import InvalidYear
from bs4 import BeautifulSoup

# Constants defined to store column widths for output file
POS_WIDTH = 5
DRIVER_WIDTH = 20
TEAM_WIDTH = 30
POINTS_WIDTH = 5


def main() -> None:
    # Pick an F1 season between 1950 and 2024
    year = 2002

    if not (1950 <= year <= 2024):
        raise InvalidYear('Please enter a valid year between 1950 and 2024.')

    # Data retrieval from site
    try:
        site = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html')
    except requests.exceptions.RequestException as e:
        print(f'An exception occurred while fetching data: {e}')
        return

    # Parser instance
    soup = BeautifulSoup(site.text, 'html.parser')

    # Lists to store all relevant data
    teams = []
    points = []

    # Driver data to be parsed through
    drivers = soup.find_all('span', class_='max-tablet:hidden')
    team_data = soup.find_all('a',
                                class_='underline underline-offset-normal decoration-1 decoration-greyLight hover:decoration-brand-primary')
    point_data = soup.find_all('p',
                                class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')

    # Parse through data and store team names
    for i in range(1, len(team_data), 2):
        teams.append(team_data[i])

    # Parse through data and store all points
    for i in range(4, len(point_data), 5):
        points.append(point_data[i])

    # Prints results to a new file
    with open(f'{year}-standings.txt', 'w') as file:
        file.write(f'{year} FORMULA ONE DRIVER STANDINGS\n\n')
        file.write(f'{"POS":<{POS_WIDTH}} {"DRIVER":<{DRIVER_WIDTH}} {"TEAM":<{TEAM_WIDTH}} {"PTS":<{POINTS_WIDTH}}\n')
        for i in range(len(drivers)):
            file.write(f'#{i+1:<{POS_WIDTH-1}} {drivers[i].text:<{DRIVER_WIDTH}} {teams[i].text:<{TEAM_WIDTH}} {points[i].text:<{POINTS_WIDTH}}\n')


if __name__ == '__main__':
    main()
