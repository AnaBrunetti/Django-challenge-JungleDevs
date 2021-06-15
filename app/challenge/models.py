from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import uuid


# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False, auto_created=True)
    name = models.CharField("Name", max_length=255)
    picture = models.ImageField("Picture", upload_to='uploads/authors/pictures/', help_text='The ideal dimension is 84x84. The max size is 2 MB.')
    additional_information = models.CharField("Additional Information", max_length=200)
    is_active = models.BooleanField("Is Active?")

    created_at = models.DateTimeField('Created At', auto_now=True)
    updated_at = models.DateTimeField('Updated At', auto_now_add=True)

    def clean(self, *args, **kwargs):
        if not self.picture:
            raise ValidationError("Picture field is required.")
        
        file_size = self.picture.file.size
        limit = 2097152 #2 mb
        if file_size > limit:
            raise ValidationError("Max size of file is 2 MB")
    
    def __str__(self):
        return self.name+' - '+self.additional_information

    class Meta:        
        verbose_name = "Author"
        verbose_name_plural = "Authors"



class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False, auto_created=True)
    author = models.ForeignKey(Author, verbose_name="Author", on_delete=models.CASCADE)
    category = models.CharField("Category", max_length=125)
    title = models.CharField("Title", max_length=255)
    summary = models.TextField("Summary")
    content = RichTextField()
    is_active = models.BooleanField("Is Active?")

    created_at = models.DateTimeField('Created At', auto_now=True)
    updated_at = models.DateTimeField('Updated At', auto_now_add=True)

    def __str__(self):
        return self.title+' - '+self.category

    class Meta:        
        verbose_name = "Article"
        verbose_name_plural = "Articles"