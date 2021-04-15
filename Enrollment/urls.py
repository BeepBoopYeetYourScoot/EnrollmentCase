from django.contrib import admin
from django.urls import path, include

from storage.router import router
from storage.views import total_cost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resources/', include(router.urls)),
    path('total_cost/', total_cost)
]
