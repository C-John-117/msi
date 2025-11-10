from django.db import models
from django.db.models.deletion import PROTECT

class Categorie(models.Model):
    nom = models.CharField(max_length=50, blank=False, verbose_name='Nom')
    image_url = models.ImageField(
        verbose_name='Image catégorie',
        max_length=255,
        default='categories/default.jpg',
        upload_to='categories/'
    )

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.nom

class Promotion(models.Model):
    actif = models.BooleanField(default=False, verbose_name='Est active')
    nom = models.CharField(max_length=50, blank=False, verbose_name='Nom')
    rabais = models.DecimalField( max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Rabais')
    date_debut = models.DateTimeField(blank=False, verbose_name='Début')
    date_fin = models.DateTimeField(blank=False, verbose_name='Fin')

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100, blank=False, verbose_name='Nom de produit')
    #pour empecher la suppression dune categorie sil est lié à un produit 
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name='produits', verbose_name='Catégorie')
    quantite_stock = models.IntegerField(default=5, blank=False, verbose_name='Quantité en stock')
    #categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits', verbose_name='Catégorie')
    promotions = models.ManyToManyField(Promotion, blank=True, verbose_name='Promotions')

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.nom

class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='images', verbose_name='Produit')
    image = models.ImageField(
        upload_to='produits/',
        verbose_name='Image du produit'
    )
    noImage = models.IntegerField(default=1, blank=False)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['noImage']

   #Pour que le numéro incérmente automatiquement
    def save(self, *args, **kwargs):
        if not self.pk and (self.noImage == 1 or self.noImage is None):
            last_image = (
                ImageProduit.objects
                .filter(produit=self.produit)
                .order_by('-noImage')
                .first()
            )
            self.noImage = (last_image.noImage + 1) if last_image else 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image de {self.produit.nom}"
