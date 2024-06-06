from osgeo import ogr

def Traverse_objects(shapefile_path):
    dataSource = ogr.Open(shapefile_path, 0) 

    if dataSource is None:
        print(f"无法打开文件 {shapefile_path}")
    else:
        layer = dataSource.GetLayer()

        for feature in layer:
            geometry = feature.GetGeometryRef()
            if geometry is not None and geometry.GetGeometryType() == ogr.wkbPolygon:
                roof_type = feature.GetField('roof_type')
                height = feature.GetField('height')

                print(f"Geometry: {geometry}")
                print(f"Roof Type: {roof_type}")
                print(f"Height: {height}")
                print("-" * 40)

        # 关闭数据源
        dataSource = None
