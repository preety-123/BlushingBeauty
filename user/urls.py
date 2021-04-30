from django.urls import path
from BlushingBeauty import settings
from user import views
from django.conf.urls.static import static
from BlushingBeauty.settings import DEBUG,MEDIA_URL,MEDIA_ROOT

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('upload/', views.upload_products, name='upload-products'),
    path('home/update/<int:product_id>', views.update, name='update_book'),
    path('home/delete/<int:product_id>', views.delete, name='delete_book'),
    path('about/',views.about,name='about')
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)