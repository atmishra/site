# Generated by Django 2.2.6 on 2019-11-16 20:00

from django.db import migrations, models
import pydis_site.apps.api.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_offensivemessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('invite', 'invite'), ('extension', 'extension'), ('channel', 'channel'), ('role', 'role')], help_text='Type of the whitelisted item.', max_length=100)),
                ('whitelisted_item', models.CharField(help_text='whitelisted item', max_length=300)),
            ],
            bases=(pydis_site.apps.api.models.utils.ModelReprMixin, models.Model),
        ),
    ]