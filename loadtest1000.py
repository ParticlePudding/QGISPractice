import math
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY,
    QgsSingleSymbolRenderer, QgsLineSymbol
)

# 1. 新しい線のレイヤーを作成
layer = QgsVectorLayer("LineString?crs=EPSG:4326", "LoadTest1000", "memory")
QgsProject.instance().addMapLayer(layer)

layer.startEditing()

# 2. 1000個の座標を計算してリストに追加する
points = []
center_x = 139.767 # 東京駅の経度
center_y = 35.681  # 東京駅の緯度

# 1000回ループして、少しずつ外側に広がる座標を作ります
for i in range(100000):
    angle = i * 0.1       # 角度を少しずつずらす
    radius = i * 0.0001   # 半径を少しずつ広げる
    
    # 三角関数でx, y座標を計算してリストに追加
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    points.append(QgsPointXY(x, y))

# 3. 1000点が入ったリストを渡して、1本の長い折れ線を引く
feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPolylineXY(points))
layer.addFeature(feat)

layer.commitChanges()

# 4. 見やすくするために、細めの青い線に設定します
symbol = QgsLineSymbol.createSimple({'color': 'blue', 'line_width': '0.5'})
layer.setRenderer(QgsSingleSymbolRenderer(symbol))
layer.triggerRepaint()

print("1000点の描画が完了しました！")