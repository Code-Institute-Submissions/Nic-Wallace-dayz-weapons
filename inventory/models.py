from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
    slug = models.SlugField(max_length=200, default="name", unique=True)
    description = models.TextField(max_length=1000, null=False, blank=False)
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, null=False, blank=False)
    weight = models.CharField(max_length=20, null=False, blank=False)
    damage = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(10), MaxValueValidator(150)],
        null=False, blank=False)
    image = CloudinaryField("image", default="placeholder")
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    # def save(self, *args, **kwargs):
    #     self.slug = self.slug or slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name
