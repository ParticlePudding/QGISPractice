from qgis.core import (
    QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY,
    QgsField, QgsPalLayerSettings, QgsVectorLayerSimpleLabeling, QgsTextFormat,
    QgsSingleSymbolRenderer, QgsMarkerSymbol, Qgis
)
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor

# 新しい一時レイヤーを作成して地図に追加
layer = QgsVectorLayer("Point?crs=EPSG:4326", "TokyoStationLayer", "memory")
QgsProject.instance().addMapLayer(layer)

# フィールド（カラム）の定義と追加
layer.startEditing()
layer.dataProvider().addAttributes([QgsField("name", QVariant.String)])
layer.updateFields() # フィールド構成を更新

# 属性を持った地物（点）の追加
feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(139.767, 35.681)))
feat.setAttributes(["東京駅"])
layer.addFeature(feat)

# 編集を保存
layer.commitChanges()

# ラベルの表示設定
settings = QgsPalLayerSettings()
settings.fieldName = "name"
settings.isExpression = False
settings.placement = QgsPalLayerSettings.AroundPoint # 点の周りに配置する
settings.dist = 2.0 # 点からの距離
text_format = QgsTextFormat()
text_format.setSize(12) #テキストサイズ
text_format.setColor(QColor("black")) # テキスト色
settings.setFormat(text_format) 

# レイヤーにラベル設定を適用して、表示をONにする
labels = QgsVectorLayerSimpleLabeling(settings)
layer.setLabeling(labels)
layer.setLabelsEnabled(True)

# シンプルなマーカーシンボルを作成
symbol = QgsMarkerSymbol.createSimple({'name': 'circle', 'color': 'red'})

# 形を設定する
symbol.symbolLayer(0).setShape(Qgis.MarkerShape.Star)

# 色とサイズを設定する
symbol.symbolLayer(0).setFillColor(QColor(0, 255, 0, 150)) # 緑色、透明度150
symbol.symbolLayer(0).setStrokeColor(QColor('darkblue')) # 濃い青の枠線
symbol.symbolLayer(0).setStrokeWidth(0.5) # 枠線の太さ
symbol.setSize(8) # シンボルの大きさ

# 作成したシンボルを単一シンボルレンダラーに設定
renderer = QgsSingleSymbolRenderer(symbol)

# レイヤーにレンダラーを適用
layer.setRenderer(renderer)

# 12. 地図を更新して反映
layer.triggerRepaint()