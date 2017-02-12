# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
# from .forms import UploadFileForm
from django.shortcuts import render

from getemotion.models import Document
from getemotion.forms import DocumentForm
# from django.views.decorators.csrf import csrf_exempt

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

# def handleupload(request):
# 	if request.POST:
# 		form = UploadFileForm(request.POST, request.FILES)
def list(request):
    # Handle file upload

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print form
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )