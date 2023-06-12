import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1g9Qd6nnuRW9msVXQg3O1v91cx_7UWTP-vrcptdZgIP8/edit?hl=id#gid=658586720')

df