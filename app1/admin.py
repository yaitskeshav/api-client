from django.contrib import admin
from app1.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class BornesHorsRueDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['nNoBorne',"sTerrain","sNomRuePrincipale","sStatut","dtHeureDebutAP"]
    search_fields = ('nNoBorne', 'sTerrain')

admin.site.register(BornesHorsRueDB,BornesHorsRueDBAdmin)


class BornesSurRueDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['nNoBorne',"sStatut"]
    search_fields = ('nNoBorne', 'nNoBorne')

admin.site.register(BornesSurRueDB,BornesSurRueDBAdmin)




class DateExportationDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['dDate']
    search_fields = ('dDate',)

admin.site.register(DateExportationDB,DateExportationDBAdmin)



class EmplacementReglementationBDAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['sNoEmplacement',"sCodeAutocollant"]
    search_fields = ('sNoEmplacement', 'sCodeAutocollant')

admin.site.register(EmplacementReglementationBD,EmplacementReglementationBDAdmin)



class PeriodesDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['nID',"dtHeureDebut"]
    search_fields = ('nID', 'dtHeureDebut')

admin.site.register(PeriodesDB,PeriodesDBAdmin)



class PlacesDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # list_display=['sNoPlace',"nLongitude"]
    # search_fields = ('nNoBorne', 'sTerrain')
    pass
admin.site.register(PlacesDB,PlacesDBAdmin)



class ReglementationPeriodeDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['sCode',"noPeriode"]
    # search_fields = ('nNoBorne', 'sTerrain')

admin.site.register(ReglementationPeriodeDB,ReglementationPeriodeDBAdmin)



class ReglementationsDBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['Name',"Type"]
    # search_fields = ('nNoBorne', 'sTerrain')

admin.site.register(ReglementationsDB,ReglementationsDBAdmin)





