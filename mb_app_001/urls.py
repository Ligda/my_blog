"""配置应用mb_app_001下的url"""

# 每个URL都被映射到特定的视图，通过视图函数调用模板。

from django.urls import path
from . import views

urlpatterns = [

    path('index/',views.index),

]
