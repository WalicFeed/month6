from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def add(x, y):
    print(f"args {x} and {y}")
    from time import sleep

    sleep(15)
    return x + y


@shared_task
def send_otp_mail(email, code):
    send_mail(
        subject="Your OTP code",
        message=f"code: {code}",
        from_email="SHOP_API",
        recipient_list=[email],
    )


@shared_task
def send_report_mail():
    send_mail(
        subject="Report",
        message="somthing important",
        from_email="SHOP_API",
        recipient_list=["riszav.01@gmail.com"],
    )


@shared_task
def send_heartbeat_mail():
    send_mail(
        subject="WE ARE ALIVE",
        message="shop_api is alive",
        from_email="SHOP_API",
        recipient_list=["riszav.01@gmail.com"],
    )


@shared_task
def print_current_time():
    from datetime import datetime
    with open(settings.BASE_DIR / "life", "a") as awake:
        awake.write(f"tick: {datetime.now()}\n")


@shared_task
def create_product(title, price, category_id, owner_id):
    from product.models import Product
    product = Product.objects.create(
        title=title,
        price=price,
        category_id=category_id,
        owner_id=owner_id,
    )
    print(f"created product: {product.title}")
    return product.id
