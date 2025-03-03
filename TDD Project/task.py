# Authors: Kevin Chang, Sue Kim, Joseph Tong
# Date: 2/25/2021
# Description: CS362 W21 Group 35 Project
# Contains conv_number, my_datetime, and conv_endian functions.

import math


def char_to_int(digit_char):
    """Converts a digit or hex character to an integer."""
    characters = "0123456789abcdef"
    for i in range(len(characters)):
        if digit_char == characters[i]:
            return i
    return None


def hex_string_to_int(num_str):
    """Converts a string of digits and alpha characters a-f to an integer."""
    result = 0

    for i in range(0, len(num_str)):
        digit = char_to_int(num_str[i])  # Convert character to int digit
        power = len(num_str) - i - 1  # Order of magnitude of the digit
        result += digit * 16 ** power

    return result


def float_string_to_float(num_str, decimal_index):
    """Converts a string of digits with a decimal to a float."""
    result = 0
    power = decimal_index - 1  # Order of magnitude of the digit

    for i in range(0, len(num_str)):

        if i == decimal_index:  # Skip over decimal point
            continue

        digit = char_to_int(num_str[i])  # Convert character to int digit
        result += digit * 10 ** power
        power -= 1

    return result/1


def int_string_to_int(num_str):
    """Converts a string of digits to an integer."""
    result = 0

    for i in range(0, len(num_str)):
        digit = char_to_int(num_str[i])  # Convert character to int digit
        power = len(num_str) - i - 1  # Order of magnitude of the digit
        result += digit * 10 ** power

    return result


def get_start(num_str):
    """Returns the number of characters in the prefix."""
    start = 0

    if num_str[0] == '-':
        start = 1

    if len(num_str) > 2 and num_str[0:2] == "0x":
        start = 2

    if len(num_str) > 3 and num_str[0:3] == "-0x":
        start = 3

    return start


def check_prefix(num_str):
    """Returns True if the string starts with 0x or -0x, otherwise returns
    False."""

    if len(num_str) > 2 and num_str[0:2] == "0x":
        return True

    if len(num_str) > 3 and num_str[0:3] == "-0x":
        return True

    return False


def check_decimal(num_str, start):
    """Returns the number of decimal points in the string and the index of
    the leftmost decimal as a tuple."""

    count = 0
    index = 0
    dec_ind = -1

    for char in num_str[start:]:

        if char == '.':
            count += 1
            dec_ind = index

        index += 1

    return count, dec_ind


def check_alpha(num_str, start):
    """Returns True if the string contains the characters a-f, otherwise
    returns False."""

    hex_chars = "abcdef"

    for char in num_str[start:]:
        if char in hex_chars:
            return True

    return False


def check_invalid(num_str, start):
    """Returns True if the string contains characters other than digits,
    letters a-f, or full stop."""

    valid_chars = "0123456789abcdef."

    for char in num_str[start:]:
        if char not in valid_chars:
            return True

    return False


def check_string(val):
    """Returns True if the passed value is a non-empty string, otherwise
    returns False."""

    # Check if a non-string value was passed
    if type(val) != str:
        return False

    # Check if an empty string was passed
    if len(val) == 0:
        return False

    return True


def parse_string(num_str):
    """Helper function for conv_num. Converts an integer, float,
    or hexadecimal string into a base-10
    number."""

    result = None  # Default return value

    is_hex = check_prefix(num_str)  # Check for "0x" or "-0x" prefix
    start = get_start(num_str)  # Index of first character after prefix

    if len(num_str[start:]) == 0:  # Check if string only contains a prefix
        return result

    has_alpha = check_alpha(num_str, start)  # Check for letters a-f

    # Get the number of decimal point and the index of the leftmost decimal
    dec_count, dec_ind = check_decimal(num_str, start)

    # Check for multiple decimal points or invalid characters
    if dec_count > 1 or check_invalid(num_str, start):
        return result

    if has_alpha and not is_hex:  # Check for hex string without prefix
        return result

    if is_hex:
        if dec_count == 1:  # Check for hex string with decimal
            return result

        # Convert hex string to integer, store as result
        result = hex_string_to_int(num_str[start:])

    elif dec_count == 1:

        # Convert float string to integer, store as result
        result = float_string_to_float(num_str[start:], dec_ind)

    else:
        # Convert integer string to integer, store as result
        result = int_string_to_int(num_str[start:])

    if num_str[0] == '-':
        result *= -1

    return result


