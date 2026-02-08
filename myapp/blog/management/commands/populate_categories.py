from typing import Any
from unicodedata import category
from blog.models import Category
from django.core.management.base import BaseCommand


    
class Command(BaseCommand):
    help = "This command populates the database with sample blog categories"

    def handle(self, *args: Any, **options: Any):
        #Delete existing data
        Category.objects.all().delete()
        
        categories = [ 'Sports', 'Technology', 'Science', 'Art', 'Food',]
        
        for category_name in categories:
            Category.objects.create(name=category_name)
            
        self.stdout.write(self.style.SUCCESS("Completed inseting data!"))