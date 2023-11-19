from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Ammunition(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    """
    Model to create a weapon listing
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, null=False, blank=False)
    weight = models.CharField(max_length=20, null=False, blank=False)
    damage = models.IntegerField(null=False, blank=False)
    image = CloudinaryField("image", default="placeholder")
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
