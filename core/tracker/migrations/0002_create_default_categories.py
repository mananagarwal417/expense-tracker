from django.db import migrations


DEFAULT_CATEGORIES = [
    'Salary',
    'Freelance',
    'Bonus',
    'Business',
    'Gift Received',
    'Interest',
    'Investment',
    'Rental Income',
    'Food',
    'Groceries',
    'Dining Out',
    'Transport',
    'Utilities',
    'Rent',
    'EMI',
    'Insurance',
    'Education',
    'Shopping',
    'Clothing',
    'Healthcare',
    'Entertainment',
    'Travel',
    'Subscriptions',
    'Taxes',
    'Mobile Recharge',
    'Pets',
    'Personal Care',
    'Home Maintenance',
    'Charity',
    'Other',
]


def create_default_categories(apps, schema_editor):
    Category = apps.get_model('tracker', 'Category')
    for name in DEFAULT_CATEGORIES:
        Category.objects.get_or_create(name=name)


def remove_default_categories(apps, schema_editor):
    Category = apps.get_model('tracker', 'Category')
    for name in DEFAULT_CATEGORIES:
        Category.objects.filter(name=name).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories, remove_default_categories),
    ]
