from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    # joint table is images_image_users_like(id, image_id, user_id)
    # settings.AUTH_USER_MODEL is the end-point table
    # related_name attribute provides manager that allows to retrieve related objects as
    # image.users_like.all()
    # user.images_liked.all()
    # https://docs.djangoproject.com/en/4.1/ topics/db/examples/many_to_many/

    class Meta:
        indexes=[
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, * args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)

