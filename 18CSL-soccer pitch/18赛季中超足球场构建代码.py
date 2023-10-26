import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Arc

# 创建一个绘图窗口
fig, ax = plt.subplots(figsize=(15, 12))

# 定义球场大小和划分区域数量
field_width = 540
field_length = 360

# 绘制足球场

def convert_to_general_coordinates(
        x, y, 
        field_height, 
        y_min_general, y_max_general
        ):
    # 计算一般坐标系中的 y 坐标，
    # 将 y 映射到 [y_min_general, y_max_general] 范围内.
    y_mapped_general = (
        (y - 28) * 
        (y_max_general - y_min_general) / 
        (388 - 28) + y_min_general
        )
    
    # 返回一般坐标系中的 x 和 y 坐标
    return x, y_mapped_general  

# 足球场坐标
x_field = [41, 581, 581, 41, 41]
y_field = [388, 388, 28, 28, 388]

# 转换为一般坐标系
field_height = 500
x_general, y_general = zip(
    *[
     convert_to_general_coordinates(
         x, y, field_height, 388, 28
         ) for x, y in zip(
             x_field, y_field
             )
     ]
    )

# 定义右球门区的坐标（足球场坐标系）
goal_area_x1 = [41, 66, 66, 41]  # 球门区上边界的横坐标
goal_area_y1 = [252, 252, 165, 165]  # 球门区上边界的纵坐标

# 转换右球门区坐标为一般坐标系
goal_area_x1_general, goal_area_y1_general = zip(
    *[
      convert_to_general_coordinates(
          x, y, field_height, 388, 28
          ) for x, y in zip(
              goal_area_x1, goal_area_y1
              )
      ]
    )

# 定义左球门区的坐标（足球场坐标系）
goal_area_x2 = [581, 557, 557, 581]  # 球门区上边界的横坐标
goal_area_y2 = [165, 165, 252, 252]  # 球门区上边界的纵坐标

# 转换左球门区坐标为一般坐标系
goal_area_x2_general, goal_area_y2_general = zip(
    *[
    convert_to_general_coordinates(
        x, y, field_height, 388, 28
        ) for x, y in zip(
            goal_area_x2, goal_area_y2
            )
      ]
    )

# 绘制球门区，使用蓝色实线
plt.plot(goal_area_x1_general, goal_area_y1_general, 'k-', label='右球门区')
plt.plot(goal_area_x2_general, goal_area_y2_general, 'k-', label='左球门区')


#定义右罚球区的坐标（足球场坐标系）
penalty_area_x1 = [41, 119, 119, 41] #罚球区上边界的横坐标
penalty_area_y1 = [304, 304, 111, 111] #罚球区上边界的纵坐标

#定义左罚球区的坐标（足球场坐标系）
penalty_area_x2 = [581, 503, 503, 581] #罚球区上边界的横坐标
penalty_area_y2 = [111, 111, 304, 304] #罚球区上边界的纵坐标

# 转换罚球区坐标为一般坐标系
penalty_area_x1_general, penalty_area_y1_general = zip(
    *[
      convert_to_general_coordinates(
          x, y, field_height, 388, 28
          ) for x, y in zip(
              penalty_area_x1, penalty_area_y1
              )
      ]
    )


penalty_area_x2_general, penalty_area_y2_general = zip(
    *[
      convert_to_general_coordinates(
          x, y, field_height, 388, 28
          ) for x, y in zip(
              penalty_area_x2, penalty_area_y2
              )
      ]
    )

# 绘制罚球区，使用黑色实线
plt.plot(
    penalty_area_x1_general, 
    penalty_area_y1_general, 
    'k-', 
    label='右罚球区'
    )

plt.plot(
    penalty_area_x2_general, 
    penalty_area_y2_general, 
    'k-', 
    label='左罚球区'
    )


# 绘制足球场
plt.plot(x_general, y_general)
plt.gca().invert_yaxis()  # 反转Y轴以匹配一般坐标系

# 绘制足球场四边，使用黑色实线
plt.plot(
    [x_general[0], x_general[1]], 
    [y_general[0], y_general[1]], 
    'k-', label='四边'
    )
plt.plot(
    [x_general[1], x_general[2]], 
    [y_general[1], y_general[2]], 
    'k-'
    )
plt.plot(
    [x_general[2], x_general[3]], 
    [y_general[2], y_general[3]], 
    'k-'
    )
plt.plot(
    [x_general[3], x_general[0]], 
    [y_general[3], y_general[0]], 
    'k-'
    )

# 绘制中线
field_center_x = (max(x_general) + min(x_general)) / 2  # 计算中心点的横坐标

plt.plot(
    [field_center_x, field_center_x], 
    [max(y_general), min(y_general)], 
    'k-', label='中线'
    )

# 计算中圈的坐标（足球场坐标系）
center_circle_x = field_center_x
center_circle_y = 210  # 根据需要自行调整中圈的纵坐标

# 转换中圈坐标为一般坐标系
center_circle_x_general, center_circle_y_general = \
convert_to_general_coordinates(
    center_circle_x, 
    center_circle_y, 
    field_height, 388, 28
    )

# 绘制中圈，使用黑色实线
center_circle = Circle(
    (center_circle_x_general, center_circle_y_general), 
    45, color='k', fill=False, linestyle='-', label='中圈'
    )
plt.gca().add_patch(center_circle)

# 计算罚球弧的参数
# 右
penalty_spot_x1 = 119
penalty_spot_y1 = 210  # 根据需要自行调整罚球点的纵坐标
penalty_arc_radius = 45
penalty_arc1_start_angle = 270  # 弧的起始角度
penalty_arc1_end_angle = 450  # 弧的终止角度
 
# 左
penalty_spot_x2 = 503
penalty_spot_y2 = 210  # 根据需要自行调整罚球点的纵坐标
penalty_arc_radius = 45
penalty_arc2_start_angle = 90  # 弧的起始角度
penalty_arc2_end_angle = 270  # 弧的终止角度

# 创建并添加罚球弧到图上
penalty_arc = Arc(
    (penalty_spot_x1, penalty_spot_y1), 
    penalty_arc_radius * 2, 
    penalty_arc_radius * 2, angle=0.0, 
    theta1=penalty_arc1_start_angle, 
    theta2=penalty_arc1_end_angle, 
    color='k', linestyle='-', label='罚球弧'
    )
plt.gca().add_patch(penalty_arc)

penalty_arc = Arc(
    (penalty_spot_x2, penalty_spot_y2), 
    penalty_arc_radius * 2, 
    penalty_arc_radius * 2, angle=0.0, 
    theta1=penalty_arc2_start_angle, 
    theta2=penalty_arc2_end_angle, 
    color='k', linestyle='-', label='罚球弧'
    )
plt.gca().add_patch(penalty_arc)

# 设置坐标轴范围
ax.set_xlim(41, 581)
ax.set_ylim(28, 388)
plt.gca().invert_yaxis()  # 反转Y轴以匹配一般坐标系

plt.title("<--------away Offensive direction--------                         \
                                  ----------home Offensive direction------->")
plt.show()