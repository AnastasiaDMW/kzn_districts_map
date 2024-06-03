import pandas as pd
from ipyleaflet import Map, Marker, Polygon, FullScreenControl, LegendControl
from ipywidgets import Layout

class MapRenderer:
    
    def __init__(self, district_data: pd.DataFrame, points_data: pd.DataFrame):
        self.__points_data = points_data
        self.__district_data = district_data

    def get_map(self) -> Map:
        
        # Центр краты
        center_lat = self.__points_data['lat'].median()
        center_lon = self.__points_data['lon'].median()

        m = Map(center=(center_lat, center_lon), zoom=12, layout=Layout(width='100%', height='800px'))

        for _, row in self.__district_data.iterrows():
            district_name = row['district']
            color = row['color']
            center = eval(row['center'])
            points = [tuple(pt) for pt in eval(row['points'])]

            # Создание полигона
            polygon = Polygon(
                locations=points,
                color=color,
                fill_color=color,
                fill_opacity=0.6,
                name=district_name
            )
            m.add_layer(polygon)

            # Создание маркера
            marker = Marker(
                location=center,
                draggable=False,
                title=district_name
            )
            m.add_layer(marker)

        m.add_control(FullScreenControl())

        return m