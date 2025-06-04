"""
pyecharts基础
"""

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 折线图
line = Line()
line.add_xaxis(["土豆","番茄","苹果"])
line.add_yaxis("个数",["1","2","3"])

# 全局配置选项
line.set_global_opts(
    title_opts = TitleOpts(title="标题", pos_left="center",pos_bottom="1%"),
#前后之间的，
    legend_opts = LegendOpts(is_show=True
    ),
    toolbox_opts = ToolboxOpts(
        is_show=True
    ),
    visualmap_opts = VisualMapOpts(
        is_show=True
    )
)

# 通过render方法，将代码生成图像
line.render()