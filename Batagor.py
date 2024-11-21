import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':orange[STATISTIK] :blue[DAERAH] :green[KOTA BANDUNG]')
#st.subheader('BANDUNG KOTA :orange[dalam] :green[GRAFIK] :orange[dan] :blue[INDIKATOR]', divider='rainbow')
st.subheader('', divider='rainbow')

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
            st.header(':blue[1.595]')

with kol5:
    with st.container(border=True):
        with st.container(border=True):
            st.subheader(':green[Rukun Tetangga (RT)]')
            st.header(':green[9.950]')
            
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

    paycart = px.pie(df, values='luas_wilayah', color='kemendagri_nama_kecamatan',
                     names='kemendagri_nama_kecamatan')

    kol6, kol7 = st.columns(2)
    with kol6:
        st.plotly_chart(trimep, use_container_width=True)

    with kol7:
        st.plotly_chart(paycart, use_container_width=True)

    # Menampilkan dataframe
    with st.expander('Lihat Tabel'):
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/luas-wilayah-kota-bandung-berdasarkan-kecamatan')

st.subheader('', divider='green')

with st.container(border=True):
    pilihan = ['Jumlah RW', 'Jumlah RT']

    kategori_terpilih = st.selectbox('Pilih Kategori Data', pilihan)

    datarw = pd.read_excel('data/listrw.xlsx')
    
    datart = pd.read_excel('data/listrt.xlsx')
        
    if kategori_terpilih == 'Jumlah RW':
        
        # Menghitung jumlah RW per kecamatan
        jumlah_rw = datarw.groupby(['nmkab', 'nmkec', 'nmdesa'])['nmrw'].count().reset_index(name='jumlah_rw')
        
        st.subheader('Jumlah RW menurut Kecamatan')
        kol1a, kol2a = st.columns(2)
        with kol1a:
            fig = px.treemap(jumlah_rw, path=['nmkab', 'nmkec'], values='jumlah_rw')
            st.plotly_chart(fig, use_container_width=True)

        with kol2a:
            fig2 = px.pie(jumlah_rw, values='jumlah_rw', names='nmkec')
            st.plotly_chart(fig2, use_container_width=True)
            
    if kategori_terpilih == 'Jumlah RT':
        
        # Menghitung jumlah RT per kecamatan
        jumlah_rt = datart.groupby(['nmkab', 'nmkec', 'nmdesa'])['nmrt'].count().reset_index(name='jumlah_rt')
        
        st.subheader('Jumlah RT menurut Kecamatan')
        kol1a, kol2a = st.columns(2)
        with kol1a:
            fig = px.treemap(jumlah_rt, path=['nmkab', 'nmkec'], values='jumlah_rt')
            st.plotly_chart(fig, use_container_width=True)

        with kol2a:
            fig2 = px.pie(jumlah_rt, values='jumlah_rt', names='nmkec')
            st.plotly_chart(fig2, use_container_width=True)
    
    with st.expander('Lihat Daftar RT RW'):
        st.dataframe(datart, use_container_width=True, hide_index=True)
        st.caption('Catatan: Jika ada perbedaan dengan kondisi terkini di wilayah Anda, silakan hubungi kami')

st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')