import os
import django
import json
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lbl.settings')
if not settings.configured:
    django.setup()

from business.models import Business 


with open('dataset.json', 'r' ,encoding = 'utf-8') as file:
    data = json.load(file)

extracted_data = []
extracted_data = [
    {'title': item['title'], 'category': item['categoryName'], 'location': item['location']}
    for item in data
]

def import_stores():
    for item in extracted_data:
        print("Title:", item['title'])
        Business.objects.create(
            name=item['title'],
            address='',
            category=item['category'],
            longtitude=item['location']['lng'],
            latitude=item['location']['lat']
        )

if __name__ == "__main__":
    import_stores()
    print("Data imported successfully")



# print(creat['title'], creat['location'])