# from django.contrib import admin
# from .models import Charges, Epilations, Maquillage, Ongles, Produits, Soins_Corps, Soins_Visages, Journees
#
# class Soins_corps_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'price', 'cost')
#     list_filter    = ('name', 'price', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
#
# class Soins_visage_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'price', 'cost')
#     list_filter    = ('name', 'price', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
# class Epilation_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'price', 'cost')
#     list_filter    = ('name', 'price', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
# class Maquillage_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'price', 'cost')
#     list_filter    = ('name', 'price', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
# class Ongles_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'price', 'cost')
#     list_filter    = ('name', 'price', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
# class Produits_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'price', 'cost')
#     list_filter    = ('name', 'price', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
# class Charges_Admin(admin.ModelAdmin):
#     list_display   = ('name', 'cost')
#     list_filter    = ('name', 'cost')
#     ordering       = ('name', )
#     search_fields  = ('name', )
#
# class Journees_Admin(admin.ModelAdmin):
#     list_display   = ('jour', 'ca', 'costs', 'result')
#     list_filter    = ('jour', 'ca', 'costs', 'result')
#     ordering       = ('jour', )
#     search_fields  = ('jour', )
#
# admin.site.register(Soins_Corps, Soins_corps_Admin)
# admin.site.register(Soins_Visages, Soins_visage_Admin)
# admin.site.register(Epilations, Epilation_Admin)
# admin.site.register(Maquillage, Maquillage_Admin)
# admin.site.register(Ongles, Ongles_Admin)
# admin.site.register(Produits, Produits_Admin)
# admin.site.register(Charges, Charges_Admin)
# admin.site.register(Journees, Journees_Admin)