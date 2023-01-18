from django.contrib import admin

from .models import Gamepark, Visitor, Payment, Warden, Wildlife_animal

class GameparkAdmin(admin.ModelAdmin):
    list_display = ("gamepark_name", "contact", "contact_person", "address")

class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visitor_name", "gender", "gamepark_id", "age", "contact", "address")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_date", "visitor_id", "amount_paid", "recieved_by")

class WardenAdmin(admin.ModelAdmin):
    list_display = ("warden_name", "address", "contact")

class Wildlife_animalAdmin(admin.ModelAdmin):
    list_display = ("spices_type", "no_of_spices", "warden_id", "recieved_by")


admin.site.register(Gamepark, GameparkAdmin)
admin.site.register(Visitor, VisitorAdmin )
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Warden)
admin.site.register(Wildlife_animal, Wildlife_animalAdmin)