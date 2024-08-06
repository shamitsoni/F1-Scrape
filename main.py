import requests
from bs4 import BeautifulSoup


def main() -> None:
    # Insert a year to view the F1 Driver Standings
    year = 2024

    # Setup
    site = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html')
    soup = BeautifulSoup(site.text, 'html.parser')

    # Driver data to be parsed through
    drivers = soup.find_all('span', class_='max-tablet:hidden')
    team_data = soup.find_all('a', class_='underline underline-offset-normal decoration-1 decoration-greyLight hover:decoration-brand-primary')
    point_data = soup.find_all('p', class_='f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px')

    # Lists to store all relevant data
    teams = []
    points = []

    # Parse through data and store team names
    for i in range(1, len(team_data), 2):
        teams.append(team_data[i])

    # Parse through data and store all points
    for i in range(4, len(point_data), 5):
        points.append(point_data[i])

    # Print standings and data
    print(f'\n{year} FORMULA ONE DRIVER STANDINGS\n')
    for i in range(len(drivers)):
        print(f'#{i+1} {drivers[i].text} | {teams[i].text} | {points[i].text} Pts')


if __name__ == '__main__':
    main()



