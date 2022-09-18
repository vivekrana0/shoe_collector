
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

OCCASIONS = (
    ('S', 'Sports'),
    ('C', 'Casual'),
    ('F', 'Formal')
)

class Cloth(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cloths_index')

class Shoe(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    cloths = models.ManyToManyField(Cloth)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})

class Reason(models.Model):
    date = models.DateField()
    occasion = models.CharField(
        max_length=1,
        choices=OCCASIONS,
        default=OCCASIONS[0][0]
    )

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_occasion_display()} on {self.date}"
        
    class Meta:
        ordering= ['-date']