from django.core.management.base import BaseCommand
from blog.utils import fetch_and_save_articles  # assuming you saved the function here

class Command(BaseCommand):
    help = 'Fetch and store articles from RSS feed'

    def handle(self, *args, **options):
        fetch_and_save_articles()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved articles.'))
