from tkinter import N
import uuid
from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class CustomUser(models.Model):
    my_id= models.TextField()
    username= models.CharField(max_length=500, unique=True)
    password= models.CharField(max_length=128)
    type= models.CharField(max_length=128)
    is_active= models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    timestamp= models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'date: {str(self.timestamp)} username: {self.username}'

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.id = str(uuid.uuid4())
    #     super().save(*args, **kwargs)


class UserProfile(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField()
    profile_image= models.FileField(null=True, blank=True, upload_to='user/profile_image')
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'profile{self.user.pk}'

class Business(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    business_name= models.CharField()
    phone= models.CharField(max_length=250)
    gst= models.CharField(max_length=250)
    since= models.CharField(max_length=250)
    segment= models.TextField()
    catigory= models.TextField()
    badge= models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'business name{self.business_name.pk} : GST: {self.gst}'

class BusinessProfile(models.Model):
    business= models.ForeignKey(Business,on_delete=models.CASCADE, null=True, blank=True)
    primary_image= models.FileField(null=True, blank=True , upload_to='business/primary_image')
    secondary_images= models.FileField(null=True, blank=True, upload_to='business/secondary_images')
    about= models.TextField()
    youtube_link= models.TextField()

    def __str__(self):
        return f'business profile{self.business.pk}'
    
class BusinessLocation(models.Model):
    business= models.ForeignKey(Business,on_delete=models.CASCADE, null=True, blank=True)
    pin_code= models.CharField(max_length=500)
    city= models.CharField(max_length=500)
    state= models.CharField(max_length=500)
    country= models.CharField(max_length=500)
    location_link= models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'State: {self.state}  business location{self.business.pk}'

class Subscription(models.Model):
    detail= models.TextField()
    services= models.TextField()
    is_active= models.BooleanField(default=False)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'review:{self.review} rating:{self.rating}'

class Plan(models.Model):
    business= models.ForeignKey(Business,on_delete=models.CASCADE, null=True, blank=True)
    services= models.TextField()
    is_active= models.BooleanField(default=False)
    plan_summary= models.TextField()
    last_activate= models.DateTimeField(auto_now_add=True)
    expire_date= models.DateTimeField(auto_now_add=True)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'is_active:{self.is_active} expire_date:{self.expire_date}'

class LeadQuery(models.Model):
    business= models.ForeignKey(Business,on_delete=models.CASCADE, null=True, blank=True)
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=500,default='')
    email= models.CharField(max_length=500,default='')
    phone= models.CharField(max_length=500,default='')
    state= models.CharField(max_length=500,default='')
    city= models.CharField(max_length=500,default='')
    country= models.CharField(max_length=500,default='')
    query= models.TextField(default='')
    status= models.TextField(default='')
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'phone:{self.phone} query:{self.query}'

class PlanQuery(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    email= models.CharField(max_length=500,default='')
    phone= models.CharField(max_length=500,default='')
    stage= models.CharField(max_length=500,default='') #{"1":"Lead","2":"Contacted","3":"Followed Up","4":"Closed"}
    attachment= models.FileField(null=True, blank=True, upload_to='lead_query/attachment')
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'phone:{self.phone} stage:{self.stage}'


class Feedback(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    contact= models.CharField(max_length=500) # lable : Contact detail 
    feedback= models.TextField() # lable : Feedback rating
    status= models.TextField() # lable : [view,]
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'contact:{self.contact} feedback:{self.feedback}'

class Blog(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    title= models.TextField() 
    cover= models.FileField(null=True, blank=True,upload_to='blog/cover')
    description=QuillField(null=True, blank=True)
    author= models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'author {self.author} title:{self.title} timestamp:{self.timestamp}'

class Constants(models.Model):
    segments= models.TextField() # {'manu':Manugraturer, 'retailer':Retailer}
    catigory= models.TextField() # {'manu':[furniture,lighting,decor,flooring,wall_coverings,window_treatments,home_textiles,kitchen_cabinets], 'retailer':[bathroom_fixtures,toilets,faucets,sinks,showers,bathtubs,bathroom_accessories,water_systems]}
    payment_detail = models.TextField()
    payment_qr = models.FileField(null=True, blank=True ,upload_to='payment_qr')
    def __str__(self):
        return f' pk {self.pk} segments:{self.segments}'

class Banners(models.Model):
    support_text = models.TextField()
    title = models.TextField()
    banner = models.FileField(null=True, blank=True ,upload_to='banners')
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f' pk {self.pk} title:{self.title}'

class OfferHeading(models.Model):
    title = models.TextField()
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f' pk {self.pk} title:{self.title}'


