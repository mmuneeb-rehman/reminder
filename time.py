import streamlit as st
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.title("Date and Time Calculator")

year = st.text_input("Enter the year (YYYY):")
month = st.text_input("Enter the month (MM):")
day = st.text_input("Enter the day of the month (D):")
hour = st.text_input("Enter the hour (0-23):")
minute = st.text_input("Enter the minute (0-59):")
am_pm = st.selectbox("Select AM or PM:", ["AM", "PM"])
reminder_message = st.text_input("Enter reminder message:")
save_to_file = st.button("Save to PDF")

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
    pdf_filename = "reminder.pdf"

    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 750, "Reminder:")
    c.drawString(100, 730, reminder_message)
    c.drawString(100, 710, "Time:")
    c.drawString(100, 690, reminder_time.strftime('%I:%M %p %Z time on %m/%d/%Y'))
    c.save()

    st.write("PDF Saved Successfully")

    # Provide a download link to the user
    st.markdown(get_binary_file_downloader_html(pdf_filename, "Download Reminder PDF"), unsafe_allow_html=True)
