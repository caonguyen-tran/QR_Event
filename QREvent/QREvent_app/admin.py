from django.urls import path
from django.contrib import admin
from django.template.response import TemplateResponse
from .models import User, Event, Report, Registration, CheckIn, NameTag, Email, SentMail


class AdminSite(admin.AdminSite):
    site_header = 'STATISTIC VIEW'

    def get_urls(self):
        return [
                   path('stats-views/', self.stats_view)
               ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': "Test"
        })

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'company_name', 'position')
    search_fields = ('first_name', 'last_name', 'phone_number', 'company_name')
    list_filter = ['id', 'first_name']


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'start_time', 'end_time')
    search_fields = ('name', 'location', 'start_time', 'end_time')
    list_filter = ['name', 'location', 'start_time', 'end_time']


class ReportAdmin(admin.ModelAdmin):
    list_display = ('total_registrations', 'total_check_in')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'qr_code', 'created_at', 'updated_at')

class CheckInAdmin(admin.ModelAdmin):
    list_display = ('check_in_time', 'device')

class NameTagAdmin(admin.ModelAdmin):
    list_display = ('status', 'created_at', 'updated_at')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'event')

class SentMailAdmin(admin.ModelAdmin):
    list_display = ('email', 'status', 'sent_at')


admin_site = AdminSite(name="QREvent")

admin_site.register(User, UserAdmin)
admin_site.register(Event, EventAdmin)
admin_site.register(Report, ReportAdmin)
admin_site.register(Registration, RegistrationAdmin)
admin_site.register(CheckIn, CheckInAdmin)
admin_site.register(NameTag, NameTagAdmin)
admin_site.register(Email, EmailAdmin)
admin_site.register(SentMail, SentMailAdmin)