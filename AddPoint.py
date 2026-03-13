from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY

# 1. 一時的なポイントレイヤーを作成
# "Point?crs=EPSG:4326" は、世界測地系（緯度経度）を使うという意味です
layer = QgsVectorLayer("Point?crs=EPSG:4326", "MyPoints", "memory")

# 2. レイヤーの編集を開始
layer.startEditing()

# 3. 指定したい座標を定義（例：東経139.76, 北緯35.68）
x, y = 139.767, 35.681

# 4. 「地物（Feature）」として点を作成
feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))

# 5. レイヤーに点を追加して、編集を保存
layer.addFeature(feat)
layer.commitChanges()

# 6. QGISのマップキャンバスにレイヤーを表示
QgsProject.instance().addMapLayer(layer)