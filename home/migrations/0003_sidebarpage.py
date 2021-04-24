# Generated by Django 3.2 on 2021-04-24 04:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0002_auto_20210418_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='SidebarPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([('column_2_1', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())]))], grid_width=12, group='Columns', template='blocks/two_column_block.html'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]