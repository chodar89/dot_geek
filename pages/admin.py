from django.contrib import admin

from .models import IndexCarousel

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'paragraph', 'first')
    list_editable = ('first',)
    list_display_links = ('id', 'heading')

admin.site.register(IndexCarousel, CarouselAdmin)
