import streamlit as st
import pandas as pd 
import altair as alt

st.set_page_config(layout='wide')

st.header('Analisis Iklim Harian Berdasarkan Data BMKG di wilayah Kota Bandung: Studi tentang Temperatur, Kelembapan, dan Curah Hujan')
st.text('Nanda Ali Putra - Dqlab TETRIS PROGRAM Batch 3 Capstone Project')
st.write('''Sebagai negara yang berada di iklim tropis, Indonesia hanya memiliki dua musim yaitu musim hujan dan kemarau. 
Setiap musim memiliki karakteristiknya masing-masing seperti yang telah diketahui masyarakat pada umumnya. 
Namun, dewasa ini banyak terjadi ketidaksesuaian antara musim yang sedang terjadi dengan semestinya.
Hal tersebut tentunya membuat masyarakat tidak bisa mengantisipasi apa yang perlu mereka persiapkan untuk dampak yang akan terjadi.
Oleh sebab itu, mari kita analisis persoalan tersebut berdasarkan salah satu wilayah di Indonesia yaiti wilayah Bandung''')
st.text('''ID WMO	    :  96783
Nama Stasiun	:  Stasiun Geofisika Bandung
Lintang	    :  -6.88356
Bujur	    :  107.59733
Elevasi	    :  791
''')
df = pd.read_excel('C:\\Users\\LENOVO\\Documents\\laporan_harian_iklim.xlsx')

df

st.subheader('Hipotesis')
st.write('''1. Terdapat hubungan antara rata-rata suhu maksimum dan suhu minimum dalam suatu bulan, dimana jika suhu maksimum cenderung tinggi, maka suhu minimum juga cenderung tinggi
2. Kelembapan rata-rata perbulan akan stabil sepanjang tahun, dibandingkan dengan sebelumnya.
3. Curah hujan rata-rata perbulan akan mengalami variasi musiman yang signifikan.
''' )

st.subheader('Data Nilai Rata-rata Temperatur Bulanan 2017-2022')

melted_df = df.melt(id_vars=['Tanggal'], value_vars=['t_min', 't_max', 't_avg'], var_name='Parameter', value_name='Nilai')

chart_1 = alt.Chart(melted_df).mark_line().encode(
    x='Tanggal',
    y='Nilai',
    color='Parameter'
)

st.altair_chart(chart_1, use_container_width=True)

kolom1 = df['t_min']
kolom2 = df['t_max']

korelasi = kolom1.corr(kolom2)

print("Korelasi", korelasi)

st.subheader('Korelasi antara Rata-rata Suhu minimum dan Suhu Maksimum Bulanan')
st.write('''Nilai koefisien korelasi yang didapat antara rata-rata suhu minimum dan suhu maksimum bulanan adalah -0,413.
Ini menunjukan ternyata jika suhu maksimum tinggi maka suhu minimum tidak selalu tinggi juga.
''')
data = pd.DataFrame({'t_min': kolom1, 't_max': kolom2})

chart_4 = alt.Chart(data).mark_circle().encode(
    x='t_min',
    y='t_max'
)

st.altair_chart(chart_4, use_container_width=True)

chart_2 = alt.Chart(df).mark_line().encode(
    x='Tanggal',
    y='persen_kelembapan_rata2'
)

st.subheader('Data Nilai Persen Rata-rata Kelembapan Bulanan 2017-2022')
st.write('''Dari awal 2017 sampai pertengahan 2020 tepatnya pada bulan september, sekitar akhir musim kemarau pada tahun tersebut, memperlihatkan persen kelembapan rata-rata yang cenderun fluktuatif. Sedangkan pada oktober 2020 setelah memasuki musim hujan, sampai akhir 2022, nilai tersebut cenderung stabil diangka kurang lebih 80%.''')
st.altair_chart(chart_2, use_container_width=True)

chart_3 = alt.Chart(df).mark_line().encode(
    x='Tanggal',
    y="curah_hujan_rata2_mm"
)

