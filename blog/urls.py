from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # post/ はURLが post に続けて / で始まることを意味
    # <int:pk> はDjangoは整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味
    # URLの最後に再び / が必要
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]