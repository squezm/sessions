from django.contrib import admin

from .models import Location, Msg_post, Board_choice_poll

model_list = [
    Location,
    Msg_post,
    Board_choice_poll
    ]

for model in model_list:
    admin.site.register(model)
