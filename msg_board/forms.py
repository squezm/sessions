from django import forms
from django.forms import ModelForm
from msg_board.models import Msg_post, Board_choice_poll
from django.contrib.auth.models import User

TIME_CHOICES = (
    ('Dawn Patrol', 'Dawn Patrol'),
    ('Sunrise', 'Sunrise'),
    ('Morning', 'Morning'),
    ('Lunch Break', 'Lunch Break'),
    ('Afternoon', 'Afternoon'),
    ('Sunset', 'Sunset'),
    ('After Dark', 'After Dark'),
    ('Full Moon', 'Full Moon')
    )
QUALITY_CHOICES = (
    ('Poor', 'Poor'),
    ('Poor+', 'Poor+'),
    ('Poor to Fair', 'Poor to Fair'),
    ('Fair', 'Fair'),
    ('Fair+', 'Fair+'),
    ('Fair to Good', 'Fair to Good'),
    ('Good', 'Good'),
    ('Good+', 'Good+'),
    ('Good to Epic', 'Good to Epic'),
    ('Epic', 'Epic')
    )
SIZE_CHOICES = (
    ('Flat', 'Flat'),
    ('Ankle High', 'Ankle high'),
    ('Knee High', 'Knee high'),
    ('Stomach High', 'Stomach high'),
    ('Chest High', 'Chest high'),
    ('Shoulder High', 'Shoulder high'),
    ('Head High', 'Head high'),
    ('Overhead', 'Overhead'),
    ('Head+1/2', 'Head and a half'),
    ('Double Overhead', 'Double overhead'),
    ('Massive', 'Massive')
    )
BOARD_CHOICES = (
    ('Longboard', 'Longboard'),
    ('Shortboard', 'Shortboard'),
    ('Funboard', 'Funboard'),
    ('Wavestorm', 'Wavestorm'),
    ('Fish', 'Fish'),
    ('Retro', 'Retro'),
    ('Experimental', 'Experimental')
    )

class Msg_boardForm(ModelForm):
    time_of_day = forms.CharField(
        widget=forms.Select(choices=TIME_CHOICES)
        )
    quality = forms.CharField(
        widget=forms.Select(choices=QUALITY_CHOICES)
        )
    size = forms.CharField(
        widget=forms.Select(choices=SIZE_CHOICES)
        )
    comment = forms.CharField(widget=forms.Textarea, strip=True)

    class Meta:
        model = Msg_post
        fields = [
            'time_of_day',
            'quality',
            'size',
            'comment'
        ]


class Board_choice_pollForm(ModelForm):
    board_choice = forms.CharField(
        widget=forms.RadioSelect(choices=BOARD_CHOICES)
        )
    
    class Meta:
        model = Board_choice_poll
        fields = [
            'board_choice'
        ]


class LoginForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'username'}
            )
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password'}
            )
        )

    class Meta:
        model = User
        fields = [
            'username',
            'password'
            ]


class AccountForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'username'}
            )
        )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'email'}
            )
        )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password'}
            )
        )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
            ]
