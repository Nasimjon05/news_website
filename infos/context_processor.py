from .models import News, Category


def latest_news(request):
    news = News.published_news.all().order_by('-published')
    context = {'news':news}
    return context

def latest_politic(request):
    news = News.published_news.filter(category__name='Politics').order_by('-published').first()
    context = {'politic': news}
    return context
def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return context