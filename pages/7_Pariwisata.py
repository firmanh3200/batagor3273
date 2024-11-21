import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Statistik Pariwisata Kota Bandung')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/pariwisata.xlsx')
data['Tahun'] = data['Tahun'].astype(str)

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

kol1a, kol1b = st.columns(2)
with kol1a:
    with st.container(border=True):
        st.success('Tingkat Penghunian Kamar (TPK) Hotel Kota Bandung')
        grafik1 = px.bar(data, x='Tahun', y='TPK', barmode='group',
                         text='TPK', color='Kategori')
        
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
        st.info('Tingkat Pemakaian Tempat Tidur (TPTT) Hotel Kota Bandung')
        grafik2 = px.bar(data, x='Tahun', y='TPTT', barmode='group',
                          text='TPTT', color='Kategori')
        
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

with st.expander('Rata-rata Lama Menginap Tamu'):        
    kol2a, kol2b, kol2c = st.columns(3)
    with kol2a:
        with st.container(border=True):
            st.success('Rata-rata Lama Menginap Tamu Asing (RLMTA) di Hotel Kota Bandung')
            grafik3 = px.bar(data, x='Tahun', y='RLMTA', barmode='group',
                            text='RLMTA', color='Kategori')
            
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
            st.info('Rata-rata Lama Menginap Tamu (RLMT) di Hotel Kota Bandung')
            grafik4 = px.bar(data, x='Tahun', y='RLMT', barmode='group',
                            text='RLMT', color='Kategori')
            
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

    with kol2c:
        with st.container(border=True):
            st.success('Rata-rata Lama Menginap Tamu Dalam Negeri (RLMTD) di Hotel Kota Bandung')
            grafik5 = px.bar(data, x='Tahun', y='RLMTD', barmode='group',
                            text='RLMTD', color='Kategori')
            
            # Menempatkan legenda di bawah grafik
            grafik5.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik5, use_container_width=True)

with st.expander('Jumlah Tamu'):
    kol3a, kol3b = st.columns(2)
    with kol3a:
        with st.container(border=True):
            st.success('Jumlah Tamu Asing - Hotel Kota Bandung')
            grafik6 = px.bar(data, x='Tahun', y='Tamu Asing', barmode='group',
                            text='Tamu Asing', color='Kategori')
            
            # Menempatkan legenda di bawah grafik
            grafik6.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik6, use_container_width=True)

    with kol3b:
        with st.container(border=True):
            st.info('Jumlah Tamu Dalam Negeri - Hotel Kota Bandung')
            grafik7 = px.bar(data, x='Tahun', y='Tamu Domestik', barmode='group',
                            text='Tamu Domestik', color='Kategori')
            
            # Menempatkan legenda di bawah grafik
            grafik7.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik7, use_container_width=True)
        
with st.expander('Lihat Tabel Lengkap'):
    st.warning('Statistik Pariwisata Kota Bandung')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')