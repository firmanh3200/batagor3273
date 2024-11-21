import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Indikator Pembangunan Manusia Kota Bandung')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/ipm.xlsx')
data['Tahun'] = data['Tahun'].astype(str)

with st.expander('M E T A D A T A'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

with st.container(border=True):
    st.success('Tren IPM Kota Bandung')
    grafik1 = px.bar(data, x='Tahun', y='Indeks Pembangunan Manusia',
                        text='Indeks Pembangunan Manusia')
    st.plotly_chart(grafik1, use_container_width=True)    
    
kol1a, kol1b = st.columns(2)
with kol1a:
    with st.container(border=True):
        st.info('Tren Pengeluaran Perkapita Disesuaikan (000 Rp) Kota Bandung')
        grafik1 = px.bar(data, x='Tahun', y='Pengeluaran Perkapita Disesuaikan (000 Rp)',
                         text='Pengeluaran Perkapita Disesuaikan (000 Rp)')
        st.plotly_chart(grafik1, use_container_width=True)

with kol1b:
    with st.container(border=True):
        st.warning('Pertumbuhan IPM Kota Bandung (%)')
        grafik2 = px.line(data, x='Tahun', y='Pertumbuhan IPM',
                          markers=True)
        st.plotly_chart(grafik2, use_container_width=True)


kol2a, kol2b = st.columns(2)
with kol2a:
    with st.container(border=True):
        st.warning('Tren Lama Sekolah di Kota Bandung')
        
        grafik3 = px.line(data, x='Tahun', y=['Harapan Lama Sekolah (Tahun)',
                                            'Rerata Lama Sekolah (Tahun)'],
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

with kol2b:
    with st.container(border=True):
        st.info('Tren Usia Harapan Hidup (UHH) di Kota Bandung')
        
        grafik4 = px.bar(data, x='Tahun', y='Usia Harapan Hidup (Tahun)',
                         text='Usia Harapan Hidup (Tahun)')
        
        st.plotly_chart(grafik4, use_container_width=True)
        
with st.expander('Lihat Tabel Lengkap'):
    st.success('Indikator Pembangunan Manusia Kota Bandung')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')