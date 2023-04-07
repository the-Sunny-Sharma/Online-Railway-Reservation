from django.contrib import admin
from myapp.models import Register,Chart,BookTicket,Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(BookTicket)
admin.site.register(Register)
admin.site.register(Chart)