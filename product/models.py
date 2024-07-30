from django.db import models
from django.contrib.auth import get_user_model

Users = get_user_model()

RATING = (
    (1, '★✩✩✩✩'),
    (2, '★★✩✩✩'),
    (3, '★★★✩✩'),
    (4, '★★★★✩'),
    (5, '★★★★★'),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.IntegerField(default=None, choices=RATING)
    review_text = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("user", "product")


