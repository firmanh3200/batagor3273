import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Produksi Padi dan Beras di Kota Bandung')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/ksa.xlsx')
data['Tahun'] = data['Tahun'].astype(str)

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

kol1a, kol1b = st.columns(2)
with kol1a:
    with st.container(border=True):
        st.success('Luas Panen Padi di Kota Bandung (Hektare)')
        grafik1 = px.bar(data, x='Bulan', y='Luas Panen Padi', barmode='group',
                         text='Luas Panen Padi', color='Tahun')
        
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
        st.info('Produksi Padi di Kota Bandung (Ton GKG)')
        grafik2 = px.bar(data, x='Bulan', y='Produksi Padi', barmode='group',
                          text='Produksi Padi', color='Tahun')
        
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

with st.expander('Produksi Beras'):        
    with st.container(border=True):
        st.success('Produksi Beras di Kota Bandung (Ton)')
        grafik3 = px.bar(data, x='Bulan', y='Produksi Beras', barmode='group',
                        text='Produksi Beras', color='Tahun')
        
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
    st.warning('Hasil Survei KSA di Kota Bandung')
    df = data.sort_values(by=['Tahun', 'Bulan'], ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.subheader('', divider='rainbow')
st.caption(':green[Batagor - Bandung Kota dalam Grafik dan Indikator]')
st.caption(':green[Hak Cipta @ BPS Kota Bandung]')