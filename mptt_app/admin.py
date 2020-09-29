from django.contrib import admin
from mptt_app.models import FilingCabinet
from mptt.admin import DraggableMPTTAdmin


admin.site.register(FilingCabinet, DraggableMPTTAdmin)




