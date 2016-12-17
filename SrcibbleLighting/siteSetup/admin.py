from django.contrib import admin

from django.db import models

from .models import ContactForm, Paragraph, Section

# Register your models here.
class ParagraphInLine(admin.TabularInline):
    model = Paragraph
    extra = 1

class ContactInfo(admin.StackedInline):
    model = ContactForm
    extra = 0

class SectionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Settings', {'fields': ['section_title', 'section_color']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ParagraphInLine, ContactInfo]
    list_display = ('section_title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['section_title']


admin.site.register(Section, SectionAdmin)
