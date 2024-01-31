from catalog.models import Category


def get_categories():
    all_category = Category.objects.all()
    return all_category