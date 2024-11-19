import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Kemiskinan Makro Kota Bandung')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/kemiskinan.xlsx')
data['Tahun'] = data['Tahun'].astype(str)
data['Garis Kemiskinan (Rp/Kap/Bulan)'] = data['Garis Kemiskinan (Rp/Kap/Bulan)'].round(2)
data['Jumlah Penduduk Miskin (Ribu Jiwa)'] = data['Jumlah Penduduk Miskin (Ribu Jiwa)'].round(2)
data['Persentase Penduduk Miskin (P0)'] = data['Persentase Penduduk Miskin (P0)'].round(2)
data['Indeks Kedalaman Kemiskinan (P1)'] = data['Indeks Kedalaman Kemiskinan (P1)'].round(2)
data['Indeks Keparahan Kemiskinan (P2)'] = data['Indeks Keparahan Kemiskinan (P2)'].round(2)

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

kol1a, kol1b = st.columns(2)
with kol1a:
    with st.container(border=True):
        st.success('Perkembangan Jumlah Penduduk Miskin di Kota Bandung')
        grafik1 = px.bar(data, x='Tahun', y='Jumlah Penduduk Miskin (Ribu Jiwa)',
                         text='Jumlah Penduduk Miskin (Ribu Jiwa)')
        st.plotly_chart(grafik1, use_container_width=True)

with kol1b:
    with st.container(border=True):
        st.info('Garis Kemiskinan Kota Bandung')
        grafik2 = px.line(data, x='Tahun', y='Garis Kemiskinan (Rp/Kap/Bulan)',
                          markers=True)
        st.plotly_chart(grafik2, use_container_width=True)
        
with st.container(border=True):
    st.warning('Persentase Penduduk Miskin (P0), Indeks Kedalaman Kemiskinan (P1), \
            Indeks Keparahan Kemiskinan (P2)')
    
    grafik3 = px.line(data, x='Tahun', y=['Persentase Penduduk Miskin (P0)', 
                                          'Indeks Kedalaman Kemiskinan (P1)',
                                          'Indeks Keparahan Kemiskinan (P2)'],
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
        
with st.expander('Lihat Tabel Lengkap'):
    st.success('Indikator Kemiskinan Makro Kota Bandung')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)