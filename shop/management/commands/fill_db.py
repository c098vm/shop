from django.core.management import BaseCommand

from shop.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {
                'name': 'Одежда',
                'description': 'Спортивная одежда для активного отдыха',
                'create_at': '2005-04-13'
            },
            {
                'name': 'Инвентарь',
                'description': 'Спортивный иныентарь для залов и домашнего пользования',
                'create_at': '1999-06-10'
            },
            {
                'name': 'Обувь',
                'description': 'Удобная и практичная обувь для прогулок и занятий спортом',
                'create_at': '2004-04-13'
            }
        ]

        product_list = [
            {
                'name': 'Ракетка',
                'description': 'Для большого тенниса',
                'category': 2,
                'price': 1500.00,
                'create_date': '2022-02-23',
                'last_change_date': '2022-08-03'
            },
            {
                'name': 'Ветровка',
                'description': 'Для защиты от дождя и ветра',
                'category': 1,
                'price': 3700.00,
                'create_date': '2023-04-13',
                'last_change_date': '2023-06-09'
            },
            {
                'name': 'Ботинки',
                'description': 'Лыжные, система крепления unifix',
                'category': 3,
                'price': 6150.00,
                'create_date': '2022-12-10',
                'last_change_date': '2023-04-12'
            }
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
