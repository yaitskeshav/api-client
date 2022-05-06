from django.contrib import admin
from app1.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BornesHorsRueDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['nNoBorne',"sTerrain","sNomRuePrincipale","sStatut","dtHeureDebutAP"]
    search_fields = ('nNoBorne', 'sTerrain')

admin.site.register(BornesHorsRueDB,BornesHorsRueDBAdmin)