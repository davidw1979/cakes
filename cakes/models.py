from django.db import models

# Create your models here.
class Catergory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"


class Cake(models.Model):
    name = models.CharField(max_length=64)
    catergories = models.ManyToManyField(Catergory)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    lead_in = models.IntegerField()
    pic_link = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.name} Price: £{self.price} Available in {self.lead_in} days."