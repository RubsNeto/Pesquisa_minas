from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback

def feedback_form(request):
    return render(request, 'forms.html')

def enviar_feedback(request):
    if request.method == 'POST':
        Feedback.objects.create(
            nome=request.POST.get('nome'),
            atendimento=request.POST.get('atendimento'),
            mix_produtos=request.POST.get('mix_produtos'),
            atendimento_agil=request.POST.get('atendimento_agil'),
            valores_produtos=request.POST.get('valores_produtos'),
            prazo_entrega=request.POST.get('prazo_entrega'),
            sugestao_melhoria=request.POST.get('sugestao_melhoria')
        )
        return redirect('thank_you')
    return redirect('feedback_form')

def thank_you(request):
    return render(request, 'thank_you.html')