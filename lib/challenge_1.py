# Defining the function.
def changing_to_24_hour(hour, minute, period):
    # Changing period to lowercase and checking if period is equal to "am"
    if period.lower() == "am":
        # If hour is equal to 12 we change it to 0
        if hour == 12:
            hour = 0
    else:
        # If it in pm we add 12 to the hour
        if hour != 12:
            hour += 12
    # Returning time in 24 hour format.
    return f"{hour:02d}{minute:02d}"
