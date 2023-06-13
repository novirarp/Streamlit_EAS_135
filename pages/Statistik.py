import streamlit as st
import numpy as np

def main():
    st.title("Aplikasi Perhitungan Statistika")

    # Menerima input data dari pengguna
    st.subheader("Masukkan data (pisahkan dengan koma):")
    data = st.text_area("Data, tekan ctrl+enter setelah input data", )

    # Mengubah data menjadi array
    data = [float(x.strip()) for x in data.split(",")]

    # Menghitung statistika
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)

    # Menampilkan hasil
    st.subheader("Hasil Perhitungan:")
    st.write("Mean:", mean)
    st.write("Median:", median)
    st.write("Standar Deviasi:", std_dev)

if __name__ == "__main__":
    main()
