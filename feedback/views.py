from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Feedback

def feedback_form(request):
    return render(request, 'forms.html')

def enviar_feedback(request):
    if request.method == 'POST':
        # Coletar dados do formulário
        nome = request.POST.get('nome')
        atendimento = request.POST.get('atendimento')
        mix_produtos = request.POST.get('mix_produtos')
        atendimento_agil = request.POST.get('atendimento_agil')
        valores_produtos = request.POST.get('valores_produtos')
        prazo_entrega = request.POST.get('prazo_entrega')
        sugestao_melhoria = request.POST.get('sugestao_melhoria')
        
        # Criar novo objeto Feedback
        Feedback.objects.create(
            nome=nome,
            atendimento=atendimento,
            mix_produtos=mix_produtos,
            atendimento_agil=atendimento_agil,
            valores_produtos=valores_produtos,
            prazo_entrega=prazo_entrega,
            sugestao_melhoria=sugestao_melhoria
        )
        
        # Redirecionar para página de agradecimento
        return redirect('thank_you')
    
    # Se não for POST, redirecionar para o formulário
    return redirect('feedback_form')

def thank_you(request):
    return render(request, 'thank_you.html')

class RespostasPesquisaView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Feedback
    template_name = 'respostas.html'
    context_object_name = 'feedbacks'
    ordering = ['-data_criacao']
    paginate_by = 10
    
    # Redireciona para login se não estiver autenticado
    login_url = '/admin/login/'
    
    # Verifica se o usuário é superusuário (admin)
    def test_func(self):
        return self.request.user.is_superuser