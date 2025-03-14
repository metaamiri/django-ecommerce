from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Listing, Price

@receiver(post_save, sender=Listing)
def create_initial_price(sender, instance, created, **kwargs):
    if created and instance.first_bid is not None:
        # ساخت نمونه جدید از مدل Price
        Price.objects.create(
            listing=instance,
            user=instance.user,  # سازنده لیستینگ به عنوان اولین کسی که قیمت می‌ذاره
            bid=instance.first_bid  # قیمت اولیه که در مدل listing ذخیره شده
        )
