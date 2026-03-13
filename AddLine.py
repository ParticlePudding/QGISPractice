from qgis.core import (
    QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY,
    QgsField, QgsSingleSymbolRenderer, QgsLineSymbol
)
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor

# 1. 新しい線のレイヤーを作成 (Point ではなく LineString にします)
layer = QgsVectorLayer("LineString?crs=EPSG:4326", "TokyoShinjukuLine", "memory")
QgsProject.instance().addMapLayer(layer)

# 2. フィールド（カラム）の定義と追加
layer.startEditing()
layer.dataProvider().addAttributes([QgsField("name", QVariant.String)])
layer.updateFields()

# 3. 属性を持った地物（線）の追加
feat = QgsFeature()

points = []
points.append(QgsPointXY(139.767, 35.681)) # 東京駅付近
points.append(QgsPointXY(139.700, 35.690)) # 新宿駅付近
points.append(QgsPointXY(139.701, 35.658)) # 渋谷駅付近

# fromPolylineXY に座標のリストを渡して直線を引きます
feat.setGeometry(QgsGeometry.fromPolylineXY(points) 
feat.setAttributes(["直線のテスト"]) 
layer.addFeature(feat)

# 編集を保存
layer.commitChanges()

# 4. 線の見た目（スタイル）を設定する
# === QGIS line_style (線の種類) の設定値リスト ===
# 'solid'        : 実線（デフォルト）
# 'dash'         : 破線（少し長めの点線）
# 'dot'          : 点線（細かい点）
# 'dash dot'     : 一点鎖線（長・短・長・短）
# 'dash dot dot' : 二点鎖線（長・短・短・長）
# 'no'           : 線なし（透明にしたいとき）
symbol = QgsLineSymbol.createSimple({
    'color': 'orange',
    'line_width': '1.5',
    'line_style': 'solid' 
})

# 5. 単一シンボルレンダラーに設定して適用
renderer = QgsSingleSymbolRenderer(symbol)
layer.setRenderer(renderer)

# 6. 地図を更新して反映
layer.triggerRepaint()