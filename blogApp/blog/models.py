from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    """ This Class is an ORM for the DB Model,
    This model name is posts and it has a title,
    content of the post, date_posted which is the acutal
    date when this object is called upon and finally User.

    Since Django handles users and authentication for us, we
    import the same to here, the on_delete method is to delete
    all posts of the user when the user gets deleted
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
