from exceptions import InvalidYear, InvalidFormat
from standings import driver_standings, constructor_standings


def main() -> None:
    # Prompts user for selection
    print('What kind of data would you like?\n')
    standing_type = input('(D) Driver Standings | (C) Constructor Standings: ')
    year = int(input('Enter a year: '))

    # Raises an Exception if the year is invalid
    if not (1950 <= year <= 2024):
        raise InvalidYear('Please enter a valid year between 1950 and 2024.')

    # Calls the respective function to retrieve data or raises an exception if the format is invalid
    if standing_type.strip().lower() == 'd':
        driver_standings(year)
    elif standing_type.strip().lower() == 'c':
        constructor_standings(year)
    else:
        raise InvalidFormat('Please enter a valid format: (D) or (C).')


if __name__ == '__main__':
    main()
