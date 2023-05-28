# Open file

# Read file
# Output file text
# Read line by line
# Clean each line

import re
import glob
import os

# import tkinter as tk


# def get_input(entry):
#     input_string = entry.get()

#     return input_string


# def input_window():
#     window = tk.Tk()

#     label = tk.Label(text="Enter filename:")

#     entry = tk.Entry()

#     label.pack()
#     entry.pack()

#     entry.bind("<Enter>", lambda event: get_input(entry))

#     window.mainloop()

#     input_string = entry.get()

#     return input_string


def get_txt_files_in_input_directory():
    txt_files = glob.glob("./input/*.txt")
    return txt_files


def remove_non_alphabet_and_spaces(text1):
    """Removes all non-alphabet characters and spaces from a string.

    Args:
      text: The string to remove non-alphabet characters and spaces from.

    Returns:
      A new string with all non-alphabet characters and spaces removed.
    """

    pattern = re.compile("[^a-zA-Z\n,.!?:']")
    return pattern.sub(" ", text1)


def remove_whitespaces(text2):
    """Removes whitespaces longer than one space from a string.

    Args:
      text: The string to remove whitespaces from.

    Returns:
      A new string with all whitespaces longer than one space removed.
    """

    # Replace all consecutive whitespace characters with a single space.

    text3 = re.sub("[ \t]+", " ", text2)

    # Return the new string.

    return text3


def edit_file_name(filename):
    base_name = os.path.basename(filename)
    name_without_ext = os.path.splitext(base_name)[0]
    new_name = name_without_ext + "_edited.txt"
    return new_name


def write_to_file(data, filename):
    if not os.path.exists("./output"):
        os.makedirs("./output")
    with open(f"./output/{filename}", "w") as file:
        file.write(data)


def clean_text(filename):
    with open(filename, "r") as f:
        text = f.read()

    cleaned_text = remove_non_alphabet_and_spaces(text).strip()

    formatted_text = remove_whitespaces(cleaned_text)

    new_filename = edit_file_name(filename)

    write_to_file(formatted_text, new_filename)


def main():
    """Removes all non-alphabet characters and spaces from a text file.

    Args:
      filename: The name of the text file to remove non-alphabet characters and spaces from.

    Returns:
      None.
    """  # noqa: E501
    txt_files = get_txt_files_in_input_directory()
    for file in txt_files:
        clean_text(file)


if __name__ == "__main__":
    main()
