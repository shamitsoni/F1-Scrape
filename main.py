from exceptions import InvalidYear, InvalidFormat
from standings import driver_standings, constructor_standings


def main() -> None:
    # Prompts user for selection
    print('Welcome! Which type of F1 data would you like?')
    standing_type = input('(D) Driver Standings | (C) Constructor Standings: ')

    # User selects driver standings
    if standing_type.strip().lower() == 'd':
        # Driver standings must start at earliest 1950
        year = int(input('Enter a year [1950-2024]: '))
        # Year is invalid -> raise exception
        if not (1950 <= year <= 2024):
            raise InvalidYear('Please enter a valid year between 1950 and 2024.')
        # Retrieve data
        driver_standings(year)

    # User selects constructors standings
    elif standing_type.strip().lower() == 'c':
        # Unlike driver standings, constructor standings must start at earliest 1958
        year = int(input('Enter a year [1958-2024]: '))
        # Year is invalid -> raise exception
        if not (1958 <= year <= 2024):
            raise InvalidYear('Please enter a valid year between 1958 and 2024.')
        # Retrieve data
        constructor_standings(year)

    # User selected an invalid standing type -> raise exception
    else:
        raise InvalidFormat('Please enter a valid format: (D) or (C).')


if __name__ == '__main__':
    main()
