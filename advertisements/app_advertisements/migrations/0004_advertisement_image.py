from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]