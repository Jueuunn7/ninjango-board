from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = "board"
        indexes = [models.Index(fields=['title'], name='single_index')]

    def __str__(self):
        return self.title