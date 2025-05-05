from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_location = models.CharField(max_length=50, default="Unknown")
    user_profile = models.ImageField(upload_to="images/user")
    Otp_Status = models.TextField(default = 'pending', max_length = 60, null = True)
    Last_Login_Time = models.TimeField(auto_now_add=True,null = True)
    Last_Login_Date = models.DateField(auto_now_add=True,null = True)
    No_Of_Times_Login = models.IntegerField(default = 0, null = True)
    Message = models.TextField(max_length=250,null=True)
    status = models.CharField(max_length=15, default="Pending")
    otp = models.CharField(max_length=6, default=0)

    class Meta:
        db_table = "User_details"


class UserFeedbackModels(models.Model):
    feed_id = models.AutoField(primary_key=True)
    star_feedback = models.TextField(max_length=900)
    star_rating = models.IntegerField()
    star_Date = models.DateTimeField(auto_now_add=True, null=True)
    user_details = models.ForeignKey(User, on_delete=models.CASCADE)
    sentment = models.TextField(max_length=20,null=True)
    class Meta:
        db_table = 'feedback_table'