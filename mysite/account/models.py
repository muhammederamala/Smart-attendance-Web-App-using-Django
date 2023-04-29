from django.db import models
from django.contrib.auth.models import User


# class add_class is used to create a classroom by the teacher.

class add_class_model(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	subject = models.TextField()
	new_class = models.TextField()
	no_of_students = models.TextField()
	# add_button = models.CharField(max_length= 20)