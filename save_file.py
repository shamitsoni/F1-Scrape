from tkinter import messagebox


def save_to_txt(file_path, headers, data, column_widths, year):
    if not file_path:
        return

    with open(file_path, 'w') as file:
        file.write(f'{headers[0]} FORMULA ONE RESULTS\n\n')
        header_line = ' '.join([f'{header:<{width}}' for header, width in zip(headers, column_widths)])
        file.write(header_line + '\n')
        for row in zip(*data):
            line = ' '.join([f'{item:<{width}}' for item, width in zip(row, column_widths)])
            file.write(line + '\n')

    # Show confirmation message
    messagebox.showinfo("Success", f'F1 data for {year} have been saved to {file_path}')


def export_to_excel(file_path, df, year):
    if not file_path:
        return

    # Export DataFrame to Excel file
    df.to_excel(file_path, index=False)

    # Show confirmation message
    messagebox.showinfo("Success", f'F1 data for {year} have been saved to {file_path}')
