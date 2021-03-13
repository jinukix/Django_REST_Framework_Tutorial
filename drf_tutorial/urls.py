from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 자동 URL 라우팅을 사용해서 API를 연결해준다.
# 추가적으로 browsable API를 사용하기 위해 로그인 URl을 포함한다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]