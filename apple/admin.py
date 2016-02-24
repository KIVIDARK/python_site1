from django.contrib import admin

from apple.models import dept, workers

admin.AdminSite.site_header = 'Заголовок админки'


class WorkersInline(admin.TabularInline):
    model = workers
    extra = 3


class DeptAdmin(admin.ModelAdmin):
    inlines = [WorkersInline]


class WorkersAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['dept']}),
        ('Информация о работнике', {'fields': ['name', 'birthday', 'boss'], 'classes': ['collapse']}),
    ]

    list_display = ('name', 'dept', 'birthday')
    search_fields = ['name']


admin.site.register(dept, DeptAdmin)

admin.site.register(workers, WorkersAdmin)