from django.db import models
from django.contrib.auth.models import User
from surveys.models import Survey


class AnswerNotification(models.Model):
    class Meta:
        verbose_name = 'Powiadomienie'
        verbose_name_plural = 'Powiadomienia'

    user = models.ForeignKey(User, verbose_name='Użytkownik', on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, verbose_name='Ankieta', on_delete=models.CASCADE)
    message = models.CharField(verbose_name='Wiadomość', max_length=200)
    read = models.BooleanField(verbose_name="Przeczytana", default=False)
