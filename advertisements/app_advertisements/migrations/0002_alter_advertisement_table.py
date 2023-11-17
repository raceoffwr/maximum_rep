from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]