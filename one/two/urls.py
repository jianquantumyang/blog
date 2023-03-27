from . import views
from django.urls import path

urlpatterns = [
    path('',views.IndexHome.as_view(),name="index"),
    path('addpage/',views.AddPage.as_view(),name="addpage"),
    path('about/',views.about,name="about"),

    path('post/<int:post_id>/',views.post,name="post"),
    path('categoryadd/',views.post_category_add,name="category_add"),
    path('category/<int:cat_id>',views.show_category,name='category')
]
