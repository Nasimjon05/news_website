from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .forms import ContactForm
from .models import News, Category

# Create your views here.



def detail_view(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {'news':news}
    return render(request, 'infos/news_detail.html', context)

def news_by_category(request, category_id):
    categories = Category.objects.all()[:3]

    featured_news = News.published_news.filter(
        category_id=category_id
    ).order_by('-published')[:10]
    featured_news_slider = featured_news[:2]
    featured_news_left = featured_news[2:6]
    featured_news_right = featured_news[6:10]


    foreign_news = News.objects.filter(category__name='Foreign')
    latest_news_slider_main = News.objects.filter().order_by('-published')[:4]

    context = {
        'categories': categories,
        'featured_news_left': featured_news_left,
        'featured_news_right': featured_news_right,
        'latest_news_slider_main': latest_news_slider_main,
        'featured_news_slider': featured_news_slider,
        'foreign_news': foreign_news,
    }

    return render(request, 'infos/index.html', context)



class HomePageView(ListView):
    model = News
    template_name = 'infos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()[:3]
        context['foreign_news'] = News.objects.filter(category__name='Foreign')[:14]

        # default category on homepage
        latest_news = News.published_news.filter().order_by('-published')
        context['latest_news_slider_main'] = latest_news[:4]
        context['featured_news_slider'] = latest_news[4:6]
        context['featured_news_left'] = latest_news[6:10]
        context['featured_news_right'] = latest_news[10:14]
        return context

class ForeignNewsView(ListView):
    model = News
    template_name = 'infos/foreign.html'
    context_object_name = 'foreign_news'

    def get_queryset(self):
        queryset = News.objects.filter(category__name='Foreign')
        return queryset

class SportNewsView(ListView):
    model = News
    template_name = 'infos/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        queryset = News.objects.filter(category__name='Sport')
        return queryset

class TechNewsView(ListView):
    model = News
    template_name = 'infos/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        queryset = News.objects.filter(category__name='Technology')
        return queryset


class ContactPageView(TemplateView):
    template_name = 'infos/contact.html'

    def get(self, request):
        form = ContactForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('Thank you for contacting me!')
        context = {'form':form}
        return render(request, self.template_name, context)

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'infos/crud/news_update.html'
    fields = ['title', 'body', 'image', 'status', 'category']

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'infos/crud/news_delete.html'
    success_url = reverse_lazy('home_page')

class NewsCreateView(CreateView):
    model = News
    template_name = 'infos/crud/news_create.html'
    fields = ['title', 'body', 'image', 'status', 'category']
    success_url = reverse_lazy('home_page')



