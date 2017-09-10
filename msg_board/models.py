from datetime import datetime
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        if ' ' in self.name:
            print(
                "Name contains whitespace."
                "Rename this location using the _ character instead of the space character, and then delete the location with the whitespace."
                )
        return self.name.replace("_", " ")


class Msg_post(models.Model):
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        max_length=30
        )
    time_of_day = models.CharField(max_length=30)
    quality = models.CharField(max_length=15)
    size = models.CharField(max_length=15)
    #image = models.ImageField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment

class Board_choice_poll(models.Model):
    board_choice = models.CharField(max_length=30)

    def __str__(self):
        return self.board_choice
