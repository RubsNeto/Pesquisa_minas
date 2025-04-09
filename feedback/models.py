from django.db import models

class Feedback(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    atendimento = models.CharField(max_length=20)
    mix_produtos = models.CharField(max_length=30)
    atendimento_agil = models.CharField(max_length=30)
    valores_produtos = models.CharField(max_length=30)
    prazo_entrega = models.CharField(max_length=30)
    sugestao_melhoria = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback de {self.nome} - {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"