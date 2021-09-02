# Generated by Django 3.2.6 on 2021-08-30 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('templates', '0002_rename_template_tag_templatetag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_templates', to='tags.tag'),
        ),
        migrations.AlterField(
            model_name='templatetag',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template_tags', to='templates.template'),
        ),
    ]
