from django.shortcuts import render, reverse, HttpResponseRedirect
from mptt_app.models import FilingCabinet
from mptt_app.forms import FolderFileForm, RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from fc_user.models import FilingCabinetUser
from fc_user.forms import FCUserForm


def folderfile_view(request):
    all_folders_files = FilingCabinet.objects.all()
    return render(request, 'index.html', { 'all_folders_files': all_folders_files })


@login_required
def add_folderfile_view(request):
    if request.method == 'POST':
        form = FolderFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            folderfile = FilingCabinet.objects.create(
                name = data.get('name'),
                parent = data.get('parent'),
                created_by=request.user
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = FolderFileForm()
    return render(request, 'generic_form.html', { 'form': form })


@login_required
def user_cabinet_view(request):
    return render(request, 'user_cabinet.html', { 'data': FilingCabinet.objects.filter(created_by=request.user)})



def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = FilingCabinetUser.objects.create_user(
                display_name=data.get('display_name'),
                username=data.get('username'),
                password=data.get('password')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = RegistrationForm()
    return render(request, 'generic_form.html', { 'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, 
                username=data.get('username'), 
                password=data.get('password')
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', { 'form': form })



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))