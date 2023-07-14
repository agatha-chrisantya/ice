import pandas as pd
import streamlit as st
import numpy as np
import plotly
import plotly_express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    dfins1 = pd.read_csv("data ice.csv", sep=";")
    dfins2 = pd.read_csv("data ice_2.csv", sep=";")
    dfins3 = pd.read_csv("data ice_3.csv", sep=";")

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
    df_merged['Tanggal'] = pd.to_datetime(df_merged['Tanggal'])

    #Pemilihan Grafik
    grafik_perbandingan = st.selectbox(
        "Silahkan Pilih Grafik Perbandingan Instagram",
        ['Engagement Instagram','Like','Komen']
    )
    if grafik_perbandingan == 'Like':
        #Membuat grafik line
        chart1 = alt.Chart(df_merged).mark_line().encode(
            alt.X('Tanggal', title='Waktu',axis=alt.Axis(labelAngle=0)),
            alt.Y('Like', title='Jumlah Like', aggregate='sum'),
            color='Perusahaan'
        ).properties(   
            width=600,
            height=400
        )

        #Menampilkan grafik
        st.subheader('Grafik Perbandingan Jumlah Like Dari ICE JCC dan JIEXPO')
        st.altair_chart(chart1, use_container_width=True)

    elif grafik_perbandingan == 'Komen' :
        #Membuat grafik line
        chart2 = alt.Chart(df_merged).mark_line().encode(
            alt.X('Tanggal', title='Waktu',axis=alt.Axis(labelAngle=0)),
            alt.Y('Komentar', title='Jumlah Komen', aggregate='sum'),
            color='Perusahaan'
        ).properties(   
            width=600,
            height=400
        )

        #Menampilkan grafik
        st.subheader('Grafik Perbandingan Jumlah Komen Dari ICE JCC dan JIEXPO')
        st.altair_chart(chart2, use_container_width=True)

    else : 
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
