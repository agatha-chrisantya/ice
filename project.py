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
    col3, col4 = st.columns([1,3])
    with col3:
        # image_path = "ice.png"
        
        # html_code = f"""
        # <div style="display: flex; justify-content: center;">
        #     <div style="border-radius: 50%; overflow: hidden; width: 200px; height: 200px;">
        #         <img src="{image_path}" style="width: 100%; height: 100%; object-fit: contain;">
        #     </div>
        # </div>
        # """
        # st.markdown(html_code, unsafe_allow_html=True)
        st.image("ice.png")
    with col4:
        st.title("ICE BSD")
        st.markdown(
            """
            <div style="text-align: justify; font-size: 17px;">
                Indonesia Convention Exhibition atau yang sering dikenal dengan ICE BSD, merupakan pusat konvensi dan pameran terbesar di Indonesia. Terletak di Bumi Serpong Damai, ICE yang dikelola oleh PT Indonesia Internasional Expo sudah menyelenggarakan berbagai acara mulai dari acara internal seperti rapat (<em>meeting</em>) sampai dengan konser sejak berdiri pada tahun 2015.
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.header("Events")
    col1, col2 = st.columns(2)

    df = pd.read_excel("data ice.xlsx", "Event")
    df2 = pd.read_excel("data ice.xlsx", "Engagement Rate")
    df3 = pd.read_excel("data ice.xlsx", "Total Event")
    df4 = pd.read_excel("data ice.xlsx", "Jumlah Pengunjung")
    # st.dataframe(df)

    with col1:
        fig3 = px.line(df3, x="Year", y="Total Event")
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        total = df.loc[:,"Exhibition":"Others"].sum()
        fig = px.bar(total, x=total.index, y=total.values, color=total.index)
        fig.update_layout(bargap=0, xaxis_title=None, yaxis_title="Total")
        fig.update_traces(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(
            """
            <div style="text-align: right; font-size: 12px; color: #808080;">
                Data Januari 2023 s.d. Maret 2023.
            </div>
            """,
            unsafe_allow_html=True
        )

    col5, col6 = st.columns(2)
    with col5:
        st.header("Visitors")
        df["Year"] = df["Bulan"].dt.to_period("Y")
        x = df[df["Year"] == "2023"]["Estimasi Jumlah Pengunjung"].sum()
        curr_year = 2023
        data2 = {"Tahun": curr_year, "Visitor":x}
        df_new = pd.DataFrame(data2, index=[0])
        new = pd.concat([df4,df_new], ignore_index=True)
        fig2 = px.line(df4, x="Tahun", y="Visitor")
        st.plotly_chart(fig2, use_container_width=True)
    with col6:
        st.header("Engagement Rate")
        fig7 = px.line(df2, x="Month", y="Engagement Rate")
        st.plotly_chart(fig7, use_container_width=True)
    # with col2:
    #     st.header("Exposure on Instagram")
    #     opsi = st.selectbox("", ("Likes", "Comment", "Followers", "Engagement Rate"))
    #     if opsi == "Likes":
    #         likes = pd.pivot_table(
    #             data=df2,
    #             index="Month",
    #             values="Likes"
    #         ).reset_index()
    #         fig2 = px.line(likes, x="Month", y="Likes")
    #         st.plotly_chart(fig2, use_container_width=True)
    #     elif opsi == "Comment":
    #         comment = pd.pivot_table(
    #             data=df2,
    #             index="Month",
    #             values="Comments"
    #         ).reset_index()
    #         fig2 = px.line(comment, x="Month", y="Comments")
    #         st.plotly_chart(fig2, use_container_width=True)
    #     elif opsi == "Followers":
    #         follower = pd.pivot_table(
    #             data=df2,
    #             index="Month",
    #             values="Followers"
    #         ).reset_index()
    #         fig2 = px.line(follower, x="Month", y="Followers")
    #         st.plotly_chart(fig2, use_container_width=True)
    #     else:
    #         rate = pd.pivot_table(
    #             data=df2,
    #             index="Month",
    #             values="Engagement Rate"
    #         ).reset_index()
    #         fig2 = px.line(rate, x="Month", y="Engagement Rate")
    #         fig2.update_layout(yaxis_title="Followers (%)")
    #         st.plotly_chart(fig2, use_container_width=True)

else:
    df3 = pd.read_excel("data ice.xlsx", "ig_ICE")
    df4 = pd.read_excel("data ice.xlsx", "ig_JIEXPO")
    df5 = pd.read_excel("data ice.xlsx", "ig_JCC")
    data = {
        'Jumlah Pengikut' : [78600,18300,83500],
        'Jumlah Post' : [3617, 3805, 1636],
        'Perusahaan' : ['ICE', 'JCC', 'JIEXPO']
    }
    df6 = pd.DataFrame(data)

    grafik = st.selectbox("", ["Engagement Instagram", "Comments"])
    if grafik == "Engagement Instagram":
        col5, col6 = st.columns(2)
        with col5:
            st.subheader("Followers")
            fig4 = px.bar(df6, x="Perusahaan", y="Jumlah Pengikut", color="Perusahaan")
            st.plotly_chart(fig4, use_container_width=True)
        with col6:
            st.subheader("Posts")
            fig5 = px.bar(df6, x="Perusahaan", y="Jumlah Post", color="Perusahaan")
            st.plotly_chart(fig5, use_container_width=True)
        
        st.subheader("Grafik Perbandingan Jumlah Like") 
        freq = st.radio("Frequency", ["Daily", "Monthly"])
        
        df3["Tanggal Upload"] = pd.to_datetime(df3["Tanggal Upload"], format="%d/%m/%Y")
        df4["Tanggal Upload"] = pd.to_datetime(df4["Tanggal Upload"], format="%d/%m/%Y")
        df5["Tanggal Upload"] = pd.to_datetime(df5["Tanggal Upload"], format="%d/%m/%Y")
        if freq == "Daily":
            df3_1 = df3.groupby("Tanggal Upload", as_index=False).agg({"Jumlah Like":"sum"})
            df4_1 = df4.groupby("Tanggal Upload", as_index=False).agg({"Jumlah Like":"sum"})
            df5_1 = df5.groupby("Tanggal Upload", as_index=False).agg({"Jumlah Like":"sum"})
            merged = pd.concat([df3_1, df4_1, df5_1], keys=["ICE", "JIEXPO", "JCC"])
            fig6 = px.line(merged, x="Tanggal Upload", y="Jumlah Like", color=merged.index.get_level_values(0))
        else:
            df3["Month"] = df3["Tanggal Upload"].dt.to_period("M").astype(str)
            df4["Month"] = df4["Tanggal Upload"].dt.to_period("M").astype(str)
            df5["Month"] = df5["Tanggal Upload"].dt.to_period("M").astype(str)
            df3_2 = df3.groupby("Month", as_index=False).agg({"Jumlah Like":"sum"})
            df4_2 = df4.groupby("Month", as_index=False).agg({"Jumlah Like":"sum"})
            df5_2 = df5.groupby("Month", as_index=False).agg({"Jumlah Like":"sum"})
            merged = pd.concat([df3_2, df4_2, df5_2], keys=["ICE", "JIEXPO", "JCC"])
            fig6 = px.line(merged, x="Month", y="Jumlah Like", color=merged.index.get_level_values(0))
        fig6.update_layout(legend_title_text="Perusahaan")
        st.plotly_chart(fig6, use_container_width=True)
        
        st.subheader("Top Categories")
    
        col7, col8, col9 = st.columns(3)
        with col7:
            top_ice = df3.groupby("Isi Konten", as_index=False).agg({"Jumlah Like":"sum"})
            top_sort = top_ice.sort_values(by="Jumlah Like", ascending=False)
            top_cat = top_sort["Isi Konten"].head(5)
            top_sort.loc[~top_sort["Isi Konten"].isin(top_cat), "Isi Konten"]="Others"
            # top1 = px.bar(top_ice, x="Isi Konten", y="Jumlah Like", color="Isi Konten")
            top1 = px.pie(top_sort, names="Isi Konten", values="Jumlah Like", color="Isi Konten")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            top1.update_layout(layout, title="ICE")
            st.plotly_chart(top1, use_container_width=True)
        with col8:
            top_jiexpo = df4.groupby("Isi Konten", as_index=False).agg({"Jumlah Like":"sum"})
            top_sort = top_jiexpo.sort_values(by="Jumlah Like", ascending=False)
            top_cat = top_sort["Isi Konten"].head(5)
            top_sort.loc[~top_sort["Isi Konten"].isin(top_cat), "Isi Konten"]="Others"
            # top2 = px.bar(top_jiexpo, x="Isi Konten", y="Jumlah Like", color="Isi Konten")
            top2 = px.pie(top_sort, names="Isi Konten", values="Jumlah Like", color="Isi Konten")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            top2.update_layout(layout, title="JIEXPO")
            st.plotly_chart(top2, use_container_width=True)
        with col9:
            top_jcc = df5.groupby("Isi Konten", as_index=False).agg({"Jumlah Like":"sum"})
            top_sort = top_jcc.sort_values(by="Jumlah Like", ascending=False)
            top_cat = top_sort["Isi Konten"].head(5)
            top_sort.loc[~top_sort["Isi Konten"].isin(top_cat), "Isi Konten"]="Others"
            # top3 = px.bar(top_jcc, x="Isi Konten", y="Jumlah Like", color="Isi Konten")
            top3 = px.pie(top_sort, names="Isi Konten", values="Jumlah Like", color="Isi Konten")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            top3.update_layout(layout, title="JCC")
            st.plotly_chart(top3, use_container_width=True)
    else:
        st.subheader("Grafik Perbandingan Jumlah Comment")
        freq = st.radio("Frequency", ["Daily", "Monthly"])
        
        df3["Tanggal Upload"] = pd.to_datetime(df3["Tanggal Upload"], format="%d/%m/%Y")
        df4["Tanggal Upload"] = pd.to_datetime(df4["Tanggal Upload"], format="%d/%m/%Y")
        df5["Tanggal Upload"] = pd.to_datetime(df5["Tanggal Upload"], format="%d/%m/%Y")
        if freq == "Daily":
            df3_1 = df3.groupby("Tanggal Upload", as_index=False).agg({"Jumlah Komentar":"sum"})
            df4_1 = df4.groupby("Tanggal Upload", as_index=False).agg({"Jumlah Komentar":"sum"})
            df5_1 = df5.groupby("Tanggal Upload", as_index=False).agg({"Jumlah Komentar":"sum"})
            merged = pd.concat([df3_1, df4_1, df5_1], keys=["ICE", "JIEXPO", "JCC"])
            fig6 = px.line(merged, x="Tanggal Upload", y="Jumlah Komentar", color=merged.index.get_level_values(0))
        else:
            df3["Month"] = df3["Tanggal Upload"].dt.to_period("M").astype(str)
            df4["Month"] = df4["Tanggal Upload"].dt.to_period("M").astype(str)
            df5["Month"] = df5["Tanggal Upload"].dt.to_period("M").astype(str)
            df3_2 = df3.groupby("Month", as_index=False).agg({"Jumlah Komentar":"sum"})
            df4_2 = df4.groupby("Month", as_index=False).agg({"Jumlah Komentar":"sum"})
            df5_2 = df5.groupby("Month", as_index=False).agg({"Jumlah Komentar":"sum"})
            merged = pd.concat([df3_2, df4_2, df5_2], keys=["ICE", "JIEXPO", "JCC"])
            fig6 = px.line(merged, x="Month", y="Jumlah Komentar", color=merged.index.get_level_values(0))
        fig6.update_layout(legend_title_text="Perusahaan")
        st.plotly_chart(fig6, use_container_width=True)

        st.subheader("Top Categories")
        col7, col8, col9 = st.columns(3)

        with col7:
            top_ice = df3.groupby("Isi Konten", as_index=False).agg({"Jumlah Komentar":"sum"})
            top_sort = top_ice.sort_values(by="Jumlah Komentar", ascending=False)
            top_cat = top_sort["Isi Konten"].head(5)
            top_sort.loc[~top_sort["Isi Konten"].isin(top_cat), "Isi Konten"]="Others"
            # top1 = px.bar(top_ice, x="Isi Konten", y="Jumlah Like", color="Isi Konten")
            top1 = px.pie(top_sort, names="Isi Konten", values="Jumlah Komentar", color="Isi Konten")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            top1.update_layout(layout, title="ICE")
            st.plotly_chart(top1, use_container_width=True)
        with col8:
            top_jiexpo = df4.groupby("Isi Konten", as_index=False).agg({"Jumlah Komentar":"sum"})
            top_sort = top_jiexpo.sort_values(by="Jumlah Komentar", ascending=False)
            top_cat = top_sort["Isi Konten"].head(5)
            top_sort.loc[~top_sort["Isi Konten"].isin(top_cat), "Isi Konten"]="Others"
            # top2 = px.bar(top_jiexpo, x="Isi Konten", y="Jumlah Like", color="Isi Konten")
            top2 = px.pie(top_sort, names="Isi Konten", values="Jumlah Komentar", color="Isi Konten")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            top2.update_layout(layout, title="JIEXPO")
            st.plotly_chart(top2, use_container_width=True)
        with col9:
            top_jcc = df5.groupby("Isi Konten", as_index=False).agg({"Jumlah Komentar":"sum"})
            top_sort = top_jcc.sort_values(by="Jumlah Komentar", ascending=False)
            top_cat = top_sort["Isi Konten"].head(5)
            top_sort.loc[~top_sort["Isi Konten"].isin(top_cat), "Isi Konten"]="Others"
            # top3 = px.bar(top_jcc, x="Isi Konten", y="Jumlah Like", color="Isi Konten")
            top3 = px.pie(top_sort, names="Isi Konten", values="Jumlah Komentar", color="Isi Konten")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            top3.update_layout(layout, title="JCC")
            st.plotly_chart(top3, use_container_width=True)




