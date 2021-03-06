from django.contrib import admin
from nodeshot.contrib import dns


class BaseAdmin(admin.ModelAdmin):
    """
    Abstract administration model for BaseDate models.
        * 'added' and 'updated' fields are everytime readonly
        * save on top button is everytime present
    """
    save_on_top = True
    readonly_fields = ['added', 'updated']

    class Meta:
        abstract = True


class DomainAdmin(BaseAdmin):
    """
    Domain administration model
    """
    list_display = ['name', 'type']
    search_fields = ['name']



class RecordAdmin(BaseAdmin):
    """
    Record administration model
        * Is readonly because is generated by the plugin
    """
    list_display = ['name', 'type', 'content', 'ttl']
    list_filter = ('domain',)

    search_fields = ['name', 'content']

    readonly_fields = ['added', 'updated', 'domain', 'name', 'type', 'content', 'ttl', 'prio', 'change_date']


class DomainPolicyAdmin(BaseAdmin):
    list_display = ['name']
    list_filter = ('domain',)

    search_fields = ['name']    


class UserRecordAdmin(BaseAdmin):
    """
    User generated Record administration model   
    """
    list_display = ['name', 'domain', 'type', 'content']
    list_filter = ('domain',)

    search_fields = ['name', 'content']

    fieldsets = [
        ('record',   {'fields': ['name', 'domain', 'type', 'content'], 'classes': ['wide']}),
        (None,       {'fields': ['user']}),
    ]


admin.site.register(dns.models.Domain, DomainAdmin)
admin.site.register(dns.models.Record, RecordAdmin)
admin.site.register(dns.models.DomainPolicy, DomainPolicyAdmin)
admin.site.register(dns.models.UserRecord, UserRecordAdmin)
#admin.site.register(dns.models.DomainManager)


