import gpxpy

dir = r"./files/"

# 读取第一个gpx文件
with open(dir + '1.gpx', 'r', encoding='UTF-8') as gpx_file1:
    gpx1 = gpxpy.parse(gpx_file1)

# 读取第二个gpx文件
with open(dir + '2.gpx', 'r', encoding='UTF-8') as gpx_file2:
    gpx2 = gpxpy.parse(gpx_file2)

# 将第二个gpx文件中的所有轨迹点添加到第一个gpx文件中
for track in gpx2.tracks:
    gpx1.tracks.append(track)

# 将第二个gpx文件中的所有路线点添加到第一个gpx文件中
for route in gpx2.routes:
    gpx1.routes.append(route)

# 将第二个gpx文件中的所有航点添加到第一个gpx文件中
for waypoint in gpx2.waypoints:
    gpx1.waypoints.append(waypoint)

# 将合并后的gpx数据写入新的gpx文件中
with open(dir + 'merge.gpx', 'w', encoding='UTF-8') as merged_file:
    merged_file.write(gpx1.to_xml())

with open(dir + 'merge.gpx', 'r', encoding='utf-8') as test:
    for line in test:
        print(line)
