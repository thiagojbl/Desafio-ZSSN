from django.contrib import admin

from api.models import (Itens, Negociar, Sinalizar, Sobrevivente,
                        SobreviventeInventario)


class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'infectado')
    search_fields = ('nome', 'idade')


class ItensAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pontos')


class SobreviventeInventarioAdmin(admin.ModelAdmin):
    list_display = ('sobrevivente', 'item', 'quantidade')


class SinalizarAdmin(admin.ModelAdmin):
    list_display = ('sobrevivente', 'sobrevivente_infectado')


class NegociarAdmin(admin.ModelAdmin):
    list_display = ('sobrevivente1', 'sobrevivente2')

admin.site.register(Sobrevivente, SobreviventeAdmin)
admin.site.register(Itens, ItensAdmin)
admin.site.register(SobreviventeInventario, SobreviventeInventarioAdmin)
admin.site.register(Sinalizar, SinalizarAdmin)
admin.site.register(Negociar, NegociarAdmin)

