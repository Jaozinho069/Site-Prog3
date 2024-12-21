from django.contrib import admin
from .models import Atividade

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'publicado', 'criado')
    list_filter = ('status', 'publicado')
    search_fields = ('titulo', 'descricao')
    prepopulated_fields = {'titulo': ('titulo',)}

    def get_model_perms(self, request):
        return super().get_model_perms(request)
    
