 
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_commande', views.add_commande, name='add_commande'),
    path('listes_commande', views.listes_commande, name='listes_commande'),
    path('edite_commande/<str:pk>/', views.edite_commande, name='edite_commande'),
    path('delete_commande/<str:pk>/', views.delete_commande, name='delete_commande'),
    
    #path('', include('django.contrib.auth.urls'))
    
    
]
