# Generated by Django 4.1.7 on 2023-03-18 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptoprequest', '0007_request_student_f_n_request_student_l_n_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='student_f_n',
            new_name='student_first_name',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='student_l_n',
            new_name='student_last_name',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='teacher_f_n',
            new_name='teacher_first_name',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='teacher_l_n',
            new_name='teacher_last_name',
        ),
    ]
