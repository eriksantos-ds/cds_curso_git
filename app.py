import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    return pd.read_csv('data/precessed/bikes_completes.csv')

def main():
    df = load_data()

    st.dataframe(df)

if__name__  == '__main__':
   main()