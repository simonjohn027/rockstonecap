from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from  django.conf import settings
from django.views.generic import RedirectView


from accs.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^capital/', include('capital.urls')),

    url(r'^register/', register_view, name='register'),

    url(r'^login/', login_view, name='login'),

    url(r'^logout/', logout_view, name='logout'),
    url(r'^$', RedirectView.as_view(url='/capital/', permanent=True)),
    url(r'capital/', RedirectView.as_view(url='/capital/', permanent=True)),


]
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
