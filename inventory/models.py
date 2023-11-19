from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Ammunition(model.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def__str__(self):
        return self.name


class Attachment(model.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def__str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def__str__(self):
        return self.name


class Weapon(model.Model):
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

    class Meta:
        ordering = ["name"]

    def__str__(self):
        return self.name
