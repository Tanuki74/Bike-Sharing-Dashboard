import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='whitegrid')

data = pd.read_csv('./dashboard/day_cleaned.csv')

st.title('🚲 Bike Sharing Dashboard')
st.markdown("Selamat datang di **Bike Sharing Dashboard**! Di sini Anda bisa melihat analisis penyewaan sepeda berdasarkan berbagai faktor seperti hari kerja, hari libur, dan kondisi cuaca.")

st.markdown("""
### Insight:
- **Bussiness Question 1**: What are the patterns of bicycle use on weekdays compared to holidays?
- **Bussiness Question 2**: How does weather conditions affect bicycle usage?
""")

st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input('Mulai dari', pd.to_datetime(data['dteday']).min())
end_date = st.sidebar.date_input('Sampai dengan', pd.to_datetime(data['dteday']).max())

data['dteday'] = pd.to_datetime(data['dteday'])
filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]

with st.container():
    st.write('## 🔄 Distribusi Penyewaan Sepeda pada Hari Kerja dan Hari Libur')

    working_day = filtered_data[filtered_data['workingday'] == 1]['cnt']
    holiday = filtered_data[filtered_data['holiday'] == 1]['cnt']

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(working_day, color='blue', kde=True, label='Hari Kerja', ax=ax)
    sns.histplot(holiday, color='red', kde=True, label='Hari Libur', ax=ax)
    
    ax.set_title("Distribusi Penyewaan Sepeda pada Hari Kerja dan Hari Libur", fontsize=16)
    ax.set_xlabel("Total Penyewaan Sepeda", fontsize=12)
    ax.set_ylabel("Frekuensi", fontsize=12)
    ax.legend()

    st.pyplot(fig)

    with st.expander('💡 Penjelasan'):
        st.write("""
        Pada hari kerja, penyewaan sepeda memiliki variasi yang lebih luas, menunjukkan perbedaan aktivitas. 
        Di sisi lain, hari libur memiliki penyewaan sepeda yang lebih stabil dan cenderung di sekitar angka yang lebih rendah.
        """)

with st.container():
    st.write('## 🌧️ Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda')

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x='weathersit', y='cnt', data=filtered_data, ax=ax, palette="Set2")
    
    ax.set_title('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda', fontsize=16)
    ax.set_xlabel('Kondisi Cuaca', fontsize=12)
    ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['Cerah', 'Berkabut + Berawan', 'Hujan/Snow Ringan'])

    st.pyplot(fig)

    with st.expander('💡 Penjelasan'):
        st.write("""
        Cuaca cerah meningkatkan penggunaan sepeda secara signifikan, dengan variasi penggunaan yang lebih besar. 
        Cuaca berkabut atau berawan masih mendukung penggunaan sepeda yang cukup signifikan. 
        Namun, hujan atau salju ringan mulai menurunkan tingkat penggunaan, sementara hujan atau salju lebat hampir menghentikan aktivitas bersepeda.
        """)

st.write("Dashboard ini dibangun menggunakan data Bike Sharing untuk memvisualisasikan pola penyewaan sepeda berdasarkan hari dan kondisi cuaca.")
