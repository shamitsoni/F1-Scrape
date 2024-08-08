from standings import driver_standings, constructor_standings
import tkinter as tk
from tkinter import messagebox


def main() -> None:
    # Called if the user wishes to retrieve driver standings
    def get_driver_standings() -> None:
        year = int(year_entry.get())
        # Show an error message if the year is invalid
        if not (1950 <= year <= 2024):
            messagebox.showerror(title='Invalid Year', message='Please enter a valid year between 1950 and 2024.')
            return
        driver_standings(year)

    # Called if the user wishes to retrieve constructor standings
    def get_constructor_standings() -> None:
        year = int(year_entry.get())
        # Show an error message if the year is invalid
        if not (1958 <= year <= 2024):
            messagebox.showerror(title='Invalid Year', message='Please enter a valid year between 1958 and 2024.')
            return
        constructor_standings(year)

    # Create instance of Tk class to act as the main GUI window
    window = tk.Tk()
    window.title("Formula One Standings")
    window.iconbitmap('f1-logo.ico')

    # Entry box to let user enter a year of choice
    tk.Label(window, text="Please Enter a Year:").grid(row=0, column=0, padx=10, pady=10)
    year_entry = tk.Entry(window)
    year_entry.grid(row=0, column=1, padx=10, pady=10)

    # Button to let user retrieve driver standings
    driver_button = tk.Button(window, text="Get Driver Standings [1950-2024]", command=get_driver_standings)
    driver_button.grid(row=1, column=0, padx=10, pady=10)

    # Button to let user retrieve constructor standings
    constructor_button = tk.Button(window, text="Get Constructor Standings [1958-2024]", command=get_constructor_standings)
    constructor_button.grid(row=1, column=1, padx=10, pady=10)

    # Window will run until the user closes it, allowing users to request data multiple times
    window.mainloop()


if __name__ == '__main__':
    main()
