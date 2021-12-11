from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=256, blank=True)
    #price = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    #created = models.DateTimeField(auto_now_add=True)
    #published = models.DateField(null=True, blank=True)
    #is_published = models.BooleanField(default=False)
    #cover = models.ImageField(upload_to='media/covers/',blank=True)
    #bookcopy = models.FileField(upload_to='media/bookcopy/',blank=True)
    #number = models.OneToOneField(BookNumber,null=True,blank=True,on_delete=models.CASCADE)
    
    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)
    
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        
        for rating in ratings:
            sum += rating.stars
            
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    
    def __str__(self):
        return self.title
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)



