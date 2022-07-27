from django.db import models
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from slugify import slugify
from bs4 import BeautifulSoup
import sys
import json
import uuid
import logging 
import re

class Student(models.Model):
    username = models.CharField(max_length=256,
                                null=False,
                                blank=False,
                                help_text='Username of Student')
    firstname = models.TextField(default="", help_text="First Name")

    lastname = models.TextField(default="", help_text="Last Name")

    email_id = models.TextField(default="", help_text="Email Id")
    password = models.CharField(max_length=256,
                                null=True,
                                blank=True,
                                help_text='Password of Student')
    created_on = models.DateTimeField(default=timezone.now)
    last_login_on = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
