import streamlit as st
import pandas as pd
import requests
import lxml

st.set_page_config(layout='wide')
st.title('Sistem Informasi Keuangan Daerah')

st.success('Data diambil dari Sistem Informasi Keuangan Daerah (SIKD) / Web djpk.kemenkeu.go.id')

bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tahun = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
wilayah = {
    '17': 'Kota Bandung'
}
# Membuat list nama untuk ditampilkan di selectbox
nama_list = list(wilayah.values())

# Membuat selectbox dengan nama
kol1, kol2, kol3 = st.columns(3)
with kol1:
    wilayah_terpilih = st.selectbox('Pilih Wilayah:', nama_list)
with kol2:
    tahun_terpilih = st.selectbox('Pilih Tahun', tahun)
with kol3:
    bulan_terpilih = st.selectbox('Pilih Bulan', bulan)

# Mendapatkan kode berdasarkan nama yang dipilih
kode_terpilih = [kode for kode, nama in wilayah.items() if nama == wilayah_terpilih][0]

if wilayah_terpilih and tahun_terpilih and bulan_terpilih:
    url = f'https://djpk.kemenkeu.go.id/portal/data/apbd?periode={bulan_terpilih}&tahun={tahun_terpilih}&provinsi=10&pemda={kode_terpilih}'
    
    # Membaca tabel HTML dari URL dan mengubahnya menjadi dataframe pandas
    dataframes = pd.read_html(url)
    
    df = dataframes[0]
    del df['Unnamed: 0']
    df = df.dropna(how='all')
    
    st.subheader(f'Realisasi APBD {wilayah_terpilih}, Bulan {bulan_terpilih}, Tahun {tahun_terpilih}')
    st.dataframe(df, hide_index=True, use_container_width=True)
    
    url2 = f'https://djpk.kemenkeu.go.id/portal/csv_apbd?type=apbd&periode={bulan_terpilih}&tahun={tahun_terpilih}&provinsi=10&pemda={kode_terpilih}'
    st.link_button('Unduh Data dalam bentuk CSV', f'{url2}')
    st.link_button('Kunjungi Web DJPK', f'https://djpk.kemenkeu.go.id/portal/data/apbd?periode={bulan_terpilih}&tahun={tahun_terpilih}&provinsi=10&pemda={kode_terpilih}')
    
st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')