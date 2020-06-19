from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    friend = models.ForeignKey('Friend', on_delete=models.PROTECT, null=True, related_name='borrowed_books')
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Friend(models.Model):
    f_name = models.CharField(max_length=128)

    def __str__(self):
        return self.f_name
