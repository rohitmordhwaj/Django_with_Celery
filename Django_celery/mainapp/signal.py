from django.dispatch import Signal, receiver

notification = Signal(providing_args=["request", "user"])

# implemented custom signal for sending notification
@receiver(notification)
def notification_alert(sender, **kwargs):
    print(sender)
    print(kwargs)
    print("Notification has been send")