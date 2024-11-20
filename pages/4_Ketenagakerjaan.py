import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Statistik Ketenagakerjaan Kota Bandung')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/tpt.xlsx')
data['Tahun'] = data['Tahun'].astype(str)

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

kol1a, kol1b = st.columns(2)
with kol1a:
    with st.container(border=True):
        st.success('Tren Tingkat Pengangguran Terbuka (TPT) Kota Bandung dan Jawa Barat')
        grafik1 = px.bar(data, x='Tahun', y='TPT (%)', barmode='group',
                         text='TPT (%)', color='Wilayah')
        
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

with kol1b:
    with st.container(border=True):
        st.info('Tren Tingkat Partisipasi Angka Kerja (TPAK) Kota Bandung dan Jawa Barat')
        grafik2 = px.line(data, x='Tahun', y='TPAK (%)',
                          markers=True, color='Wilayah')
        
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
        
        
with st.expander('Lihat Tabel Lengkap'):
    st.warning('Indikator Ketenagakerjaan Makro Kota Bandung dan Jawa Barat')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)