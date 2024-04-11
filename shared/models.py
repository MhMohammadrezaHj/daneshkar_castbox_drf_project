from django.db import models


class BaseModel(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ("pk",)

    # def __str__(self) -> str:
    #     raise NotImplementedError("You should implement __str__ method.")
