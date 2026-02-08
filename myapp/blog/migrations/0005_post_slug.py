from django.db import migrations, models
from django.utils.text import slugify


def generate_unique_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        base_slug = slugify(post.title) or 'post'
        slug = base_slug
        counter = 1
        # Ensure uniqueness
        while Post.objects.filter(slug=slug).exclude(pk=post.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        post.slug = slug
        post.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_created_at'),
    ]

    operations = [
        # Step 1: Add slug field as nullable
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        # Step 2: Populate slugs for existing posts
        migrations.RunPython(generate_unique_slugs, migrations.RunPython.noop),
        # Step 3: Make slug non-nullable and unique
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
