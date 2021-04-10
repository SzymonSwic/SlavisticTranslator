from django.shortcuts import render
from .forms import TextPostForm


def text_input(request):
    translated_txt = 'NOTHING TO SHOW'
    if request.method == 'POST':
        txtinput_form = TextPostForm(request.POST)
        if txtinput_form.is_valid():
            input_form_data = txtinput_form.cleaned_data
            translated_txt = input_form_data['content']
    else:
        txtinput_form = TextPostForm()
    return render(request, 'translator/translating_page.html', {'input_form': txtinput_form,
                                                                'translated_text': translated_txt})
