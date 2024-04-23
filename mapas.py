import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
   np.random.randn(100, 2) / [50, 50] + [18.882706, -97.061378],
   columns=['lat', 'lon']
)
st.dataframe(map_data)
st.map(map_data)
