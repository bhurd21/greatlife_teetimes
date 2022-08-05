import streamlit as st
from app import final
from datetime import date, time, timedelta

st.title('GreatLife Golf Course Tee Times')

with st.sidebar:
     calendar_date = st.date_input("Select a day within the current week", date.today() + timedelta(days=1)) 
     start_time, end_time = st.slider("Tee Time", value=(time(6, 00), time(9, 00)), step= timedelta(minutes=60), min_value=time(6, 00), max_value=time(18, 00))
     holes = st.radio("Number of holes", ('18', '9'))
     players = st.radio("Number of players", ('4', '3', '2', '1'))

     year, month, day = str(calendar_date).split('-')
     start_time = int(str(start_time).split(':')[0]) + 1
     end_time = int(str(end_time).split(':')[0]) - 1

dic = final(month, day, year, start_time, end_time, players, holes)

# st.subheader(str(month) + '/' + str(day) + '/' + str(year) + ' for ' + str(players) + ' players on ' + str(holes) + ' holes between ' + str(start_time - 1) + ' and ' + str(end_time + 1))
st.write('-' * 50)
try:
     for key, value in dic.items():
          st.write(key, '-', ', '.join(value))
except:
     st.write('No tee times available')