from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Applications, Balance, Warehouse
from .forms import ChangeAppForm, NewAppForm


# Create your views here.
@login_required
def index(request):
    open_apps = Applications.objects.filter(master=request.user, status='a')
    if request.method == 'POST' and 'close_app' in request.POST:
        pk = request.POST.get('current_id')
        current_app = get_object_or_404(Applications, pk=pk)
        form = ChangeAppForm(request.POST, request.FILES, instance=current_app)
        if form.is_valid():
            current_app.status='c'
            form.save()
            return redirect('ticketSystem:index')
    else:
        form = ChangeAppForm()


    if request.method == 'POST' and 'fast_close' in request.POST:
        pk = request.POST.get('current_id')
        current_app = get_object_or_404(Applications, pk=pk)
        current_app.status='c'
        current_app.save()



    context = {'open_apps':open_apps, 'form':form}
    return render(request, 'ticketSystem/index.html', context)

@login_required
def completed(request):
    completed_apps = Applications.objects.filter(master=request.user, status='c')
    balance = Balance.objects.get(holder=request.user)
    warehouse = Warehouse.objects.get(owner=request.user)
    context = {'completed_apps':completed_apps, 'balance':balance, 'warehouse':warehouse}
    return render(request, 'ticketSystem/completed.html', context)


@login_required
def create_new_app(request):
    if request.method == 'POST':
        create_form = NewAppForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('ticketSystem:create_new_app')
    else:
        create_form = NewAppForm()
    context = {'create_form': create_form}
    return render (request, 'ticketSystem/create_new_app.html', context)

@login_required
def balance_template(request):
    apps = Applications.objects.filter(master=request.user, status='c', handed_over=False)
    balance = Balance.objects.get(holder=request.user)
    equpiment = Warehouse.objects.get(owner=request.user)
    if request.method == 'POST' and 'handed_over' in request.POST:
        pk = request.POST.get('current_app')
        current_app = get_object_or_404(Applications, pk=pk)
        current_app.handed_over=True
        current_app.save()
        balance.save()
    context = {'apps':apps, 'balance':balance, 'equpiment':equpiment}
    return render(request, 'ticketSystem/balance.html', context)

