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

pdrbx = pd.read_excel('data/pdrbx.xlsx')
pdrbx['Tahun'] = pdrbx['Tahun'].astype(str)


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

st.divider()

st.subheader('PDRB menurut Lapangan Usaha')
tab1a, tab1b = st.tabs(['Harga Berlaku', 'Harga Konstan 2010'])

with tab1a:
    with st.container(border=True):
        st.success('Tren PDRB Berlaku menurut Lapangan Usaha Kota Bandung (Milyar Rupiah)')
        grafik1a = px.bar(pdrblu, x='Tahun', y='Berlaku', color='Lapangan Usaha')
        
        st.plotly_chart(grafik1a, use_container_width=True)

with tab1b:
    with st.container(border=True):
        st.success('Tren PDRB Konstan menurut Lapangan Usaha Kota Bandung (Milyar Rupiah)')
        grafik1b = px.bar(pdrblu, x='Tahun', y='Konstan', color='Lapangan Usaha')
        
        st.plotly_chart(grafik1b, use_container_width=True)

st.divider()

st.subheader('PDRB menurut Pengeluaran')
tab2a, tab2b = st.tabs(['Harga Berlaku', 'Harga Konstan 2010'])

with tab2a:
    with st.container(border=True):
        st.success('Tren PDRB Berlaku menurut Pengeluaran Kota Bandung (Milyar Rupiah)')
        grafik2a = px.bar(pdrbx, x='Tahun', y='Berlaku', color='Kelompok')
        
        st.plotly_chart(grafik2a, use_container_width=True)

with tab2b:
    with st.container(border=True):
        st.success('Tren PDRB Konstan menurut Pengeluaran Kota Bandung (Milyar Rupiah)')
        grafik2b = px.bar(pdrbx, x='Tahun', y='Konstan', color='Kelompok')
        
        st.plotly_chart(grafik2b, use_container_width=True)


st.divider()

tahun = pdrblu['Tahun'].unique()
tahun_terpilih = st.selectbox('Filter Tahun', tahun)

if tahun_terpilih:
    pdrblu_terpilih = pdrblu[pdrblu['Tahun'] == tahun_terpilih]
    
    kol1a, kol1b = st.columns(2)
    with kol1a:
        with st.container(border=True):
            st.warning(f'PDRB Berlaku menurut Lapangan Usaha Tahun {tahun_terpilih} (Miliar Rupiah)')
            grafik2 = px.treemap(pdrblu_terpilih, path=['Lapangan Usaha'], values='Berlaku')
            
            st.plotly_chart(grafik2, use_container_width=True)
            
    with kol1b:
        with st.container(border=True):
            st.info(f'PDRB Konstan menurut Lapangan Usaha Tahun {tahun_terpilih} (Miliar Rupiah)')
            grafik3 = px.sunburst(pdrblu_terpilih, path=['Lapangan Usaha'], values='Konstan')
            
            st.plotly_chart(grafik3, use_container_width=True)
            
    pdrbx_terpilih = pdrbx[pdrbx['Tahun'] == tahun_terpilih]
    
    kol2a, kol2b = st.columns(2)
    with kol2a:
        with st.container(border=True):
            st.warning(f'PDRB Berlaku menurut Pengeluaran Tahun {tahun_terpilih} (Miliar Rupiah)')
            grafik4 = px.sunburst(pdrbx_terpilih, path=['Kelompok'], values='Berlaku')
            
            st.plotly_chart(grafik4, use_container_width=True)
    
    with kol2b:
        with st.container(border=True):
            st.warning(f'PDRB Konstan menurut Pengeluaran Tahun {tahun_terpilih} (Miliar Rupiah)')
            grafik5 = px.treemap(pdrbx_terpilih, path=['Kelompok'], values='Konstan')
            
            st.plotly_chart(grafik5, use_container_width=True)
            
        
with st.expander('Lihat Tabel Lengkap PDRB menurut Lapangan Usaha'):
    st.warning('Produk Domestik Regional Bruto menurut Lapangan Usaha Kota Bandung')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
with st.expander('Lihat Tabel Lengkap PDRB menurut Pengeluaran'):
    st.warning('Produk Domestik Regional Bruto menurut Pengeluaran Kota Bandung')
    df = pdrbx.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)