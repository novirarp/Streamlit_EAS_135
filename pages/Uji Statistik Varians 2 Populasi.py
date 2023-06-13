import streamlit as st
import numpy as np
from scipy import stats

def perform_f_test(population1, population2):
    f_stat, p_value = stats.f_oneway(population1, population2)
    return f_stat, p_value

def main():
    st.title("Aplikasi Uji Statistik Varians 2 Populasi")
    st.write("Masukkan data untuk kedua populasi di bawah ini:")

    # Memasukkan data populasi pertama
    population1_data = st.text_input("Populasi 1 (pisahkan dengan koma):")
    population1_data = [float(x.strip()) for x in population1_data.split(',') if x.strip()]

    # Memasukkan data populasi kedua
    population2_data = st.text_input("Populasi 2 (pisahkan dengan koma):")
    population2_data = [float(x.strip()) for x in population2_data.split(',') if x.strip()]

    if st.button("Hitung"):
        # Melakukan uji F-test
        f_stat, p_value = perform_f_test(population1_data, population2_data)

        # Menampilkan hasil
        st.write("Hasil Uji F-Test:")
        st.write("F-Statistic:", f_stat)
        st.write("P-Value:", p_value)

if __name__ == '__main__':
    main()
