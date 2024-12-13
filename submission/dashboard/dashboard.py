import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

kualitas_udara_harian = pd.read_csv('kualitas_udara_per_jam_clean.csv ', delimiter= ',')
rata_rata_tahunan = pd.read_csv('rata_rata_tahunan_clean.csv', delimiter= ',')
persentase_hari = pd.read_csv('persentase_hari_clean.csv', delimiter= ',')

kualitas_udara_harian_df = pd.DataFrame(kualitas_udara_harian)
rata_rata_tahunan_df = pd.DataFrame(rata_rata_tahunan)
persentase_hari_df = pd.DataFrame(persentase_hari)

st.title("Dashboard Proyek Analisis Data")
st.caption("By : Ahmad Zakky Arja")

st.header("Rata-rata konsentrasi polutan dalam 24 jam")
with st.container(border= True):
    pilihan = st.selectbox(
        "Pilih jenis Polutan :",
        ("PM2.5", "PM10", "SO2", "NO2", "CO", "O3"),
        index= None,
        placeholder= "Jenis polutan")

    if pilihan == "PM2.5" :
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=kualitas_udara_harian_df, x= 'hour', y='PM2.5', label='PM2.5', errorbar=None, color='#0E117A').grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata kandungan PM2.5 tertinggi ada pada pukul 20:00 dengan tingkat kandungan mencapai 77µg/m3")

    if pilihan == "PM10" :
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=kualitas_udara_harian_df, x= 'hour', y='PM10', label='PM10', errorbar=None, color='#399169').grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata kandungan PM10 tertinggi ada pada pukul 20:00 dengan tingkat kandungan mencapai 111µg/m3")
        
    if pilihan == "SO2" :
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=kualitas_udara_harian_df, x= 'hour', y='SO2', label='SO2', errorbar=None, color='#DFC516').grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata kandungan SO2 tertinggi ada pada pukul 10:00 dengan tingkat kandungan mencapai 19µg/m3")
        
    if pilihan == "NO2" :
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=kualitas_udara_harian_df, x= 'hour', y='NO2', label='NO2', errorbar=None, color='#EA5445').grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata kandungan NO2 tertinggi ada pada pukul 20:00 dengan tingkat kandungan mencapai 52µg/m3")
            
    if pilihan == "CO" :
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=kualitas_udara_harian_df, x= 'hour', y='CO', label='CO', errorbar=None, color='#EF7B3E').grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata kandungan CO tertinggi ada pada pukul 09:00 dengan tingkat kandungan mencapai 1343µg/m3")
            
    if pilihan == "O3" :
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=kualitas_udara_harian_df, x= 'hour', y='O3', label='O3', errorbar=None, color='#4D3A4D').grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata kandungan O3 tertinggi ada pada pukul 16:00 dengan tingkat kandungan mencapai 97µg/m3")

st.subheader("DataFrame Rata-rata konsentrasi polutan dalam 24 jam") 
st.dataframe(kualitas_udara_harian_df)

st.header("Rata-rata konsentrasi polutan dalam 5 tahun")
with st.container(border= True):
    pilihan_2 = st.selectbox(
        "Pilih jenis Polutan :",
        ("PM2.5 (2013-2017)", "PM10 (2013-2017)", "SO2 (2013-2017)", "NO2 (2013-2017)", "CO (2013-2017)", "O3 (2013-2017)"),
        placeholder= "Jenis polutan",
        index= None)

    if pilihan_2 == "PM2.5 (2013-2017)":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data= rata_rata_tahunan_df, x= 'year', y= 'PM2.5', label= 'PM2.5', color='#0E117A', errorbar= None).grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata tahunan polutan PM2.5 sempat mengalami kenaikan pada tahun 2013 ke 2014 sebelum mengalami penurunan secara signifikan di rentang tahun 2014 sampai 2016. Tetapi setelah itu mengalami kenaikan lagi secara signifikan sampai pada tahun 2017.")
        
    if pilihan_2 == "PM10":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data= rata_rata_tahunan_df, x= 'year', y= 'PM10', label= 'PM10', color='#399169', errorbar= None).grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata tahunan polutan PM10 mengalami kenaikan pada tahun 2013 ke tahun 2014, kemudian mengalami penurunan dua tahun berturut-turut yaitu pada tahun 2015 dan 2016 sebelum naik kembali sampai tahun 2017.")
        
    if pilihan_2 == "SO2 (2013-2017)":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data= rata_rata_tahunan_df, x= 'year', y= 'SO2', label= 'SO2', color='#DFC516', errorbar= None).grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata tahunan polutan SO2 mengalami sedikit kenaikan dari tahun 2013 ke 2014 sebelum mengalami penurunan dua tahun berturut-turut pada tahun 2015 dan 2016. Namun kembali naik pada tahun 2107.")
    
    if pilihan_2 == "NO2 (2013-2017)":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data= rata_rata_tahunan_df, x= 'year', y= 'NO2', label= 'NO2', color='#EA5445', errorbar= None).grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata tahunan polutan NO2 hanya mengalami penurunan pada tahun 2014 ke 2015. Selain itu, pada tahun 2013 ke 2014 dan 2015 ke 2017 sama-sama mengalami kenaikan.")
        
    if pilihan_2 == "CO (2013-2017)":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data= rata_rata_tahunan_df, x= 'year', y= 'CO', label= 'CO', color='#EF7B3E', errorbar= None).grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata tahunan polutan CO mengalami kenaikan pada tahun 2013 ke 2014. Lalu sempat menurun pada tahun 2015 dan 2016 sebelum Kenaikan signifikan pada 2017.")
        
    if pilihan_2 == "O3 (2013-2017)":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data= rata_rata_tahunan_df, x= 'year', y= 'O3', label= 'O3', color='#4D3A4D', errorbar= None).grid(True)
        plt.xticks(rotation=30)
        st.pyplot(fig)
        st.write("Rata-rata tahunan polutan O3 mengalami kenaikan pada tahun 2013 ke 2014. Setelah itu mengalami penurunan hingga tahun 2017.")

