from django.db import models
from django.core.exceptions import ValidationError


def validate_price(value):
    if value <= 0.0:
        raise ValidationError("Price must be greater than 0")
    return value


class Book(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="books/", null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    description = models.TextField(max_length=1000)
    author = models.ManyToManyField('Author', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, validators=[validate_price])
    genre = models.ManyToManyField('Genre', blank=True)
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['title', 'edition']]


class Edition(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30, null=True, blank=True)
    patronymic = models.CharField(max_length=50, null=True, blank=True)
    date_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        if self.surname is not None:
            return f"{self.name} {self.surname}"
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
