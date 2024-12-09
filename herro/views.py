from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from herro.models import Exercice,Perf,All_Perf
from django.contrib.auth.decorators import login_required
from herro_project.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    
    return render(request,"herro\\index.html",)

def Mes_perfs(request):
    perfs = Perf.objects.filter(user=request.user)
    return render(request,"herro\\Mes_perfs.html",context={"perfs":perfs})

def add_exercice(request):
    exercices = Exercice.objects.all() 
    return render(request, 'herro\\add_exercice.html', {'exercices': exercices})

@login_required
def ajouter_performance(request):
    if request.method == 'POST':
        user = request.user
        exercice = request.POST.get('exercice')
        perf_value = request.POST.get('perf_value')
        public = request.POST.get('public') == 'on' 
        # Récupérer l'exercice correspondant
        exercice = get_object_or_404(Exercice, nom = exercice)
        # Enregistrer la performance dans un modèle Performance
        perf = Perf.objects.create(
            user=user,
            exercice=exercice,
            perf_value=float(perf_value),
            public=public
        )
        all_perf, _ =  All_Perf.objects.get_or_create(user=user)
        
        all_perf.perfs.add(perf)
        all_perf.save()         
                    
        return redirect('add_exercice') 
    return HttpResponse("Méthode non autorisée", status=405)

def search_users(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = User.objects.filter(
            Q(username__icontains=query) 
        )
    return render(request, 'herro\\search_results.html', {'query': query, 'results': results})
    