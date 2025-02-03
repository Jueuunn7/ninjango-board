from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "board"

    def __str__(self):
        return self.name