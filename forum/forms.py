from django import forms
from pagedown.widgets import PagedownWidget
from forum.models import Post


class PostForm(forms.ModelForm):
    """Form to show the pagedown markdown"""
    title = forms.CharField(max_length=300, label='',
                            widget=forms.TextInput({
                                'class': 'title-input',
                                'placeholder': "What's your question? Insert here.",
                            }))
    post_field = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'post_field',
        ]


# class ForumPost(forms.ModelForm):
#     """Form to display title and question"""
#     title = forms.