from django.urls import  path
from .views import  detail_view, ContactPageView, HomePageView, news_by_category, ForeignNewsView, \
    SportNewsView, TechNewsView , NewsUpdateView, NewsDeleteView, NewsCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign' ),
    path('technology/', TechNewsView.as_view(), name='technology' ),
    path('sport/', SportNewsView.as_view(), name='sport' ),
    path('contact/', ContactPageView.as_view(), name='contact' ),
    path('create/', NewsCreateView.as_view(), name='create' ),
    path("<slug:slug>/", detail_view, name='detail' ),
    path('<slug>/update/', NewsUpdateView.as_view(), name='update' ),
    path('<slug>/delete/', NewsDeleteView.as_view(), name='delete' ),
    path('category/<int:category_id>/', news_by_category, name='news_by_category')
]