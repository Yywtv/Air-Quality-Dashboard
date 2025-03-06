import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./dashboard/main_data.csv")
df['date'] = pd.to_datetime(df[['year', 'month', 'day']]) # membuat kolom baru untuk memudahkan pemetaan tanggal

st.title("Hourly Air Quality Tracker") # judul aplikasi

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
