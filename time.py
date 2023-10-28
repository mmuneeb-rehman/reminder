import streamlit as st
import datetime

st.title("Date and Time Calculator")

year = st.text_input("Enter the year (YYYY):")
month = st.text_input("Enter the month (MM):")
day = st.text_input("Enter the day of the month (D):")
hour = st.text_input("Enter the hour (0-23):")
minute = st.text_input("Enter the minute (0-59):")
am_pm = st.selectbox("Select AM or PM:", ["AM", "PM"])
reminder_message = st.text_input("Enter reminder message:")
save_to_file = st.button("Save to File")

reminder_time = None

try:
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    hour_int = int(hour)
    minute_int = int(minute)

    if am_pm == "PM" and hour_int != 12:
        hour_int += 12
    elif am_pm == "AM" and hour_int == 12:
        hour_int = 0

    reminder_time = datetime.datetime(year_int, month_int, day_int, hour_int, minute_int)
except ValueError:
    st.write("Invalid date and time. Please enter valid values.")

if save_to_file:
    reminder = f"Reminder: {reminder_message}\nTime: {reminder_time.strftime('%I:%M %p %Z time on %m/%d/%Y')}"
    with open("reminder.txt", "w") as file:
        file.write(reminder)
    st.write("File Saved Sucessfully")