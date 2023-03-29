from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from book.models import *


# Register your models here.

@admin.register(LibraryUser)
class User(UserAdmin):
    pass


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
