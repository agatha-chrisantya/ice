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
        # "Apa"
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
        
        st.markdown(
            """
            <div style="text-align: justify;margin-top:-30px">
                Pada hasil visulisasi Events, kenaikan jumlah acara mulai tahun 2015 hingga 2018. Mulai 2019, banyak acara menurun drastis hingga 2020. 
                Hal ini dikarenakan adanya pandemic Covid-19 yang mulai masuk ke Indonesia di sekitar Maret 2020, sehingga kegiatan yang ramai dibatasi 
                bahkan ditiadakan yang berimbas dengan sedikitnya acara yang dilakukan secara luring. Kenaikan banyak acara mulai terlihat lagi hingga tahun 2022. 
                Berdasarkan hasil visualisasi ini, diperoleh bahwa ICE mampu bertahan dalam kondisi pandemi. Pasca pandemipun, ICE mampu mengembalikan target banyak acara 
                yang dapat ditampung di lingkungan ICE. Untuk 2023, karena masih pada pertengahan tahun sehingga belum dapat disimpulkan.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        total = df.loc[:,"Exhibition":"Others"].sum()
        fig = px.bar(total, x=total.index, y=total.values, color=total.index)
        fig.update_layout(bargap=0, xaxis_title=None, yaxis_title="Total")
        fig.update_traces(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(
            """
            <div style="text-align: right; font-size: 12px; color: #808080;margin-top:-50px">
                Data Januari 2023 s.d. Maret 2023.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div style="text-align: justify;margin-top:-45px">
                Dari hasil visualisasi histogram, diperoleh bahwa banyak kegiatan yang berlangsung di ICE yaitu Non-Corporate Meeting dibandingan dengan empat kategori lain seperti Exhibition, Corporate Meeting, Conference, dan lainnya.
            </div>
            """,
            unsafe_allow_html=True
        )
        

    col5, col6 = st.columns(2)
    with col5:
        st.markdown('\n')
        st.header("Visitors")
        df["Year"] = df["Bulan"].dt.to_period("Y")
        x = df[df["Year"] == "2023"]["Estimasi Jumlah Pengunjung"].sum()
        curr_year = 2023
        data2 = {"Tahun": curr_year, "Visitor":x}
        df_new = pd.DataFrame(data2, index=[0])
        new = pd.concat([df4,df_new], ignore_index=True)
        fig2 = px.line(df4, x="Tahun", y="Visitor")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown(
            """
            <div style="text-align: justify;margin-top:-35px">
                Dari data yang ada, dapat dibuat visualisasi untuk melihat banyaknya pengunjung yang ada di ICE. 
                Dengan mengesampingkan kategori pengunjung yang datang, diperoleh kenaikan yang signifikan mulai dari tahun 2015 hingga 2018. 
                Penurunan yang drastic terjadi mulai tahun 2018 hingga 2022. Perlu dilakukan pengecekan kembali pada tahun ini, apakah pencatatan pengunjung 
                tercatat dengan baik, mengingat mulai tahun 2020 terjadi pandemic sehingga kebanyakan kegiatan dibatalkan dan diubah menjadi luring.
            </div>
            """,
            unsafe_allow_html=True
        )
        

    with col6:
        st.markdown('\n')
        st.header("Engagement Rate")
        fig7 = px.line(df2, x="Month", y="Engagement Rate")
        st.plotly_chart(fig7, use_container_width=True)
        st.markdown(
            """
            <div style="text-align: justify;margin-top:-35px">
                Kenaikan cukup signifikan terlihat pada grafik ICE mulai bulan April 2023, meskipun pada 
                bulan sebelumnya terjadi sedikit penurunan yang membuat engagement rate sama kembali seperti bulan Januari 2022 hingga Januari 2023.
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    df3 = pd.read_excel("data ice.xlsx", "ig_ICE")
    df4 = pd.read_excel("data ice.xlsx", "ig_JIEXPO")
    df5 = pd.read_excel("data ice.xlsx", "ig_JCC")
    df6 = pd.read_excel("data ice.xlsx", "ER_IG")
    df7 = pd.read_excel("data ice.xlsx", "ER_IG2")

    with st.sidebar:
        st.markdown(
            """
            <style>
            .custom-col10 h3 {
                font-size: 20px; /* Atur ukuran teks sesuai kebutuhan */
            }
            .custom-col10 p {
                font-size: 16px; /* Atur ukuran teks sesuai kebutuhan */
                text-align: justify;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="custom-col10">
                <h3>Balai Sidang Jakarta Convention Center (JCC)</h3>
                <p>berdiri sejak tahun 1992, memiliki 30 tahun pengalaman dalam menangani acara besar dunia. JCC memiliki luas 30.000 sqm yang memiliki 2 bangunan utama yang digunakan sebagai Meeting Room dan Exhibition Halls.</p>
                <br>
                <h3>PT Jakarta International Expo</h3>
                <p>adalah anak perusahaan dari Central Cipta Murdaya Group (CCM), yang dikenal dengan pengalaman dan reputasinya di berbagai industri di Indonesia, seperti manufaktur, perdagangan dan pameran. Reputasi yang sangat baik ini dibuktikan dengan kesuksesan berbagai acara dan proyek. Jakarta International Expo atau JIExpo memiliki luas lahan sekitar lebih 44 hektar.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    grafik = st.selectbox("", ["Engagement Instagram", "Comments"])

    if grafik == "Engagement Instagram":
        st.subheader("Perbandingan Jumlah Post")
        col7, col8 = st.columns(2)
        with col7:
            #Grafik engadmen by post
            EngadmenIG = df7.groupby("Perusahaan", as_index=False).agg({"Jumlah_Post":"sum"})
            ENG1 = px.pie(EngadmenIG, names="Perusahaan", values="Jumlah_Post", color="Perusahaan")
            layout = go.Layout(
                autosize=False,
                width=400,
                height=400,
            )
            # ENG1.update_layout(layout)  # Penyesuaian gap grafik dan legend
            ENG1.update_layout(layout,legend=dict(orientation="h",x=0.5, y=-0.1, xanchor='center', yanchor='top'))
            ENG1.update_layout(margin=dict(t=20, b=20, l=50, r=50))
            st.plotly_chart(ENG1, use_container_width=True)

        with col8:
            EngadmenIG = df7.groupby("Perusahaan", as_index=False).agg({"Jumlah_Post":"sum"})
            EngadmenIG_sorted = EngadmenIG.sort_values(by="Jumlah_Post", ascending=False)
            perusahaan_terbesar = EngadmenIG_sorted.iloc[0]["Perusahaan"]
            # css_center_text = '''
            #     <style>
            #         .center-text {
            #             display: flex;
            #             justify-content: center;
            #         }
            #     </style>
            # '''
            teks = f"Berdasarkan grafik disamping dapat dilihat bahwa dalam rentan waktu 26 Juni 2023 hingga 17 Juni 2023, {perusahaan_terbesar} memiliki jumlah post terbanyak. Kemudian bagaimana dengan pertumbuhan pengikut harian instagram {perusahaan_terbesar} dibandingkan dengan kompetitor? Untuk perbandingannya dapat dilihat pada grafik di bawah."
            style = "font-size: 18px; text-align: justify; margin-top: 80px; margin-bottom: 20px;"
            # st.markdown("<p style='font-size: 18px; text-align: justify;'>{}</p>".format(teks), unsafe_allow_html=True)
            st.markdown(f"<p style='{style}'>{teks}</p>", unsafe_allow_html=True)
        #Grafik pertumbuhan followers harian
        # Mengubah nama kolom
        df6 = df6.rename(columns={
            'ice_day_followers': 'ICE',
            'jiexpo_day_followers': 'JIEXPO',
            'jcc_day_followers': 'JCC'
        })

        # Membuat multiselect untuk memilih kolom yang ingin ditampilkan
        kolom_options = ['ICE', 'JIEXPO', 'JCC']
        multitahun = st.multiselect(
            "Pilih Perusahaan",
            kolom_options,
            default=['ICE']  # Nilai default saat aplikasi pertama kali dijalankan
        )
        
        # Filter dataframe berdasarkan kolom-kolom yang dipilih
        filtered_df = df6[['date'] + multitahun]
        
        # Melt dataframe menjadi format long untuk line chart dengan Altair
        melted_df = filtered_df.melt('date', var_name='Kolom', value_name='Followers')

        # Membuat line chart dengan Altair
        line_chart = alt.Chart(melted_df).mark_line().encode(
            alt.X('date:T', title='Tanggal'),
            alt.Y('Followers:Q', title='Jumlah Pengikut'),
            color='Kolom:N',
            tooltip=['Kolom:N', 'Followers:Q']
        ).properties(
            title=f"Penambahan Pengikut Instagram Harian {', '.join(map(str, multitahun))}"
        )

        # Menampilkan chart menggunakan Streamlit
        st.altair_chart(line_chart, use_container_width=True)
        st.markdown(
            """
            <div style="text-align: justify;margin-top:-25px">
                Dari hasil visualisasi jumlah pengikut harian terhadap ICE, JCC, dan JIEXPO. Diperoleh bahwa JIEXPO mempunyai 
                kenaikan yang tinggi pada hari tertentu. Perlu dilakukan peninjauan ulang dalam hari pada saat 
                jumlah pengikut harian tinggi bahwa terdapat suatu acara atau kegiatan yang mengakibatkan kenaikan jumlah pengikut tersebut.
            </div>
            """,
            unsafe_allow_html=True,
        )

        #Proses Grafik Like Instagram
        st.markdown('\n')
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
            fig6 = px.line(merged, x="Tanggal Upload", y="Jumlah Like",color=merged.index.get_level_values(0))

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

        st.markdown(
            """
            <div style="text-align: justify;margin-top:-25px">
                Dari hasil visualisasi perbandingan jumlah like dari ICE, JIEXPO, dan JCC, terlihat jelas bahwa ICE 
                memiliki lompatan data jumlah like tertinggi dibandingkan lainnya. Perlu dipertanyakan, pada JIEXPO 
                jumlah kenaikan pengikut naik signifikan akan tetapi jumlah like tidak mencerminkan kenaikan seperti 
                pada ICE. Asumsi yang dimiliki, jika kenaikan pengikut tinggi maka terdapat suatu post mengenai acara 
                atau kegiatan yang mencerminkan kenaikan pengikut tersebut dan mengakibatkan banyaknya jumlah like pada postingan tersebut.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('\n')
        st.subheader("Top Categories")
    
        col9, col10, col11 = st.columns(3)
        with col9:
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
            st.markdown(
            """
            <div style="text-align: justify;margin-top:-65px">
                Komponen postingan terbanyak berdasarkan like dari ICE yaitu Notifikasi Acara disusul oleh Pameran. 
                Sebagai pengingat akan acara yang akan diselenggarakan di ICE penting untuk di publish agar pengikut 
                setia ICE tahu akan ada acara baru di tanggal tertentu.
            </div>
            """,
            unsafe_allow_html=True,
        )
        with col10:
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
            st.markdown(
            """
            <div style="text-align: justify;margin-top:-65px">
                Komponen postingan terbanyak berdasarkan like dari JIEXPO yaitu Others seperti dokumentasi acara, 
                rapat suatu acara penting seperti kenegaraan, upacara pembukaan kegiatan, dll.
           </div>
            """,
            unsafe_allow_html=True,
        )
        with col11:
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
            st.markdown(
            """
            <div style="text-align: justify;margin-top:-65px">
                Komponen postingan terbanyak berdasarkan like dari JCC yaitu Repost. Merepresentasikan dokumentasi 
                atau hal yang di unggah oleh orang lain kemudian di repost oleh akun JCC.
            </div>
            """,
            unsafe_allow_html=True,
        )
        
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

        st.markdown(
            """
            <div style="text-align: justify;margin-top:-25px">
                Dari hasil visualisasi perbandingan jumlah komentar, ICE memiliki lonjakan komentar tertinggi 
                pada 29 Maret 2023 dibandingkan dengan kompetitor lainnya. Dari analisis sebelumnya, banyaknya 
                pengikut harusnya akan mempengaruhi banyak like. Berlaku juga dalam hal ini, banyaknya pengikut 
                akan berpengaruh terhadap banyak komentar yang ada dalam postingan tersebut.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('\n')
        st.subheader("Top Categories")
        col9, col10, col11 = st.columns(3)

        with col9:
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
            st.markdown(
            """
            <div style="text-align: justify;margin-top:-65px">
                Komponen postingan terbanyak berdasarkan komentar dari ICE yaitu Notifikasi Acara disusul oleh Pameran yang sama dengan analisis berdasarkan like.
            </div>
            """,
            unsafe_allow_html=True,
        )
        with col10:
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
            st.markdown(
            """
            <div style="text-align: justify;margin-top:-65px">
                Komponen postingan terbanyak berdasarkan like dari JIEXPO yaitu Notifikasi Acara sebagai pengingat akan adanya acara sesuai waktunya.
            </div>
            """,
            unsafe_allow_html=True,
        )
        with col11:
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
            st.markdown(
            """
            <div style="text-align: justify;margin-top:-65px">
                Komponen postingan terbanyak berdasarkan like dari JCC yaitu Repost sama dengan analisis berdasarkan jumlah like.
            </div>
            """,
            unsafe_allow_html=True,
        )
