import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Produk Domestik Regional Bruto (PDRB) Kota Bandung')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/pdrb.xlsx')
data['Tahun'] = data['Tahun'].astype(str)
total = data[data['Lapangan Usaha'] == 'Total PDRB']

pdrblu = data[data['Lapangan Usaha'] != 'Total PDRB']
pdrblu = pdrblu.sort_values(by=['Tahun', 'Lapangan Usaha'], ascending=[False, True])

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

with st.container(border=True):
    st.success('Tren PDRB Kota Bandung (Milyar Rupiah)')
    grafik1 = px.bar(total, x='Tahun', y=['Berlaku', 'Konstan'], barmode='group')
    
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

tahun = pdrblu['Tahun'].unique()
tahun_terpilih = st.selectbox('Filter Tahun', tahun)

if tahun_terpilih:
    pdrblu_terpilih = pdrblu[pdrblu['Tahun'] == tahun_terpilih]
    
    kol1a, kol1b = st.columns(2)
    with kol1a:
        with st.container(border=True):
            st.warning(f'PDBR Berlaku menurut Lapangan Usaha Tahun {tahun_terpilih} (Miliar Rupiah)')
            grafik2 = px.treemap(pdrblu_terpilih, path=['Lapangan Usaha'], values='Berlaku')
            
            st.plotly_chart(grafik2, use_container_width=True)
            
    with kol1b:
        with st.container(border=True):
            st.info(f'PDRB Konstan menurut Lapangan Usaha Tahun {tahun_terpilih}')
            grafik3 = px.sunburst(pdrblu_terpilih, path=['Lapangan Usaha'], values='Konstan')
            
            st.plotly_chart(grafik3, use_container_width=True)
            
        
with st.expander('Lihat Tabel Lengkap'):
    st.warning('Indikator Ketenagakerjaan Makro Kota Bandung dan Jawa Barat')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)