st.subheader("DataFrame Rata-rata konsentrasi polutan dalam 5 tahun") 
st.dataframe(rata_rata_tahunan_df)

st.header("Persentase hari dengan kualitas udara aman dan hari dengan kualitas udara melebihi batas aman")

with st.container(border= True):
    pilihan_3 = st.selectbox(
        "Pilih jenis Polutan",
        ("PM2.5 (Persentase)", "PM10 (Persentase)", "SO2 (Persentase)", "NO2 (Persentase)", "CO (Persentase)", "O3 (Persentase)"),
        placeholder= "Lihat disini",
        index= None)

    color = ('#12E2A4', '#D72324')
    
    if pilihan_3 == "PM2.5 (Persentase)":
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.pie(x= (persentase_hari_df['hari_DBA_Dalam_Batas_Aman'][0], persentase_hari_df['hari_melebihi_DBA'][0]), labels= ('aman', 'melebihi batas aman'), autopct='%1.1f%%', colors=color)    
        plt.title('PM2.5')
        plt.suptitle('PERSENTASE JUMLAH HARI DENGAN KANDUNGAN POLUTAN MELEBIHI BATAS AMAN/DALAM BATAS AMAN')
        st.pyplot(fig)
        st.write("Hanya 21,1% Dari total seluruh hari pada dataset yang rata-rata kandungan polutan PM2.5 nya masih dalam batas aman. Sedangkan sisanya 78,9% melebihi batas aman.")
        
    if pilihan_3 == "PM10 (Persentase)":
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.pie(x= (persentase_hari_df['hari_DBA_Dalam_Batas_Aman'][1], persentase_hari_df['hari_melebihi_DBA'][1]), labels= ('aman', 'melebihi batas aman'), autopct='%1.1f%%', colors=color)    
        plt.title('PM10')
        plt.suptitle('PERSENTASE JUMLAH HARI DENGAN KANDUNGAN POLUTAN MELEBIHI BATAS AMAN/DALAM BATAS AMAN')
        st.pyplot(fig)
        st.write("Hanya 33,5% Dari total seluruh hari pada dataset memiliki rata-rata kandungan polutan PM10 masih dalam batas aman. Sedangkan sisanya 66,5% melebihi batas aman.")
    
    if pilihan_3 == "SO2 (Persentase)":
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.pie(x= (persentase_hari_df['hari_DBA_Dalam_Batas_Aman'][2], persentase_hari_df['hari_melebihi_DBA'][2]), labels= ('aman', 'melebihi batas aman'), autopct='%1.1f%%', colors=color)    
        plt.title('SO2')
        plt.suptitle('PERSENTASE JUMLAH HARI DENGAN KANDUNGAN POLUTAN MELEBIHI BATAS AMAN/DALAM BATAS AMAN')
        st.pyplot(fig)
        st.write("Hanya 9,7% Dari total seluruh hari pada dataset memiliki rata-rata kandungan polutan SO2 masih dalam batas aman. Sedangkan sisanya 90,3% melebihi batas aman.")
    
    if pilihan_3 == "NO2 (Persentase)":
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.pie(x= (persentase_hari_df['hari_DBA_Dalam_Batas_Aman'][3], persentase_hari_df['hari_melebihi_DBA'][3]), labels= ('aman', 'melebihi batas aman'), autopct='%1.1f%%', colors=color)    
        plt.title('NO2')
        plt.suptitle('PERSENTASE JUMLAH HARI DENGAN KANDUNGAN POLUTAN MELEBIHI BATAS AMAN/DALAM BATAS AMAN')
        st.pyplot(fig)
        st.write("Hanya 31,5% Dari total seluruh hari pada dataset memiliki rata-rata kandungan polutan NO2 masih dalam batas aman. Sedangkan sisanya 68,5% melebihi batas aman.")
    
    if pilihan_3 == "CO (Persentase)":
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.pie(x= (persentase_hari_df['hari_DBA_Dalam_Batas_Aman'][4], persentase_hari_df['hari_melebihi_DBA'][4]), labels= ('aman', 'melebihi batas aman'), autopct='%1.1f%%', colors=color)    
        plt.title('CO')
        plt.suptitle('PERSENTASE JUMLAH HARI DENGAN KANDUNGAN POLUTAN MELEBIHI BATAS AMAN/DALAM BATAS AMAN')
        st.pyplot(fig)
        st.write("100% Atau total seluruh hari pada dataset memiliki rata-rata kandungan polutan CO melebihi batas aman.")
    
    if pilihan_3 == "O3 (Persentase)":
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.pie(x= (persentase_hari_df['hari_DBA_Dalam_Batas_Aman'][5], persentase_hari_df['hari_melebihi_DBA'][5]), labels= ('aman', 'melebihi batas aman'), autopct='%1.1f%%', colors=color)    
        plt.title('O3')
        plt.suptitle('PERSENTASE JUMLAH HARI DENGAN KANDUNGAN POLUTAN MELEBIHI BATAS AMAN/DALAM BATAS AMAN')
        st.pyplot(fig)
        st.write("Hanya 15,9% Dari total seluruh hari pada dataset yang memiliki rata-rata kandungan polutan O3 yang melebihi batas aman. Sisanya 84,1% masih dalam batas aman.")
        
st.subheader("DataFrame Persentase hari dengan kualitas udara aman dan hari dengan kualitas udara melebihi batas aman")
st.dataframe(persentase_hari_df)





    
