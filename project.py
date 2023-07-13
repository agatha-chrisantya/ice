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
