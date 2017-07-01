from django.shortcuts import render
from .forms import SearchForm

from .models import WordTags, MetaWord, Meta2Lib


# 通过一个关键词的搜索, 返回对应的结果
def get_words_url_from_word_tags(string):
    return WordTags.objects.all()


# Create your views here.
def serch(request):
    if request.method == 'GET':
        form = SearchForm()
        return render(request, 'search_init.html', {'form': form})

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['search']
        res = get_words_url_from_word_tags(form.search)
        return render(request, "search.html", {
            "res": res
        })