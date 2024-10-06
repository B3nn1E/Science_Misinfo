import streamlit as st
import pandas as pd
import os

#Search bar
st.set_page_config (page_title="Welcome!", page_icon=":robot:", layout="wide") 
url = st.text_input ("Please enter your URL here 👇")

#Check for csv file
csv_file = "data/Web.csv"

#Input url
if url:
    if os.path.exists(csv_file): #read the csv file if exists
        web = pd.read_csv(csv_file)
    else: #create dataframe if doesn't
        web = pd.DataFrame(columns=['Website'])

    #Cannot use append so concat instead
    web = pd.concat([web, pd.DataFrame([url], columns = ['Website'])], axis = 0, join = 'outer', ignore_index=True)

    #Save to csv file
    with open('data/Web.csv', 'w') as f:
        web.to_csv(f, index=False)
        
    #Try to make hyperlink (fail for now)
    def make_clickable(url):
        return f'<a target="_blank" href="{url}">{url}</a>'
    st.write(web.style.format({'Website': make_clickable}))

