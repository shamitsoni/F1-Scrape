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
        # Map each button to the selected option
        button_map = {'driver': driver_button, 'constructor': constructor_button, 'race': race_results_button}

        # Highlight the button corresponding to the selected option and un-highlight all other buttons
        for option, button in button_map.items():
            if selected_option == option:
                button.config(bg='#34eb65')
            else:
                button.config(bg='SystemButtonFace')

    # Called to set the selected format option
    def set_format_type(option: str) -> None:
        global selected_option
        selected_option = option
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

        # Sets the ranges for valid years based on the format type
        if selected_option == 'constructor':
            min_year, max_year = 1958, 2024
        else:
            min_year, max_year = 1950, 2024

        # Gives error if the user picks an invalid year
        if not (min_year <= year <= max_year):
            messagebox.showerror(title='Invalid Year', message=f'Please enter a valid year between {min_year} and {max_year}.')
            return

        # Gives warning if the user picks the current season
        if year == CURRENT_YEAR:
            messagebox.showwarning(title='Stats in Progress',
                                   message='This season is currently ongoing! Stats are subject to change.')

        # Map options to corresponding functions
        format_map = {'driver': driver_standings, 'constructor': constructor_standings, 'race': race_results}

        # Send an error if the user tries to retrieve data without selecting an option
        if selected_option not in format_map.keys():
            messagebox.showerror(title='No Option Selected', message='Please select a standings format before requesting data!')
        else:
            format_map[selected_option](year)

    # Create instance of Tk class to act as the main GUI window
    window = tk.Tk()
    window.title("Formula One Standings")
    window.iconbitmap('f1-logo.ico')

    # Entry box to let user enter a year of choice
    tk.Label(window, text="Please Enter a Year:").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    year_entry = tk.Entry(window)
    year_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    # Button to select driver standings
    driver_button = tk.Button(window, text="Get Driver Standings [1950-2024]", command=lambda: set_format_type('driver'))
    driver_button.grid(row=1, column=0, padx=10, pady=10)

    # Button to select constructor standings
    constructor_button = tk.Button(window, text="Get Constructor Standings [1958-2024]", command=lambda: set_format_type('constructor'))
    constructor_button.grid(row=1, column=1, padx=10, pady=10)

    # Button to select race results
    race_results_button = tk.Button(window, text="Get Race Results [1950-2024]", command=lambda: set_format_type('race'))
    race_results_button.grid(row=1, column=2, padx=10, pady=10)

    # Button to retrieve standings
    retrieve_button = tk.Button(window, text="Retrieve Standings", command=retrieve_standings, height=1, width=25, bg='#f2c7d3')
    retrieve_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Window will run until the user closes it, allowing users to request data multiple times
    window.mainloop()


if __name__ == '__main__':
    main()
