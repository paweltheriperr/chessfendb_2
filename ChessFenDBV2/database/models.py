from django.db import models


class Fen(models.Model):
    position_id = models.IntegerField(null=False, blank=True)
    fen = models.TextField(blank=True, null=False)
    user = models.CharField(max_length=50, null=False, blank=True)

    added = models.DateTimeField(null=False)

    class Meta:
        verbose_name = 'Fen'
        verbose_name_plural = 'Fen\'s'
        ordering = ['pk', 'position_id']  # Sort by `id` then `position_id`

    def __str__(self):
        return f'<Fen: {self.fen}>'
