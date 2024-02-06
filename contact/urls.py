from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    # Adicione outras URLs específicas deste arquivo, se necessário
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

