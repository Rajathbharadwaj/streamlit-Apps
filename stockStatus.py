import streamlit as st
import datetime
from dummy import variable

import pandas as pd

def colorChanger(val):
    if isinstance(val, str):
        if val == 'sell' or val == "Don't buy" or val == "In Short" or val == 'No sell, but in Short':
            color = 'red'
        elif val == 'buy' or val == "In Long" or val == "No buy, but in Long":
            color = 'green'
        else:
            color = 'yellow'
        return 'color: %s' % color
    else:
        pass


st.set_page_config(
   page_title="Stock status",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded", )

st.title('Stock Status - 1 HR considered')
st.title('Legend')
st.warning("buy -> Buy immediately\n\nNo buy, but in Long/Short -> It's already in Long/Short no need to buy/sell now\n\nsell -> Short immediately\n\nIn Long -> PSAR is already in long\n\nIn Short -> \
    PSAR is already in short\n\nbuy -> Buy immediately")

df = pd.read_csv('stockStatus.csv')
df.drop('Unnamed: 0', axis=1, inplace = True)
styled = df.style.applymap(colorChanger)
# df.set_index('name', inplace=True)
st.table(styled,)
