
from django.contrib import admin
from django.conf.urls import include
from .models import CapitalPortfolio,ClientPortfolio
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import  User
from accs.models import Profile


class ProfileInline(admin.StackedInline):
    model =  Profile
    can_delete =  False
    verbose_name =  "Profile"
    fk_name =  'user'
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.site_title = ugettext_lazy('Rockstone capital')
admin.site.site_header = ugettext_lazy('Dashboard')
admin.site.index_title = ugettext_lazy('capital')


@admin.register(ClientPortfolio)
class ClientsPortfolioAdmin(admin.ModelAdmin):
    list_display = ('date','name','principalAmount','currentBalance','lastBalance','performance','roi','fee')
    # list_editable = ('investmentAmount','marketOpening','marketClosing')
    search_fields = ['name__username']


@admin.register(CapitalPortfolio)
class RCPortfolioAdmin(admin.ModelAdmin):
    list_display = ('date','principal_amount','open_amount','closing_amount','ROI','performance','profit')
    list_editable = ('open_amount', 'closing_amount')

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)