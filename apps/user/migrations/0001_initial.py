# Generated by Django 3.1.2 on 2021-07-11 16:24

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('permission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('name', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '部门管理',
                'verbose_name_plural': '部门管理',
                'db_table': 'user_department',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='', max_length=20, verbose_name='中文姓名')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/user/%Y/%m/%d/')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='邮箱')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='职位')),
                ('staff_id', models.IntegerField(blank=True, null=True, verbose_name='员工编号')),
                ('job_status', models.BooleanField(default=True, verbose_name='员工在职状态')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='手机号码')),
                ('remarks', models.TextField(blank=True, default=None, null=True, verbose_name='备注')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='user.department', verbose_name='部门')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role', models.ManyToManyField(blank=True, related_name='user', to='permission.Role', verbose_name='角色')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
