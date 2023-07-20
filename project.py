import pandas as pd
import streamlit as st
import numpy as np
import plotly
import plotly_express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

st.set_page_config(
    page_title="ICE",
    layout="wide"
)

opt = option_menu(
    menu_title = None,
    options = ["ICE", "Analytics"],
    orientation = "horizontal"
)

if opt == "ICE":
    st.title("ICE BSD")
    st.write("Indonesia Convention Exhibition atau yang sering dikenal dengan ICE BSD, merupakan pusat konvensi dan pameran terbesar di Indonesia. Terletak di Bumi Serpong Damai, ICE yang dikelola oleh PT Indonesia Internasional Expo sudah menyelenggarakan berbagai acara mulai dari acara internal seperti rapat (meetings) sampai dengan konser sejak berdiri pada tahun 2015.")
    col1, col2 = st.columns(2)

    df = pd.read_excel("data ice.xlsx", "Event")
    df2 = pd.read_excel("data ice.xlsx", "Engagement Rate")
    # st.dataframe(df)
    with col1:
        st.header("Total Acara")
        total = df.loc[:,"Exhibition":"Others"].sum()
        fig = px.bar(total, x=total.index, y=total.values, color=total.index)
        fig.update_layout(bargap=0, xaxis_title=None, yaxis_title="Total")
        fig.update_traces(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.header("Exposure on Instagram")
        opsi = st.selectbox("", ("Likes", "Comment", "Followers", "Engagement Rate"))
        if opsi == "Likes":
            likes = pd.pivot_table(
                data=df2,
                index="Month",
                values="Likes"
            ).reset_index()
            fig2 = px.line(likes, x="Month", y="Likes")
            st.plotly_chart(fig2, use_container_width=True)
        elif opsi == "Comment":
            comment = pd.pivot_table(
                data=df2,
                index="Month",
                values="Comments"
            ).reset_index()
            fig2 = px.line(comment, x="Month", y="Comments")
            st.plotly_chart(fig2, use_container_width=True)
        elif opsi == "Followers":
            follower = pd.pivot_table(
                data=df2,
                index="Month",
                values="Followers"
            ).reset_index()
            fig2 = px.line(follower, x="Month", y="Followers")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            rate = pd.pivot_table(
                data=df2,
                index="Month",
                values="Engagement Rate"
            ).reset_index()
            fig2 = px.line(rate, x="Month", y="Engagement Rate")
            fig2.update_layout(yaxis_title="Followers (%)")
            st.plotly_chart(fig2, use_container_width=True)

else : 
    #Untuk input data
    dfins1 = pd.read_excel("data ice.xlsx", "ig_ICE")
    dfins2 = pd.read_excel("data ice.xlsx", "ig_JIEXPO")
    dfins3 = pd.read_excel("data ice.xlsx", "ig_JCC")

    data4 = {
        'Jumlah Pengikut' :  [78600,18300,83500],
        'Jumlah Post' : [3617, 3805, 1636],
       'Perusahaan' : ['ICE', 'JCC', 'JIEXPO']
    }
    df4 = pd.DataFrame(data4)

    #membuat dataframe
    dfins1 = pd.DataFrame(dfins1)
    dfins2 = pd.DataFrame(dfins2)
    dfins3 = pd.DataFrame(dfins3)

    #aggregasi data
    df_merged = pd.concat([dfins1, dfins2, dfins3], ignore_index=True)    
    
    #mengubah tipe data tanggal dari object (string) ke dalam tanggal
    df_merged['Tanggal Upload'] = pd.to_datetime(df_merged['Tanggal Upload'])

    df_merged['tahun'] = df_merged['Tanggal Upload'].dt.year
    CURR_YEAR = df_merged['tahun'].max()
    PREV_YEAR = CURR_YEAR - 1

    #Pemilihan Grafik
    grafik_perbandingan = st.selectbox(
        "Silahkan Pilih Grafik Perbandingan Instagram",
        ['Engagement Instagram','Komen']
    )
    if grafik_perbandingan == 'Engagement Instagram':

        #Membuat grafik histogram
        chart3 = alt.Chart(df4).mark_bar().encode(
            alt.X('Perusahaan', title=None, axis=alt.Axis(labelAngle=0, labels=False)),
            alt.Y('Jumlah Pengikut', title='Jumlah Pengikut'),
            color='Perusahaan'
        )
        chart4 = alt.Chart(df4).mark_bar().encode(
            alt.X('Perusahaan', title=None, axis=alt.Axis(labelAngle=0, labels=False)),
            alt.Y('Jumlah Post', title='Jumlah Post'),
            color='Perusahaan'
        )

        #Menampilkan grafik
        st.subheader('Grafik Jumlah Pengikut berdasarkan Perusahaan')
        st.altair_chart(chart3, use_container_width=True)

        st.subheader('Grafik Jumlah Post berdasarkan Perusahaan')
        st.altair_chart(chart4, use_container_width=True)
       

        #Korelasi engandmen instagram dengan reaction dari post instagram

        st.write("Kemudian bagaimana pengaruh like terhadap engadmen instagram?")
        st.write("Korelasi keduanya dapat dilihat pada grafik di bawah : ")
        
        freq = st.selectbox(
            "Silahkan Pilih Tipe Grafik", ["Harian", "Bulanan"])

        timeUnit = {
            'Harian':'yearmonthdate',
            'Bulanan':'yearmonth'
        }
        if freq == 'Harian' : 
            chart1 = alt.Chart(df_merged[df_merged['tahun'] == CURR_YEAR]).mark_line().encode(
                alt.X('Tanggal Upload', title='Waktu', timeUnit=timeUnit[freq], axis=alt.Axis(tickCount='day')),
                alt.Y('Jumlah Like', title='Jumlah Like', aggregate='sum'),
                color='Perusahaan'
            ).properties(   
                width=600,
                height=400
            )

            #Menampilkan grafik
            st.subheader('Grafik Perbandingan Jumlah Like Dari ICE, JCC dan JIEXPO')
            st.altair_chart(chart1, use_container_width=True)

        else :
            chart1 = alt.Chart(df_merged[df_merged['tahun'] == CURR_YEAR]).mark_line().encode(
                alt.X('Tanggal Upload', title='Waktu', timeUnit=timeUnit[freq], axis=alt.Axis(tickCount='month')),
                alt.Y('Jumlah Like', title='Jumlah Like', aggregate='sum'),
                color='Perusahaan'
            ).properties(   
                width=600,
                height=400
            )

            #Menampilkan grafik
            st.subheader('Grafik Perbandingan Jumlah Like Dari ICE, JCC dan JIEXPO')
            st.altair_chart(chart1, use_container_width=True)

        #Menampikan top 5 kategori untuk tiap perushaan
        st.write('Berdasarkan grafik diatas berikut adalah top 5 kategori untuk tiap perusahaan')

        def get_top_categories(df_merged, perusahaan, top_n=5):
            perusahaan_df = df_merged[df_merged['Perusahaan'] == perusahaan]
            top_categories = perusahaan_df.groupby('Isi Konten')['Jumlah Like'].sum().nlargest(top_n)
            return top_categories

        # Membuat dictionary untuk menyimpan hasil dari setiap perusahaan
        top_categories_perusahaan_dict = {}

        list_perusahaan = df_merged['Perusahaan'].unique().tolist()

        for perusahaan in list_perusahaan:
            top_categories_perusahaan_dict[perusahaan] = get_top_categories(df_merged, perusahaan)

        # Menampilkan hasil dalam bentuk data frame
        top_categories_df = pd.DataFrame(top_categories_perusahaan_dict)
        top_categories_df = top_categories_df.rename_axis('Top Kategori').reset_index()
        st.dataframe(top_categories_df) 

    else :
        #Page Komen
        freq = st.selectbox(
            "Silahkan Pilih Tipe Grafik", ["Harian", "Bulanan"])

        timeUnit = {
            'Harian':'yearmonthdate',
            'Bulanan':'yearmonth'
        }

        if freq == 'Harian' : 
            chart2 = alt.Chart(df_merged[df_merged['tahun'] == CURR_YEAR]).mark_line().encode(
                alt.X('Tanggal Upload', title='Waktu', timeUnit=timeUnit[freq], axis=alt.Axis(tickCount='day')),
                alt.Y('Jumlah Komentar', title='Jumlah Komen', aggregate='sum'),
                color='Perusahaan'
            ).properties(   
                width=600,
                height=400
            )

            #Menampilkan grafik
            st.subheader('Grafik Perbandingan Jumlah Komen Dari ICE JCC dan JIEXPO')
            st.altair_chart(chart2, use_container_width=True)
        
        else : 
            chart2 = alt.Chart(df_merged[df_merged['tahun'] == CURR_YEAR]).mark_line().encode(
                alt.X('Tanggal Upload', title='Waktu', timeUnit=timeUnit[freq], axis=alt.Axis(tickCount='month')),
                alt.Y('Jumlah Komentar', title='Jumlah Komen', aggregate='sum'),
                color='Perusahaan'
            ).properties(   
                width=600,
                height=400
            )

            #Menampilkan grafik
            st.subheader('Grafik Perbandingan Jumlah Komen Dari ICE JCC dan JIEXPO')
            st.altair_chart(chart2, use_container_width=True)

        #Menampikan top 5 kategori untuk tiap perushaan
        st.write('Berdasarkan grafik diatas berikut adalah top 5 kategori untuk tiap perusahaan')

        def get_top_categories(df_merged, perusahaan, top_n=5):
            perusahaan_df = df_merged[df_merged['Perusahaan'] == perusahaan]
            top_categories = perusahaan_df.groupby('Isi Konten')['Jumlah Komentar'].sum().nlargest(top_n)
            return top_categories

        # Membuat dictionary untuk menyimpan hasil dari setiap perusahaan
        top_categories_perusahaan_dict = {}

        list_perusahaan = df_merged['Perusahaan'].unique().tolist()

        for perusahaan in list_perusahaan:
            top_categories_perusahaan_dict[perusahaan] = get_top_categories(df_merged, perusahaan)

        # Menampilkan hasil dalam bentuk data frame
        top_categories_df = pd.DataFrame(top_categories_perusahaan_dict)
        top_categories_df = top_categories_df.rename_axis('Top Kategori').reset_index()
        st.dataframe(top_categories_df) 
