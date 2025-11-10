from multiprocessing.resource_tracker import register

from django.utils.html import format_html
from django.conf import settings
import Boutique_project
from .models import Promotion, Produit, Categorie, ImageProduit
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from .models import Categorie, Produit, Promotion, ImageProduit
# Register your models here.

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'RabaisPreview', 'date_debut', 'date_fin', 'actif', 'ProductsList')
    ordering = ['date_debut']
    search_fields = ('rabais', 'nom')
    list_filter = ['actif']

    def ProductsList(self, obj):
        """la liste des produits pour chaque promotion"""
        produits = obj.produit_set.all()[:3]
        produits_list = [
            format_html(
                '<span style="background-color:#cce5ff; padding:2px 6px; margin-right:5px; border-radius:4px;">{}</span>',
                p.nom
            ) for p in produits
        ]
        count = obj.produit_set.count()
        if count > 3:
            produits_list.append(format_html('<span style="color:gray;">... +{} autres</span>', count - 3))
        return format_html('{}', ''.join(produits_list))

    ProductsList.short_description = 'produits associés'

    def RabaisPreview(self, obj, *args, **kwargs):
        """Affiche les rabais en % ou en $ pour chaque promotion"""
        if obj.rabais is None:
            return "-"
        style = "green" if obj.actif else "red"
        if obj.rabais > 1:
            return format_html('<span style="color:{}; font-weight:bold;">${}</span>', style, obj.rabais)
        else:
            value = obj.rabais * 100
            return format_html('<span style="color:{}; font-weight:bold;">{:.2}%</span>', style, value)

    RabaisPreview.short_description = 'rabais appliqué'
    RabaisPreview.admin_order_field = 'rabais'
    
class ImageInLine(admin.TabularInline):
    model = ImageProduit
    extra = 1 
    fields = ('image_preview', 'image', 'noImage')
    readonly_fields = ('image_preview', 'noImage')    

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 60px; border-radius: 4px;" />', obj.image.url)
        return "(Aucune image)"

    image_preview.short_description = "Aperçu"

@admin.register(ImageProduit)
class ImageProduitAdmin(admin.ModelAdmin):
    list_display = ('image_preview','image', 'produit',)
    ordering = ('image',)
    readonly_fields = ('noImage',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 60px; border-radius: 4px;" />', obj.image.url)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    inlines = [ 
        ImageInLine, 
        ]
    list_display = ('nom_with_image', 'quantite_stock', 'categorie', 'view_promotions_link')
    ordering = ('nom',)

    def nom_with_image(self, obj):
        if not obj.pk:
            return "-"

        images = obj.images.all()

        main_image = images.filter(noImage=1).first() or images.first()
        if main_image:
            return format_html(
                '<span style="display:flex; align-items:center;">'
                '<img src="{}" style="max-width:32px; margin-right:6px;" />'
                '{}'
                '</span>',
                main_image.image.url,
                obj.nom,
            )
        else: 
            return obj.nom

    nom_with_image.short_description = "Nom Produit"
    nom_with_image.admin_order_field = 'Nom'

    def promotions_list(self, obj):
        if not obj.pk:
            return "-"

        promotions = obj.promotion.all()
        if not promotions:
            return "Aucune promotions"
        else:
            return format_html_join(
                mark_safe('<br>'),
                '<a href="{}">{}</a>',
                (
                    (
                        reverse("admin:Boutique_app_promotion_change", args=(pro.id,)),
                        f"{pro.id} - {pro.nom}"
                    )
                    for pro in promotions
                )
            )

    def view_promotions_link(self, obj):
        count = obj.promotions.count()
        if count == 0:
            return "Aucune promotion"
        url = (
            reverse("admin:Boutique_app_promotion_changelist")
            + f"?produit__id__exact={obj.id}"
        )
        return format_html('<a href="{}">Voir les promotions ({})</a>', url, count)

    view_promotions_link.short_description = "Promotions associées"
    
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('ImagePreview', 'nom',)
    search_fields = ('nom',)  
    readonly_fields = ('ImagePreview',) 
    fields = ('nom', 'image_url', 'ImagePreview')  # pour spécifier l'ordre des champs dans le formulaire

    def ImagePreview(self, obj):
        #Aperçu de l'image (liste + formulaire d'édition).
        if obj.image_url:
            try:
                return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image_url.url)
            except Exception:
                return "(Désolé il ya pas d’image)"
        return "(Désol il y'a pas d’image)"
    ImagePreview.short_description = "Aperçu"