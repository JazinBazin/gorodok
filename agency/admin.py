from django.contrib import admin
from django import forms
from .models import \
    SocialNetwork, ProductCategory, \
    Advantage, AdvantageListItem, \
    Feedback, Contact, ContactPhone, \
    Apartment, ApartmentImage, \
    House, HouseImage, \
    Land, LandImage, \
    Garage, GarageImage, \
    Commercial, CommercialImage, \
    News, Partner, \
    Service, ServiceListItem, \
    AboutCompanyBlock, \
    Background, BackgroundData


class BackgroundDataInline(admin.TabularInline):
    model = BackgroundData
    extra = 1
    max_num = 1


class BackgroundAdmin(admin.ModelAdmin):
    inlines = [BackgroundDataInline]


class FeedbackAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.video_link:
            video_token = str(obj.video_link)[-11:]
            obj.video_link = 'https://www.youtube.com/embed/' + video_token
        obj.save()


class ServiceListItemInline(admin.TabularInline):
    model = ServiceListItem
    extra = 1


class SeviceAdmin(admin.ModelAdmin):
    inlines = [ServiceListItemInline]


class ContactPhoneInline(admin.TabularInline):
    model = ContactPhone
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactPhoneInline]


class AdvantageListItemInline(admin.TabularInline):
    model = AdvantageListItem
    extra = 1


class AdvantageAdmin(admin.ModelAdmin):
    inlines = [AdvantageListItemInline]


class RealEstateImageInLine(admin.TabularInline):
    class Meta:
        abstract = True

    extra = 0


class RealEstateForm(forms.ModelForm):
    class Meta:
        abstract = True
    exclude = []


class RealEstateAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    list_display = ('vendor_code', 'title_text', 'status', 'edit_date')
    search_fields = ['vendor_code']

    def get_queryset(self, request):
        queryset = super(RealEstateAdmin, self).get_queryset(
            request).order_by('-status', '-edit_date')
        return queryset

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('images_multiple'):
            obj.images.create(image=afile)


class ApartmentImageInline(RealEstateImageInLine):
    model = ApartmentImage


class ApartmentForm(RealEstateForm):
    model = Apartment


class ApartmentAdmin(RealEstateAdmin):
    form = ApartmentForm
    inlines = [ApartmentImageInline]


class HouseImageInline(RealEstateImageInLine):
    model = HouseImage


class HouseForm(RealEstateForm):
    model = House


class HouseAdmin(RealEstateAdmin):
    form = HouseForm
    inlines = [HouseImageInline]


class LandImageInline(RealEstateImageInLine):
    model = LandImage


class LandForm(RealEstateForm):
    model = Land


class LandAdmin(RealEstateAdmin):
    form = LandForm
    inlines = [LandImageInline]


class GarageImageInline(RealEstateImageInLine):
    model = GarageImage


class GarageForm(RealEstateForm):
    model = Garage


class GarageAdmin(RealEstateAdmin):
    form = GarageForm
    inlines = [GarageImageInline]


class CommercialImageInline(RealEstateImageInLine):
    model = CommercialImage


class CommercialForm(RealEstateForm):
    model = Commercial


class CommercialAdmin(RealEstateAdmin):
    form = CommercialForm
    inlines = [CommercialImageInline]


admin.site.register(SocialNetwork)
admin.site.register(ProductCategory)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(Garage, GarageAdmin)
admin.site.register(Commercial, CommercialAdmin)
admin.site.register(News)
admin.site.register(Partner)
admin.site.register(Service, SeviceAdmin)
admin.site.register(AboutCompanyBlock)
admin.site.register(Background, BackgroundAdmin)
