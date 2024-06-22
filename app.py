import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

latitude = -3.539241
longitude = 118.941828


def display_map():
    map = folium.Map(
        location=[latitude, longitude],
        zoom_start=13,
        scrollWheelZoom=False,
    )

    geo_data = "banggae.json"

    data = pd.read_csv("banggae.csv")

    st.write(data.head())

    choropleth = folium.Choropleth(
        geo_data=geo_data,
        data=data,
        columns=["DESA", "KEPADATAN"],
        key_on="feature.properties.DESA",
        fill_color="YlOrRd",
        fill_opacity=0.9,
        threshold_scale=[0, 3000, 6000, 9000, 12000],
        legend_name="Kepadatan",
    )

    choropleth.geojson.add_to(map)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["DESA", "KEPADATAN"], labels=False),
    )

    map.save("index.html")

    with open("index.html", "r") as file:
        html_content = file.read()

    top_right = """
    <div style="position: absolute; top: 10px; right: 10px; z-index: 9999; background-color: orange; padding: 5px 10px; border-radius: 5px; color: white; font-weight: bold;">
        <h3>Edwin (D0221371) - SIG Informatika A</h3>
    </div>
    """

    html_content = html_content.replace("<body>", f"<body>{top_right}")

    with open("index.html", "w") as file:
        file.write(html_content)

    st_folium(map, width=700, height=450)


st.title("Peta Kepadatan Penduduk - Banggae, Majene, Sulawesi Barat")
display_map()
