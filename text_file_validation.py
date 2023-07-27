import re
import csv
import os


def isbn_validation(isbn):
    return bool(re.match(r"^\d{9}(\d|X)$", isbn))


def price_validation(price):
    return bool(re.match(r"^\s*\d+(?:[,.]\d{1,2})?\s*(?:€|Kč)$", price))


def validate_line(line, line_num):
    data = line.strip().split(";")
    if len(data) != 4:
        print(f"Error! Line {line_num}: Expected 4 columns, found {len(data)}: {line}")
        return

    book_name, author_name, isbn, price = data

    if not book_name.strip():
        print(f"Error! Line {line_num}: Missing title.")
    if not author_name.strip():
        print(f"Error! Line {line_num}: Missing author.")
    if not isbn.strip():
        print(f"Error! Line {line_num}: Missing ISBN.")
    elif not isbn_validation(isbn):
        print(f"Error! Line {line_num}: Invalid ISBN format.")
    if not price.strip():
        print(f"Error! Line {line_num}: Missing price.")
    elif not price_validation(price):
        print(f"Error! Line {line_num}: Invalid price format.")


def validate_csv_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error! File '{file_path}' not found.")
        return

	
    with open(file_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            validate_line(line, line_num)


if __name__ == "__main__":
    file_path = input(
        "Enter the name of the CSV file to validate (e.g., books.csv): "
    ).strip()
    if not file_path:
        print("Error! File name cannot be empty.")
    else:
        validate_csv_file(file_path)
