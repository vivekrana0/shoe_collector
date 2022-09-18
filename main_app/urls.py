from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='index'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_reason/', views.add_reason, name='add_reason'),
    #cloth paths

    path('cloths/', views.ClothList.as_view(), name='cloths_index'),
    path('cloths/create', views.ClothCreate.as_view(), name='cloths_create'),
    path('cloths/<int:pk>/', views.ClothDetails.as_view(), name='cloths_detail'),
    path('cloths/<int:pk>/update', views.ClothUpdate.as_view(), name='cloths_update'),
    path('cloths/<int:pk>/delete', views.ClothDelete.as_view(), name='cloths_delete'),

    path('cloths/<int:shoe_id>/<int:cloth_id>/add', views.add_attribute, name='add_attribute'),
    path('cloths/<int:shoe_id>/<int:cloth_id>/remove', views.remove_attribute, name='remove_attribute'),

    path('accounts/sigup/', views.signup, name='signup')
]