from sqlalchemy import create_engine
import pandas as pd
from connect_db import db_connect
from call_gpt import execute_query

def execute_query_on_db(question):
    engine = db_connect()
    query = execute_query(question)
    df = pd.read_sql(query, engine)
    return df.iloc[0, 0]


## make a streamlit application
import streamlit as st  
st.title("Electoral Bonds")

txt_input = st.text_input("Enter the question: ")
if st.button("Submit"):
    # st.write(execute_query(txt_input))
    st.write(execute_query_on_db(txt_input))