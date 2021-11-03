import streamlit as st
import datetime
import dummy
import pandas as pd

def colorChanger(val):
    if isinstance(val, str):
        if val == 'sell' or val == "Don't buy" or val == "In Short" or val == 'No sell, but in Short' or val == 'No' or val == 'crossed below' or val == 'Less':
            color = 'red'
        elif val == 'buy' or val == "In Long" or val == "No buy, but in Long" or val == 'crossed above' or val == 'HTH' or val == 'Was HTH':
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


def displayStatus(name):

    st.title(name)

    autolist = pd.read_csv(name)
    autolist.drop('Unnamed: 0', axis=1, inplace = True)
    autostyled = autolist.style.applymap(colorChanger)
    st.table(autostyled, )




# st.title('FMCG')
# fmcglist = pd.read_csv('stockStatusind_niftyfmcglist.csv')
# fmcglist.drop('Unnamed: 0', axis=1, inplace = True)
# fmcgstyled = fmcglist.style.applymap(colorChanger)
# st.table(fmcgstyled,)

# st.title('Health Care')
# healthlist = pd.read_csv('stockStatusind_niftyhealthcarelist.csv')
# healthlist.drop('Unnamed: 0', axis=1, inplace = True)
# healthstyled = healthlist.style.applymap(colorChanger)
# st.table(healthstyled,)

# st.title('Consumer Durables')
# cdlist = pd.read_csv('stockStatusconsumer_durables.csv')
# cdlist.drop('Unnamed: 0', axis=1, inplace = True)
# cdstyled = cdlist.style.applymap(colorChanger)
# st.table(cdstyled,)
# # df.set_index('name', inplace=True)

# st.title('ALL')
# alllist = pd.read_csv('stockStatusallSymbols.csv')
# alllist.drop('Unnamed: 0', axis=1, inplace = True)
# allstyled = alllist.style.applymap(colorChanger)
# st.table(allstyled,)

if __name__ == '__main__':
    names = ['final_allBuyfinalisedSymbols.csv', 'final_stockStatusfinalisedSymbols.csv']
    
    option = st.sidebar.selectbox(
    'Which sector do you want?',
     names)

    
    try:
        displayStatus(option)
    except Exception as e:
        print(e)
        pass