import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./dashboard/main_data.csv")
df['date'] = pd.to_datetime(df[['year', 'month', 'day']]) # membuat kolom baru untuk memudahkan pemetaan tanggal

st.title("Air Quality Dashboard") # judul aplikasi
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.header("Hourly Air Quality Tracker")

    date = st.date_input("Pilih tanggal", df['date'].min()) # input tanggal 

    pollutant = st.selectbox("Pilih polutan/gas", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']) # seleksi polutan yang ingin di analisis

    new_df = df[df['date'] == pd.to_datetime(date)] # membuat dataframe baru untuk tanggal yang sudah di input, mempermudah proses visualisasi data

    # membuat line plot untuk menunjukkan perubahan kadar polutan per jam
    fig, ax = plt.subplots()
    sns.lineplot(data=new_df, x="hour", y=pollutant, ax=ax)

    st.pyplot(fig)

    # penjelasan aplikasi
    with st.expander("See explanation"):
        st.write(
            """Aplikasi ini adalah aplikasi dashboard sederhana yang menampilkan kadar polutan di kota Nongzhanguan, China.
            Aplikasi ini menunjukkan kadar polutan pada hari tertentu dan menunjukkan perubahan konsentrasi
            berbagai polutan setiap jam. Diharapkan pengguna dapat memperoleh insight tentang keadaan kualitas udara di kota tersebut
            dengan menggunakan aplikasi ini.
            (data yang dicatat hanya dari tanggal 2013-03-01 hingga 2017-02-28)
            """)

with tab2:
    st.header("Air Quality Correlation Heatmap")

    df_corr = df.drop(columns=['wd', 'station'])

    corr_matrix = df_corr.corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")

    st.pyplot(plt)

    with st.expander("See explanation"):
        st.write(
            """Diagram di atas merupakan sebuah heatmap yang menunjukkan korelasi(correlation) antar fitur.
            Dari gambar ini dapat diketahui bahhwa beberapa polutan memiliki korelasi yang tinggi satu dengan yang lainnya.
            Sebagai contoh CO dengan PM2.5 memiliki korelasi yang cukup tinggi (0.81), hal ini menandakan bahwa
            kedua zat tersebut memiliki kemungkinan berasal dari sumber yang sama. Jika ditelusuri lebih
            lanjut, PM2.5 merupakan partikel yang berukuran 2.5 micrometer. pada umumnya, partikel ini dihasilkan oleh emisi kendaraan
            dan juga limbah pabrik, yang mana kedua hal tersebut juga menjadi sumber emisi CO.
            Heatmap ini dapat memberikan insight lebih dalam tentang kualitas udara, meskipun tidak ditemukan bahwa hujan dan temperatur memiliki
            korelasi yang tinggi seperti pertanyaan analisis yang pada awalnya menjadi topik analisis.
            """)
