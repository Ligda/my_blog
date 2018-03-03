"""编写视图函数"""

# 视图函数获取并处理网页所需的数据。
# 视图函数通常调用一个模板，后者生成浏览器能够理解的网页。

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 创建响应函数
def index(request):
    return(HttpResponse("Hello,world! I'm so happy to learning python!"))