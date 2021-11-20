from django.db import models


# Create your models here.

class Question(models.Model):

    DIFFICULTY = (
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    )
    topic = models.CharField(max_length=50, null=False)
    problem = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)
    difficulty = models.CharField(choices=DIFFICULTY, max_length=1, null=True)
    url = models.URLField(null=False, blank=False)
    done = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Request."""
        return f"Question [{self.problem}]"


class ListedQuestion(models.Model):
    date = models.DateField(auto_now_add=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True, unique=True)

    class Meta:
        """Meta definition for ListedQuestion."""

        verbose_name = 'ListedQuestion'
        verbose_name_plural = 'ListedQuestions'

    def __str__(self):
        """Unicode representation of ListedQuestion."""
        return f"ListedQuestion [{self.question}]"