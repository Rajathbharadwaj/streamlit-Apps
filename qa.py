import streamlit as st
import datetime
import pandas as pd
from dummy import variable

import pandas as pd

st.set_page_config(
   page_title="Traded status",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded", )
# {str(datetime.date.today())}.txt


def colorChanger(val):
    if isinstance(val, float):
        color = 'red' if val < 0 else 'green'
        return 'color: %s' % color
    else:
        pass


df = pd.read_csv('QA.csv')
# print(df.head())

st.title('Rasa')
four = df[['user', 'rasa', 'blenderbot_400M_distill', 'DialoGPT_medium',
       'QA_answers']].iloc[4+1]
st.table(four)

seven = df[['user', 'rasa', 'blenderbot_400M_distill', 'DialoGPT_medium',
       'QA_answers']].iloc[7+1]
st.table(seven)

_11 = df[['user', 'rasa', 'blenderbot_400M_distill', 'DialoGPT_medium',
       'QA_answers']].iloc[11+1]
st.table(_11)

st.title('Blenderbot')
_2 = df[['user', 'rasa', 'blenderbot_400M_distill', 'QA_answers']].iloc[0]
st.table(_2)

st.title('DialoGPT')
_18 = df[['user', 'rasa', 'blenderbot_400M_distill', 'DialoGPT_medium',
       'QA_answers']].iloc[18+1]
st.table(_18)



    
