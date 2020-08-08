from django.db import models  # type: ignore


class Value(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Principle(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
