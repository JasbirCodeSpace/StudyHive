from django.contrib import admin
from dsa.models import question
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class DSAResource(resources.ModelResource):
    class Meta:
        model = question.Question
        exclude = ('Notes', 'Bookmark')


class DSAAdmin(ImportExportModelAdmin):
    resource_class = DSAResource


# Register your models here.
admin.site.register(question.Question, DSAAdmin)
admin.site.register(question.ListedQuestion)
