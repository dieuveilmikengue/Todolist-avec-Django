from django.shortcuts import redirect, render, HttpResponseRedirect
from .models import Taches
from .forms import AddTask

# Create your views here.


# Cette fonction permet d'afficher et d'ajouter une tache dans la base des données
def index(request):
    if request.method == 'POST':
        fm = AddTask(request.POST)
        if fm.is_valid():
            champ_title = fm.cleaned_data['title'] #On affecte les informations du champs qui seront supprimées après l'envoie
            champ_description = fm.cleaned_data['description'] #On affecte les informations du champs qui seront supprimées après l'envoie
            reg = Taches(title = champ_title, description = champ_description) #On efface les données dans le formurmulaire après l'envoie
            reg.save() #On enregistre les information dans la base des données
            fm = AddTask()
    else:
        fm = AddTask() #On ne fait absolument rien si le formulaire n'est pas remplie

    context = {"form":fm,
               "taches":Taches.objects.all()}
    return render(request, "todolist/index.html", context)

# Cette fonction permet de supprimer une tâche
def remove(request, id):
    pi = Taches.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect("/")

# Cette fonction permet de modifier une täche
def edit(request, id):
    pi = Taches.objects.get(pk=id)
    if request.method == 'POST':
        form = AddTask(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddTask(instance=pi)
    return render(request, "todolist/modif.html", {"form": form})