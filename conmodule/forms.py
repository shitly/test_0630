from django import forms


# 搜索表单
class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'search',
                   'placeholder': 'Search'})
    )
