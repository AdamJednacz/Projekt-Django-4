# Generated by Django 4.1 on 2024-05-24 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0004_alter_task_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="Done",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("clicks", models.IntegerField(default=0)),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="www.task"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
