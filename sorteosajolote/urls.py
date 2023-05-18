from django.contrib import admin
from django.urls import path, include
from lottery import views as lottery_views

admin.site.site_header = "Sorteos Ajolote"
admin.site.site_title = 'Sorteos Ajolote'
admin.site.site_url = '/'
admin.site.index_title = "Admin"

urlpatterns = [
    path ('', lottery_views.index, name = 'index'),
    path ('admin/', admin.site.urls),
    path ('lottery/', include ('lottery.urls')),
]
