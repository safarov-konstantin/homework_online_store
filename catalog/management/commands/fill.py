import json
import os
from pathlib import Path
from catalog.models import Category, Product
from django.core.management import BaseCommand


PATH_DATA = os.path.join(Path(__file__).parent.parent.parent.parent, 'data.json')


class Command(BaseCommand):
    
    def handle(self, *args, **optioons):        
        # удаление данных  
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open(PATH_DATA, 'r', encoding='utf8') as file:
            data_json = json.load(file)
            
            category = [Category(pk=i['pk'], **i['fields']) for i in data_json if i['model'] == 'catalog.category']      

            products = []
            for i in data_json:
                if i['model'] == 'catalog.product':
                    
                    # Находим категорию для данного продукта
                    # Не придумал ничего лучше как перебрать все. Можно ли как-то упростить?
                    category_product = [j for j in category if j.pk == i['fields']['category']][0]
                              
                    product = Product(
                        pk=i['pk'],
                        name= i['fields']['name'],
                        description=i['fields']['description'],
                        image=i['fields']['image'],
                        category=category_product,
                        price=i['fields']['price'],
                        date_of_creation=i['fields']['date_of_creation'],
                        date_of_last_changing=i['fields']['date_of_last_changing']   
                    )
                    
                    products.append(product)
        
        Category.objects.bulk_create(category) 
        Product.objects.bulk_create(products)
                
        