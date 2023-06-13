import streamlit as st
import numpy as np
from scipy import stats

def perform_ttest(population1, population2):
    t_stat, p_value = stats.ttest_ind(population1, population2)
    return t_stat, p_value

def main():
    st.title("Aplikasi Uji Statistik Rata-rata 2 Populasi")
    st.write("Masukkan data untuk kedua populasi di bawah ini:")

    # Memasukkan data populasi pertama
    population1_data = st.text_input("Populasi 1 (pisahkan dengan koma):")
    population1_data = [float(x.strip()) for x in population1_data.split(',') if x.strip()]

    # Memasukkan data populasi kedua
    population2_data = st.text_input("Populasi 2 (pisahkan dengan koma):")
    population2_data = [float(x.strip()) for x in population2_data.split(',') if x.strip()]

    if st.button("Hitung"):
        # Melakukan uji t-test
        t_stat, p_value = perform_ttest(population1_data, population2_data)

        # Menampilkan hasil
        st.write("Hasil Uji T-Test:")
        st.write("T-Statistic:", t_stat)
        st.write("P-Value:", p_value)

if __name__ == '__main__':
    main()
