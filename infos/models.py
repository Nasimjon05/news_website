from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from unicodedata import category


class Published(models.Manager):
    def get_queryset(self):
        return super(Published, self).get_queryset().filter(status='PB')
class Economic(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category__name = "Economy")
# Create your models here.
class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF' # draft
        PUBLISHED = 'PB' # published
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published_news = Published()
    economic_news = Economic()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-published']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    fname = models.CharField(max_length=100 ,default="noname")
    lname = models.CharField(max_length=100, default="noname")
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email
