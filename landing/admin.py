from django.contrib import admin


from landing.models import Site, OldageHome, Patient, Illness, Donation, Doctor, Staff

admin.site.register(Site)
admin.site.register(OldageHome)
admin.site.register(Patient)
admin.site.register(Illness)
admin.site.register(Donation)
admin.site.register(Doctor)
admin.site.register(Staff)
