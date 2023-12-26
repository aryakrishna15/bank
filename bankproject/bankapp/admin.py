from django.contrib import admin
from .models import Registration, Branch, Personnal, District, Material

admin.site.register(Material)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(Registration, RegisterAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(District, DistrictAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'wikipedia_link']


admin.site.register(Branch, BranchAdmin)


class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phonenumber', 'mailid', 'address', 'district', 'branch',
                    'AccountType', 'materials_provide1', 'materials_provide2', 'materials_provide3']
    list_editable = ['AccountType', 'materials_provide1', 'materials_provide2', 'materials_provide3']

    list_per_page = 20


admin.site.register(Personnal, PersonalAdmin)
