from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # new 30.07.2020 /// 1
    path('accounts/', include('accounts.urls')),  # new 30.07.2020 /// 2
    path('', include('blog.urls')),  # new
]
