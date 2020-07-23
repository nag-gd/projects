from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class CustomeManager(models.Manager):
    def order_by_name(self, f):
        return super().get_queryset().order_by(f)

    def sal_range(self,a,b):
        return super().get_queryset().filter(Experience__range=(a,b)).order_by('name')



class Contactinfo(models.Model):
    name=models.CharField(max_length=35, null=True)
    class Meta:
        abstract=True 

class Teacher(Contactinfo):
    Experience = models.IntegerField(null=True,)
    objects=CustomeManager()
    
    class Meta:
        db_table = 'music_album'


# class Student(Contactinfo):
#     grade = models.IntegerField(null=True)




class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    name = models.CharField(max_length=35, null=True)
    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )



    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):

    STATUS_CHOICES=[('draft','Draft'),('published','Published')]
    title = models.CharField(max_length=35)
    slug = models.SlugField(max_length=35, unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post', on_delete=models.CASCADE)
    body = models.TextField(default='No Input')
    publish = models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=65, choices=STATUS_CHOICES, default='Draft')
    

    # quary filters
    objects=PostManager()
    tags = TaggableManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_post", args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
        

