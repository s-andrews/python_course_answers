#!python

# We have a set of horribly inconsistent dates
# which we need to sort out.
date_strings = """2018-04-16 10:25:29 AM MDT
2018-01-05 12:05:00 PM CST
Tue Jan 02 2018 08:12:10 GMT-0600 (CST)
2018/01/01 4:50 PM HST
01/01/2018
12/02/2018"""

# Start by splitting them into individual entries
dates = date_strings.split("\n")

# Now we can process them individually and populate
# a list of results

# To convert months to numbers we need a dictionary
months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

parsed_dates = []

for date in dates:
    # Look at the first letter, if it's a number then
    # treat it differently to if it's a letter.

    if date[0].isnumeric():
        # We're going to have a delimited date in either
        # ymd or dmy and with either a / or - delimiter

        # Split off everything before the first space
        delim_date = date.split(" ")[0]

        # Find the delimiter
        delimiter = "-"
        if delimiter not in delim_date:
            delimiter = "/"
        
        # Split the date sections
        date_sections = delim_date.split(delimiter)

        # Figure out if we're dmy or ymd
        if len(date_sections[0]) == 4:
            # It's ymd
            parsed_dates.append((int(date_sections[0]), int(date_sections[1]), int(date_sections[2])))
        else:
            # It's dmy
            parsed_dates.append((int(date_sections[2]), int(date_sections[1]), int(date_sections[0])))

    else:
        # It's a text representation of 
        # text day text month num day year
        date_sections = date.split(" ")
        year = int(date_sections[3])
        day = int(2)
        month = months[date_sections[1]]

        parsed_dates.append((year,month,day))


for date in parsed_dates:
    print(f"Found date {date[0]}-{str(date[1]).zfill(2)}-{str(date[2]).zfill(2)}")
