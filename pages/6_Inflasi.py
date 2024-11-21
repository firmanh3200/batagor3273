import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Inflasi Kota Bandung')
st.subheader('', divider='rainbow')

datafull = pd.read_excel('data/inflasi.xlsx')
datafull['Tahun'] = datafull['Tahun'].astype(str)

# Mengubah kolom 'Bulan' menjadi format dua digit
datafull['Bulan'] = datafull['Bulan'].astype(str).str.zfill(2)

datafull['IHK'] = datafull['IHK'].round(2)
datafull['Inflasi MtM'] = datafull['Inflasi MtM'].round(2)
datafull['Inflasi YtD'] = datafull['Inflasi YtD'].round(2)
datafull['Inflasi YoY'] = datafull['Inflasi YoY'].round(2)

data = datafull[datafull['Kelompok'] == 'Umum']

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

with st.container(border=True):
    st.success('Perkembangan Indeks Harga Konsumen (IHK) Kota Bandung')
    grafik1 = px.line(data, x='Bulan', y='IHK', color='Tahun', markers=True)
    
    # Menempatkan legenda di bawah grafik
    grafik1.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
        title_text=''
    ))
    
    st.plotly_chart(grafik1, use_container_width=True)

with st.container(border=True):
    st.info('Inflasi Month to Month (MtM) Kota Bandung')
    grafik2 = px.line(data, x='Bulan', y='Inflasi MtM', color='Tahun',
                        markers=True)
    
    # Menempatkan legenda di bawah grafik
    grafik2.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
        title_text=''
    ))
    st.plotly_chart(grafik2, use_container_width=True)
        
with st.container(border=True):
    st.warning('Inflasi Year to Date (YtD) Kota Bandung')
    
    grafik3 = px.line(data, x='Bulan', y='Inflasi YtD', color='Tahun',
                      markers=True)
    
    # Menempatkan legenda di bawah grafik
    grafik3.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
        title_text=''
    ))
    
    st.plotly_chart(grafik3, use_container_width=True)
        
with st.container(border=True):
    st.success('Inflasi Year on Year (YoY) Kota Bandung')
    
    grafik4 = px.line(data, x='Bulan', y='Inflasi YoY', color='Tahun',
                      markers=True)
    
    # Menempatkan legenda di bawah grafik
    grafik4.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
        title_text=''
    ))
    
    st.plotly_chart(grafik4, use_container_width=True)

st.divider()

datafull = datafull.sort_values(by=['Tahun', 'Bulan'], ascending=False)
tahun = datafull['Tahun'].unique()

with st.container(border=True):
    kol1, kol2 = st.columns(2)
    with kol1:
        tahun_terpilih = st.selectbox('Filter Tahun', tahun)

    with kol2:
        pilihan = ['IHK', 'Inflasi MtM', 'Inflasi YtD', 'Inflasi YoY']
        indikator = st.selectbox('Pilih Indikator', pilihan)
        
    if tahun_terpilih and indikator:
        data_terpilih = datafull[datafull['Tahun'] == tahun_terpilih]
        grafik5 = px.line(data_terpilih, x='Bulan', y=indikator, color='Kelompok', markers=True)
        
        st.success(f'Perkembangan {indikator} Tahun {tahun_terpilih} menurut Kelompok Komoditas')
        st.plotly_chart(grafik5, use_container_width=True)

with st.expander('Lihat Tabel Lengkap'):
    st.success('IHK dan Inflasi Kota Bandung')
    df = datafull.sort_values(by=['Tahun', 'Bulan'], ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')