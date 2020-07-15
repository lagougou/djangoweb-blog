from django.contrib import admin

# Register your models here.
from .models import AlbumInfo
from account.models import MyUser


@admin.register(AlbumInfo)
class AlbumInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'introduce', 'photo']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user_id = request.user.id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            id = request.user.id
            kwargs['queryset'] = MyUser.objects.filter(id=id)
        return super().formfield_for_foreignkey(db_field, request, **kwags)

        