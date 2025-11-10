from django.db.models.signals import post_delete, pre_save
from django.dispatch.dispatcher import receiver

from .models import Produit, ImageProduit

@receiver(post_delete, sender=Produit)
def produit_image_post_delete(sender, instance, **kwargs):
    for image_obj in instance.images.all():
        if image_obj.image:
            image_obj.image.delete(False)

@receiver(post_delete, sender=ImageProduit)
def delete_image_file_on_image_produit_delete(sender, instance, **kwargs):
   
   # Supprime le fichier image du système de fichiers lorsque l'instance ImageProduit est supprimée.
  
    if instance.image:
        instance.image.delete(False)

@receiver(pre_save, sender=ImageProduit)
def delete_image_file_on_image_produit_update(sender, instance, **kwargs):
    
   # Supprime l'ancien fichier image du système de fichiers lorsque l'instance ImageProduit est mise à jour avec une nouvelle image.
    
    if not instance.pk:
        return  # L'instance est nouvelle, pas de suppression nécessaire

    try:
        old_instance = ImageProduit.objects.get(pk=instance.pk)
    except ImageProduit.DoesNotExist:
        return  # L'instance n'existe pas, pas de suppression nécessaire

    old_image = old_instance.image
    new_image = instance.image
    if old_image and old_image != new_image:
        old_image.delete(False)
