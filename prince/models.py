from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    message = RichTextUploadingField(max_length=500)
    timeStamp = models.DateField(auto_now_add=True ,blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
    


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Category(models.Model):
    category = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural= "Categories"
        ordering = ['-category']
    def __str__(self):
        return self.category
        
    def get_absolute_url(self):
        return reverse('blog')
    
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='')
    categories = models.ForeignKey(Category,verbose_name='Category',on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    snippet = RichTextUploadingField()

    class Meta:
        ordering = ['-created_on']
        

    def __str__(self):
        return self.title 
class PostComments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = RichTextUploadingField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)