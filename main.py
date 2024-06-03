import pandas as pd
from convex_hull_builder import ConvexHullBuilder
from map_renderer import MapRenderer

# Поменяйте путь на свой
PATH_TO_SAVE = "C:\\Users\\user\\Desktop\\dz_new\\kzn_districts_map_template\\result.csv"

points_df = pd.read_csv("C:\\Users\\user\\Desktop\\dz_new\\kzn_districts_map_template\\points.csv")

builder = ConvexHullBuilder(points_df)

result_df = builder.get_convex_hull()

result_df.to_csv(PATH_TO_SAVE, index=False)
districts_df = pd.read_csv(PATH_TO_SAVE)

renderer = MapRenderer(districts_df, points_df)
renderer.get_map()