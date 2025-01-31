from django.db import models

class ArtCollection (models.Model):

    class Meta:
        verbose_name_plural = "Collections"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def return_friendly_name(self):
        return self.friendly_name

class Product (models.Model):

    art_collection = models.ForeignKey('ArtCollection', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    upvotes = models.IntegerField(null=True, blank=True)
    downvotes = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
