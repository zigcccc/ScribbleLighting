from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

# Create your models here.
class Section(models.Model):

    SECTION_TITLE = (
        ('about_us', 'About Us'),
        ('our_work', 'Our Work'),
        ('contact_us', 'Contact Us')
    )

    section_title = models.CharField(
        choices = SECTION_TITLE,
        max_length = 50,
    )
    pub_date = models.DateTimeField(default=timezone.datetime.now())

    CREAM = 'e5e5e5'
    DARK = '222222'
    BACKGROUND_COLORS = (
        (CREAM, 'Cream'),
        (DARK, 'Dark')
    )

    section_color = models.CharField(
        max_length=6,
        choices = BACKGROUND_COLORS,
        default = CREAM
    )

    def __str__(self):
        return self.section_title

class Paragraph(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    paragraph_title = models.CharField(max_length=100)
    paragraph_text = models.TextField()

    def __str__(self):
        return self.paragraph_title


class ContactForm(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=100)
    email = models.EmailField()
