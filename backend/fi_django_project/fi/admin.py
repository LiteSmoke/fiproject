from django.contrib import admin
from fi.models import (
    User,
    Transaction,
    TransactionCategory)


class TransactionAdmin(admin.ModelAdmin):
    """Transaction admin form customization"""

    fields = ('date', 'type', 'amount', 'description', 'category')
    date_hierarchy = 'date'
    list_display = ('date', 'type', 'amount', 'description', 'category')


class TransactionCategoryAdmin(admin.ModelAdmin):
    """Transaction category admin form customization"""

    fields = ('name', 'parent')
    list_display = ('id', 'name', 'parent')
    readonly_fields = ('id', )

admin.site.register(User)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionCategory, TransactionCategoryAdmin)