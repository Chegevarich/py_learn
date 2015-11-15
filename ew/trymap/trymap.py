#!/usr/bin/python
# coding: utf8

from __future__ import unicode_literals
from mpl_toolkits.basemap import Basemap
from matplotlib.pyplot import *

# Создаем карту в ортографической проекции
m = Basemap(projection="ortho", lat_0=20, lon_0=70, resolution="l")
# Задаем фона голубого цвета
m.drawmapboundary(fill_color="aqua")
# Рисуем континенты
m.fillcontinents(color="coral", lake_color="aqua")
# Рисуем береговые линии
m.drawcoastlines(linewidth=0.25)
# Рисуем реки
m.drawrivers(linewidth=0.1)
# Рисуем сетку широт
m.drawmeridians(np.arange(0,360,30))
# Рисуем сетку долгот
m.drawparallels(np.arange(-90,90,30))
# Переводим значения долготы и широты в координаты на карте
x, y = m(30,60)
# Рисуем точку на карте
m.plot(x, y, "b*", markersize=10)
# Добавляем рядом подпись
text(x+5.5, y-5.5, "Санкт-Петербург", fontsize=14)
# Записываем рисунок в файл
savefig("base004.png", dpi=75)
# Отображаем карту
show()