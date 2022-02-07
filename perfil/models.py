from re import M
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.db import models 
from stdimage.models import StdImageField    
from accounts.models import CustomUser 


class SocialNetwork(models.TextChoices):
    YOUTUBE = 'YOUTUBE', 'youtube'
    WHATSAPP = 'WHATSAPP', 'whatsapp'
    FACEBOOK = 'FACEBOOK', 'facebook'
    INSTAGRAM = 'INSTAGRAM', 'instagram'
    TWITTER = 'TWITTER', 'twitter'
    PINTEREST = 'PINTEREST', 'pinterest'
    SNAPCHAT = 'SNAPCHAT', 'snapchat'
    TIKTOK = 'TIKTOK', 'tiktok'
    DISCORD = 'DISCORD', 'discord'
    GITHUB = 'GITHUB', 'Github'

class IconSocialNetwork(models.Model):
        name = models.CharField( max_length=10, choices=SocialNetwork.choices, blank=True, null=True)
        icon = models.ImageField(upload_to='icon', blank=True, null=True)

        def __str__(self):
            return self.name 
  
            

class Profile(models.Model):   
        user = models.OneToOneField(CustomUser,  on_delete=models.CASCADE, related_name='profile') 
        image = StdImageField('Image', upload_to='profile', variations={'thumb': (500, 500, True)}, delete_orphans = True, blank=True)  
        occupation = models.CharField(max_length=120)
        description = models.TextField()  
        gender = models.CharField(max_length=20, blank=True)
        phone = models.CharField(max_length=20, blank=True)
        city = models.CharField(max_length=20, blank=True)
        country = models.CharField(max_length=20, blank=True)
        likes = models.ManyToManyField(CustomUser, blank=True, related_name='profile_likes')

        def __str__(self):
                return f' Profile: {self.user.username}'

        class Meta:
                verbose_name = "Profile"
                verbose_name_plural = "Profiles"
        
        @receiver(post_save, sender=CustomUser)
        def create_profile(sender, **kwargs):
                if kwargs.get('created', False):
                        Profile.objects.create(user=kwargs['instance'])

class Network(models.Model):
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='network', blank=True, null=True)  
        name = models.ForeignKey(IconSocialNetwork, on_delete=models.CASCADE, related_name="icon_social_network", blank=True, null=True)
        url = models.URLField(blank=True, null=True)

        def __str__(self):
                return f'{self.user or ""}, {self.name}'
        
        class Meta:
                verbose_name = "Network"
                verbose_name_plural = "Networks"
                ordering = ['user']

        @receiver(post_save, sender=CustomUser)
        def create_network(sender, ** kwargs):
                print("create_network")
                if kwargs.get('created', False): 
                        for i in IconSocialNetwork: 
                                Network.objects.create(name=i.id, user=kwargs['instance'])
         
                                
                                

       
