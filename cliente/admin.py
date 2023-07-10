from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class NomeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'rg', 'celular', 'ativo']
    list_per_page = 13
    search_fields = ['nome', 'cpf']
    list_filter = ['ativo']
    ordering = ['nome']




