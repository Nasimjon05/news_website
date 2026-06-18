from django.urls import  path
from .views import list_view, detail_view, ContactPageView, HomePageView, news_by_category, ForeignNewsView, \
    SportNewsView, TechNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('list/', list_view , name='list' ),
    path('foreign/', ForeignNewsView.as_view(), name='foreign' ),
    path('technology/', TechNewsView.as_view(), name='technology' ),
    path('sport/', SportNewsView.as_view(), name='sport' ),
    path('contact/', ContactPageView.as_view(), name='contact' ),
    path("<slug:slug>/", detail_view, name='detail' ),
    path('category/<int:category_id>/', news_by_category, name='news_by_category')
]