import pandas as pd
import numpy as np
import random

class ConvexHullBuilder:
    
    def __init__(self, points: pd.DataFrame):
        print(points)
        self.__points = points

    # Поворот
    def rotate(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def jarvis(self, points):
        n = len(points)
        if n < 3:
            return points

        hull = []
        # мин знач столбика x
        l = np.argmin(points[:, 0])
        p = l

        while True:
            hull.append(tuple(points[p]))
            # получение след точки
            next_p = (p + 1) % n
            for i in range(n):
                # против часовой стрелки
                if self.rotate(points[p], points[i], points[next_p]) < 0:
                    next_p = i
            p = next_p
            if p == l:
                break

        return hull

    def get_convex_hull(self) -> pd.DataFrame:
        results = []
        
        for district, group in self.__points.groupby('district'):
            points = group[['lat', 'lon']].values
            hull_points = self.jarvis(points)
            center = points.mean(axis=0)
            color = "#%06x" % random.randint(0, 0xFFFFFF)

            results.append({
                'district': district,
                'points': hull_points,
                'center': tuple(center),
                'color': color
            })

        return pd.DataFrame(results)