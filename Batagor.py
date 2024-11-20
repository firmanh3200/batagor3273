import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':orange[+++] B A T A :green[G] :blue[O R] :orange[+++]')
st.subheader('BANDUNG KOTA :orange[dalam] :green[GRAFIK] :orange[dan] :blue[INDIKATOR]', divider='rainbow')

with st.expander('PENGANTAR'):
    st.success('Aplikasi ini berisi kumpulan Indikator Makro yang resmi dirilis oleh Badan Pusat Statistik, \
        ditambah data-data lain yang sumber resminya tercantum.')
    st.info('Aplikasi ini dibuat untuk memudahkan Para Pemangku Kepentingan dalam proses Perencanaan, Pelaksanaan, \
        Monitoring dan Evaluasi Pembangunan di Kota Bandung.')
    st.warning('Silakan mengakses setiap indikator makro melalui menu di sebelah kiri.')

st.subheader('', divider='green')

kol1, kol2, kol3, kol4, kol5 = st.columns(5)
with kol1:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':green[Luas Wilayah (Km2)]')
            st.header(':green[167,31]')

with kol2:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':blue[Jumlah Kecamatan]')
            st.header(':blue[30]')

with kol3:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':orange[Jumlah Kelurahan]')
            st.header(':orange[151]')

with kol4:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':blue[Rukun Warga (RW)]')
            st.header(':blue[1.598]')

with kol5:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':green[Rukun Tetangga (RT)]')
            st.header(':green[9.951]')
            
with st.expander('Catatan'):
    st.caption('Jumlah RW dan RT berdasarkan Master Satuan Lingkungan Setempat Semester 1 Tahun 2023')

st.subheader('', divider='green')

# LUAS KECAMATAN
with st.container(border=True):
    st.subheader('Luas Kota Bandung menurut Kecamatan (Hektar)')

    # URL luas wilayah
    url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/luas_wilayah_kota_bandung_berdasarkan_kecamatan"

    # Fungsi untuk mengambil data dari setiap halaman
    def fetch_data(url, page):
        response = requests.get(url, params={'page': page})
        data = response.json()
        return data

    # Mengambil semua data dengan memperhatikan pagination
    all_data = []
    page = 1
    while True:
        data = fetch_data(url, page)
        if 'data' in data:
            all_data.extend(data['data'])
            if data['pagination']['has_next']:
                page += 1
            else:
                break
        else:
            break

    # Memfilter data untuk tahun 2023
    dataluas2023 = [item for item in all_data if item['tahun'] == 2023]

    # Mengubah data yang sudah difilter menjadi pandas dataframe
    df = pd.DataFrame(dataluas2023)
    df_luas = df[['kemendagri_nama_kecamatan', 'luas_wilayah', 'satuan', 'tahun']]

    trimep = px.treemap(df, path=['bps_nama_kabupaten_kota', 'kemendagri_nama_kecamatan'],
                        values='luas_wilayah')

    paycart = px.pie(df, values='luas_wilayah', color='kemendagri_nama_kecamatan')

    kol6, kol7 = st.columns(2)
    with kol6:
        st.plotly_chart(trimep, use_container_width=True)

    with kol7:
        st.plotly_chart(paycart, use_container_width=True)

    # Menampilkan dataframe
    with st.expander('Lihat Tabel'):
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/luas-wilayah-kota-bandung-berdasarkan-kecamatan')

st.subheader('', divider='rainbow')