def conv_num(num_str):
    """Converts an integer, float, or hexadecimal string into a base-10
    number."""

    if not check_string(num_str):  # Ensure input is non-empty string
        return None

    # Convert alpha characters to lower case
    num_str = num_str.lower()

    result = parse_string(num_str)

    return result


def my_datetime(num_sec):
    """Converts number of seconds since Jan 1st 1970 into a date and returns it
    as a string with the format: MM-DD-YYY. """

    # convert number of seconds to days (add 1 to adjust date starting at 1-1)
    days = math.floor(num_sec/86400)+1

    # get year
    year = get_elapsed_year_days(days)[0]

    # get days remaining after year
    remaining_days = get_elapsed_year_days(days)[1]

    # get month
    month = get_month_day(year, remaining_days)[0]

    # get day
    day = math.floor(get_month_day(year, remaining_days)[1])

    # format date to string MM-DD-YY
    return "{:02}-{:02}-{}".format(month, day, year)


def get_month_day(year, remaining_days):
    """Returns the month and days elapsed given a year and remaining days"""

    # dictionary for days in each month
    days_months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # 29 days in February if leap year
    if is_leap_year(year):
        days_months[2] = 29

    for month in days_months:
        if remaining_days <= days_months[month]:
            return month, remaining_days
        remaining_days -= days_months[month]


def get_elapsed_year_days(days):
    """Given number of days after 1970, returns resulting year and remaining
    days"""
    year = 1970

    while days > 366:
        if is_leap_year(year):
            days -= 366
        else:
            days -= 365
        year += 1

    if not is_leap_year(year) and days == 366:
        year += 1
        days -= 365
    return year, days


def is_leap_year(year):
    """Given a year returns True if a leap year otherwise returns False"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def count_leap_years(end_year):
    """Returns number of leap years between 1970 and given year (not including
    the year)"""
    leap_years = 0
    for x in range(1970, end_year):
        if is_leap_year(x):
            leap_years += 1
    return leap_years


def int_to_hex_digits(num):
    """Takes in integer and returns a list of its digits of its absolute value
    in hexadecimal form"""

    remainder_list = []  # list to hold remainder values for conversion
    value = abs(num)  # absolute value of num

    while value >= 1:
        curr_remainder = value % 16
        remainder_list.append(curr_remainder)
        value = math.trunc(value / 16)

    # convert remainders into the hexadecimal digits
    hex_digits_list = hex_str_converter(remainder_list)

    # If number of digits is odd, append a 0 char for byte formatting
    if len(hex_digits_list) % 2 != 0:
        hex_digits_list.append("0")

    # Reverse list order into big endian before returning
    hex_digits_list.reverse()
    return hex_digits_list


def hex_str_converter(digit_list):
    """Converts list of numerical digits to corresponding string characters
    representing hexadecimal digits."""
    conversion_dict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    converted_hex_list = []

    for r in digit_list:
        converted_hex_list.append(conversion_dict[r])

    return converted_hex_list


def digit_to_bytes(digit_list):
    """Converts list of digits into list of bytes (2 character lengths)"""
    byte_list = []  # List to hold each byte
    for i in range(0, len(digit_list), 2):
        curr_byte = digit_list[i] + digit_list[i+1]
        byte_list.append(curr_byte)

    return byte_list


def conv_endian(num, endian='big'):
    """Converts num into hexadecimal number of given endian type. Returns
    converted number as string"""
    if endian != 'big' and endian != 'little':
        return None

    if num == 0:  # If the passed number is 0, return '00'
        return '00'

    # List created of the digits of converted hexadecimal number
    converted_digit_list = int_to_hex_digits(num)

    # List of each 2 char strings representing each byte
    bytes_list = digit_to_bytes(converted_digit_list)

    # Reverse order into little endian if endian == little
    if endian == 'little':
        bytes_list.reverse()

    space = " "

    # Converted hexadecimal number as string
    hex_num_str = space.join(bytes_list)

    if num < 0:
        hex_num_str = "-" + hex_num_str

    return hex_num_str
