import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':orange[STATISTIK] :blue[KEPENDUDUKAN] :green[KOTA BANDUNG]')
#st.subheader('BANDUNG KOTA :orange[dalam] :green[GRAFIK] :orange[dan] :blue[INDIKATOR]', divider='rainbow')
st.subheader('', divider='rainbow')

# URL API Open Data
url = "https://opendata.bandung.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_kota_bandung_berdasarkan_kelurahan"

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
    
# Menarik semua data
data_penduduk = [item for item in all_data]

# Mengubah data menjadi pandas dataframe
df = pd.DataFrame(data_penduduk)

# Menghitung series tahunan
df_juni = df[df['semester'] == 1]

df_tahun = df_juni.groupby(['bps_nama_kabupaten_kota', 'tahun'])['jumlah_penduduk'].sum().reset_index()

# Menampilkan grafik tahunan
with st.container(border=True):
    fig1 = px.bar(df_tahun, x='tahun', y='jumlah_penduduk')
    st.subheader('Perkembangan Jumlah Penduduk Kota Bandung')
    st.plotly_chart(fig1, use_container_width=True)
    with st.expander('Catatan'):
        st.caption('Catatan: Kondisi pertengahan tahun/ Semester 1')
        st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-kelurahan')

# # Membuat kolom Semester
# df['Semester'] = df['tahun'].astype(str) + '-' + df['semester'].astype(str)

# # Menghitung series semesteran
# df_semester = df.groupby('Semester')['jumlah_penduduk'].sum().reset_index()

with st.container(border=True):
    df_kec = df.sort_values(by=['tahun', 'semester'], ascending=False)
    tahun = df_kec['tahun'].unique()
    semester = df_kec['semester'].unique()
    
    kol1, kol2 = st.columns(2)
    with kol1:
        tahun_terpilih = st.selectbox('Filter Tahun', tahun)
    
    with kol2:
        semester_terpilih = st.selectbox('Filter Semester', semester)
    
    if tahun_terpilih and semester_terpilih:
        st.subheader(f'Penduduk Kota Bandung menurut Kecamatan, Semester {semester_terpilih} {tahun_terpilih}')
        df_terpilih = df[(df['tahun'] == tahun_terpilih) & (df['semester'] == semester_terpilih)]
        
        kol1a, kol1b = st.columns(2)
        with kol1a:
            fig2 = px.treemap(df_terpilih, path=['bps_nama_kabupaten_kota', 'kemendagri_nama_kecamatan'],
                              values='jumlah_penduduk')
            st.plotly_chart(fig2, use_container_width=True)
            
        with kol1b:
            fig3 = px.pie(df_terpilih, values='jumlah_penduduk', names='kemendagri_nama_kecamatan')
            st.plotly_chart(fig3, use_container_width=True)

# Penduduk Kelurahan
with st.expander('Penduduk menurut Kelurahan'):
    kecamatan = df['kemendagri_nama_kecamatan'].unique()
    kec_terpilih = st.selectbox('Filter Kecamatan', kecamatan)
    
    if kec_terpilih:
        df_kec = df_terpilih[df_terpilih['kemendagri_nama_kecamatan'] == kec_terpilih]
        st.subheader(f'Penduduk Kecamatan {kec_terpilih}, Semester {semester_terpilih} {tahun_terpilih}')
        
        kol2a, kol2b = st.columns(2)
        with kol2a:
            fig4 = px.treemap(df_kec, path=['kemendagri_nama_kecamatan', 'kemendagri_nama_desa_kelurahan'],
                              values='jumlah_penduduk')
            st.plotly_chart(fig4, use_container_width=True)
        
        with kol2b:
            fig5 = px.pie(df_kec, values='jumlah_penduduk', names='kemendagri_nama_desa_kelurahan')
            st.plotly_chart(fig5, use_container_width=True)


# Tampilkan pada streamlit
with st.expander('Lihat Tabel Lengkap'):
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption('Sumber: https://opendata.bandung.go.id/dataset/jumlah-penduduk-kota-bandung-berdasarkan-kelurahan')
    
st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')