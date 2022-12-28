from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reated_at = models.DateTimeField(
        auto_now_add=True)

    def str(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20,
                             unique=True)

    def str(self):
        return self.title