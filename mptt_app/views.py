from django.shortcuts import render, reverse, HttpResponseRedirect
from mptt_app.models import FilingCabinet
from mptt_app.forms import FolderFileForm


def folderfile_view(request):
    all_folders_files = FilingCabinet.objects.all()
    return render(request, 'index.html', { 'all_folders_files': all_folders_files })



def add_folderfile_view(request):
    if request.method == 'POST':
        form = FolderFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            folderfile = FilingCabinet.objects.create(
                name = data.get('name'),
                parent = data.get('parent')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = FolderFileForm()
    return render(request, 'generic_form.html', { 'form': form })