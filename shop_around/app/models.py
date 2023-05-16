from django.db import models


class Pol(models.Model):
    title = models.CharField(max_length=255, default="a")

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=255, default="a")

    def __str__(self):
        return f'{self.title}'


class Size(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} | {self.title}'


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview_img = models.ImageField(upload_to="products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pol = models.ForeignKey(Pol, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} | {self.description[:50]} | {self.category} | {self.price} | {self.pol} | {" ".join([i.title for i in self.size.all()])}'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.title}'