st.subheader('Data Nilai Rata-rata Curah hujan Bulanan 2017-2022')
st.write('''Nilai rata-rata curah hujan bulanan yang ditunjukan mengalami variasi yang cukup banyak setiap musimnya.
Bahkan pada juni tahun 2020 pada musim kemarau, terdapat nilai curah hujan tertinggi yang belum pernah tercapai sebelumnya yaitu mencapai 3138,53 mm. 
Menurut kompas.com "Meskipun pada Juni ini wilayah Indonesia memasuki musim kemarau, curah hujan yang terjadi ternyata di atas rata-rata iklim tahun 1981-2010. Diungkapkan oleh Deputi Bidang Klimatologi Badan Meteorologi, Klimatologi, dan Geofisika (BMKG), Drs Herizal, Msi, hasil analisis hingga 20 Juni 2020 menunjukkan bahwa curah hujan yang terjadi di 50 persen wilayah Indonesia menunjukkan kondisi Atas Normal atau lebih basah dari biasanya. Sementara itu, wilayah yang mengalami kondisi Bawah Normal atau lebih kering dari rata-rata iklim mencapai 30 persen. Untuk diketahui, umumnya curah hujan di sebagian besar wilayah Indonesia pada pertengahan Juni 2020 berada pada kriteria rendah, yaitu berkisar 0-50 mm per dasarian.

Artikel ini telah tayang di Kompas.com dengan judul "Curah Hujan Juni 2020 di Atas Rata-rata Iklim, Bagaimana Bulan Juli?", Klik untuk baca: https://www.kompas.com/sains/read/2020/06/27/130400223/curah-hujan-juni-2020-di-atas-rata-rata-iklim-bagaimana-bulan-juli?page=all.
Penulis : Ellyvon Pranita
Editor : Shierine Wangsa Wibawa

Kompascom+ baca berita tanpa iklan: https://kmp.im/plus6
Download aplikasi: https://kmp.im/app6"''')

st.altair_chart(chart_3, use_container_width=True)

st.subheader('Data Nilai Rata-rata Lamanya penyinaran matahari bulanan 2017-2022')
st.write('''Sama halnya dengan sebelumnya, nilai rata-rata lamanya penyinaran matahari bulanan menunjukan variasi musiman. 
Sesuai dengan musim yang terjadi dimana pada musim kemarau memiliki nilai yang lebih tinggi dibandingkan dengan musim kemarau''')
chart_5 = alt.Chart(df).mark_line().encode(
    x='Tanggal',
    y='lama_sinar_matahari_jam'
)

st.altair_chart(chart_5, use_container_width=True)

st.subheader('Kesimpulan')
st.write('''Terdapat hubungan antara rata-rata suhu minimum dan suhu maksimum bulanan tahun 2017-2022 di Kota Bandung dimana setelah dianalisis memiliki nilai koefisien korelasi -0,431 yang berarti tidak selalu jika rata-rata suhu maksimum bulanan tinggi, maka rata-rata suhu minimum itu tinggi pula.
Selanjutnya Rata-rata Persen Kelembapan yang semula cenderung fluktuatif dari awal 2017 sampai pertengahan 2020 pada musim kemarau cenderung menjadi stabil diangka kurang lebih 80%.
Dan begitu pula dengan rata-rata curah hujan yang memang cenderung bervariasi musiman. Bahkan pada Juni 2020, rata-rata curah hujan menembus angka 3138,53 mm melebihi rata-rata curah hujan pada musim kemarau yaitu 0-50 mm per dasarian.

Dengan adanya analisis ini, kita bisa mengetahui bahwa cuaca yang kita alami sampai saat ini mulai tidak stabil yang disebabkan oleh pemanasan global.
dan dengan pengetahuan tersebut, diharapkan masyarakat bisa lebih memepersiapkan lagi bagaimana untuk menanggapi dampak dari cuaca dimasa yang akan datang.''')