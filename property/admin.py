from django.contrib import admin

from .models import Flat, Complaint, Owner



@admin.register(Flat)
class FlatModelAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('likers', )

@admin.register(Complaint)
class ComplaintModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')

@admin.register(Owner)
class OwnerModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )