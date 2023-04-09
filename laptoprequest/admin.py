from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import NewUser
from . import models

# Register your models here.

# class CustomNewUserAdmin(UserAdmin):
#     search_fields = ['username', 'first_name', 'last_name', 'email', 'user_id']
#     list_filter = ['role', 'is_active', 'is_staff']
#     list_per_page = 20
#     fieldsets = (
#         *UserAdmin.fieldsets, 
#         (
#             'Additional Info',
#             {
#                 'fields': ('role','user_id')
#             }
#         )
#     )
# admin.site.register(NewUser, CustomNewUserAdmin)

@admin.register(models.NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ['user_id','username', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name','username',  'email', 'user_id']
    list_filter = ['role', 'is_active', 'is_staff']
    ordering = ['first_name','last_name', 'username']
    list_per_page = 20
    fieldsets = (
        *UserAdmin.fieldsets, 
        (
            'Additional Info',
            {
                'fields': ('role','user_id')
            }
        )
    )


# admin.site.register(models.Computer)
@admin.register(models.Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['id', 'serial_number', 'last_update','status','os', 'ram', 'ssd', 'graphic_card', 'computer_classification']
    list_editable = ['status']
    ordering = ['last_update', 'computer_classification']
    list_filter = ['status', 'last_update','os','computer_classification']
    search_fields = ['id', 'serial_number']
    list_per_page = 20
    

# admin.site.register(models.Faculty)
@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_date', 'student_email','teacher_email', 'computer_sn', 'order_status', 'approved_date', 'approved', 'returned_date', 'returned']
    ordering = ['order_date']
    list_filter = ['order_date','order_status', 'approved_date', 'returned']
    search_fields = ['id', 'teacher_email', 'student_email']
    list_editable = ['order_status', 'approved', 'returned']
    list_per_page = 20

