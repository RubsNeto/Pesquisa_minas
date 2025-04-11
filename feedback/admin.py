from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'atendimento', 'data_criacao')
    list_filter = ('atendimento', 'mix_produtos', 'atendimento_agil', 'valores_produtos', 'prazo_entrega')
    search_fields = ('nome', 'sugestao_melhoria')
    readonly_fields = ('data_criacao',)
    date_hierarchy = 'data_criacao'
