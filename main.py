from standings import driver_standings, constructor_standings
from race_results import race_results
import tkinter as tk
from tkinter import messagebox

# Defines the year for the ongoing F1 season
CURRENT_YEAR = 2024

# Store the selected format type
selected_option = None


def main() -> None:
    # Updates the color of buttons to indicate the selected option
    def update_button_styles() -> None:
        global selected_option
        if selected_option == 'driver':
            driver_button.config(bg='#34eb65')
            constructor_button.config(bg='SystemButtonFace')
            race_results_button.config(bg='SystemButtonFace')
        elif selected_option == 'constructor':
            constructor_button.config(bg='#34eb65')
            driver_button.config(bg='SystemButtonFace')
            race_results_button.config(bg='SystemButtonFace')
        elif selected_option == 'race':
            race_results_button.config(bg='#34eb65')
            driver_button.config(bg='SystemButtonFace')
            constructor_button.config(bg='SystemButtonFace')
        else:
            driver_button.config(bg='SystemButtonFace')
            constructor_button.config(bg='SystemButtonFace')
            race_results_button.config(bg='SystemButtonFace')

    # Called if the user wishes to retrieve driver standings
    def set_driver_standings() -> None:
        global selected_option
        selected_option = 'driver'
        update_button_styles()

    # Called if the user wishes to retrieve constructor standings
    def set_constructor_standings() -> None:
        global selected_option
        selected_option = 'constructor'
        update_button_styles()

    def set_race_results() -> None:
        global selected_option
        selected_option = 'race'
        update_button_styles()

    # Check if the inserted year is a number
    def valid_year(year: str) -> bool:
        # If year is not a number: return and send error message
        if not year.isdigit():
            messagebox.showerror(title='Invalid Year', message='Please enter the year as an integer.')
            return False
        return True

    # Makes sure all inputs are valid and retrieves data
    def retrieve_standings() -> None:
        # Retrieve the selected year as a string
        year = year_entry.get()
        # Checks if the year is a number and returns, else converts year to integer for use in stats retrieval
        if not valid_year(year):
            return
        else:
            year = int(year)

        # If user selects get driver standings button
        if selected_option == 'driver':
            # Show an error message if the year is invalid
            if not (1950 <= year <= 2024):
                messagebox.showerror(title='Invalid WDC Year', message='Please enter a valid year between 1950 and 2024.')
                return

            # Warns the user that stats can change for the ongoing season
            if year == CURRENT_YEAR:
                messagebox.showwarning(title='Stats in Progress',
                                       message='This season is currently ongoing! Stats are subject to change.')

            # Retrieve Data
            driver_standings(year)

        # If user selects get constructor standings button
        elif selected_option == 'constructor':
            # Show an error message if the year is invalid
            if not (1958 <= year <= 2024):
                messagebox.showerror(title='Invalid WCC Year', message='Please enter a valid year between 1958 and 2024.')
                return

            # Warns the user that stats can change for the ongoing season
            if year == CURRENT_YEAR:
                messagebox.showwarning(title='Stats in Progress',
                                       message='This season is currently ongoing! Stats are subject to change.')

            # Retrieve Data
            constructor_standings(year)

        # If user selects get constructor standings button
        elif selected_option == 'race':
            # Show an error message if the year is invalid
            if not (1950 <= year <= 2024):
                messagebox.showerror(title='Invalid WDC Year',
                                     message='Please enter a valid year between 1950 and 2024.')
                return

            # Warns the user that stats can change for the ongoing season
            if year == CURRENT_YEAR:
                messagebox.showwarning(title='Stats in Progress',
                                       message='This season is currently ongoing! Stats are subject to change.')

            # Retrieve Data
            race_results(year)

        # If the user tries to retrieve data without selecting an option
        else:
            messagebox.showerror(title='No Option Selected',
                                 message='Please select a standings format before requesting data!')

    # Create instance of Tk class to act as the main GUI window
    window = tk.Tk()
    window.title("Formula One Standings")
    window.iconbitmap('f1-logo.ico')

    # Entry box to let user enter a year of choice
    tk.Label(window, text="Please Enter a Year:").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    year_entry = tk.Entry(window)
    year_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    # Button to select driver standings
    driver_button = tk.Button(window, text="Get Driver Standings [1950-2024]", command=set_driver_standings)
    driver_button.grid(row=1, column=0, padx=10, pady=10)

    # Button to select constructor standings
    constructor_button = tk.Button(window, text="Get Constructor Standings [1958-2024]", command=set_constructor_standings)
    constructor_button.grid(row=1, column=1, padx=10, pady=10)

    # Button to select race results
    race_results_button = tk.Button(window, text="Get Race Results [1950-2024]", command=set_race_results)
    race_results_button.grid(row=1, column=2, padx=10, pady=10)

    # Button to retrieve standings
    retrieve_button = tk.Button(window, text="Retrieve Standings", command=retrieve_standings, height=1, width=25, bg='#f2c7d3')
    retrieve_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Window will run until the user closes it, allowing users to request data multiple times
    window.mainloop()


if __name__ == '__main__':
    main()
