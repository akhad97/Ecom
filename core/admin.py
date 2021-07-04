from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, BillingAddress, Category, Slide


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'shipping_address',
                    'payment',
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'payment',
    ]
    list_filter = ['user',
                   'ordered',
                   'being_delivered',
                   'received',
                   ]
    search_fields = [
        'user__username',
        'ref_code'
    ]

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'region',
        'district',
        'zip',
        'address_type',
    ]
    list_filter = [ 'address_type', 'region', 'district']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    list_filter = ['title', 'category']
    search_fields = ['title', 'category']
    prepopulated_fields = {"slug": ("title",)}
    actions = [copy_items]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slide)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(BillingAddress, AddressAdmin)
