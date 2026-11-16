import streamlit as st
import pandas as pd
import numpy as np
import joblib

mo_hinh = joblib.load("Mo_hinh_hoc_vien.pkl")
st.title("Mo hinh danh gia")
st.write("Nhap thong tin: ")

col1, col2, col3 = st.columns(3)

with col1:
    tuoi = st.number_input("Tuoi", min_value = 0, max_value = 120)
with col2:
    diem = st.number_input("Diem dau vao", min_value = 0, max_value = 120)
with col3:
    nghi = st.number_input("So buoi nghi", min_value = 0, max_value = 120)
if st.button("Du doan", type = "primary"):
    du_lieu_nhap = pd.DataFrame([[tuoi, diem, nghi]], columns = ['Tuoi', 'Diem_dau_vao', 'So_buoi_vang'])
    du_doan = mo_hinh.predict(du_lieu_nhap)
    st.divider()
    if du_doan[0] == 0:
        st.error("canh bao")
    else:
        st.success("an toan")

