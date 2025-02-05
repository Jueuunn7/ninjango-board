from django.db import models

from board.domain.models import Board


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=300)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.board.title