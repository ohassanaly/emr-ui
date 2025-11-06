import json

import streamlit as st

with open("data/tazi_records.json", "r") as f:
    json_data = json.load(f)

rghc = st.text_input("rghc", placeholder="Enter a rghc to access its record")

if rghc:
    if rghc in list(json_data.keys()):
        st.json({k: v for k, v in json_data[rghc].items() if v != ""})
else:
    st.info("invalid rghc")
