from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Product(models.Model):

    prdName = models.CharField(max_length=100, verbose_name=_("Product Name"))
    prdCat = models.ForeignKey('Category', on_delete=models.CASCADE,
                               blank=True, null=True, verbose_name=_('Category'))
    # prdBrd = models.ForeignKey('settings.Brand', on_delete=models.CASCADE,
    #                            blank=True, null=True, verbose_name=_('product brand'))
    prdDesc = models.TextField(verbose_name=_("Description"))
    prdMainImage = models.ImageField(
        upload_to='product\images\item', blank=True, null=True, verbose_name=_("Image"))
    prdPrice = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name=_("Price"))
    prdDiscountPrice = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, verbose_name=_("Discount Price"))

    prdCost = models.DecimalField(
        max_digits=6, decimal_places=3, verbose_name=_("Cost"))
    prdCreated = models.DateTimeField(verbose_name=_("Created Date"), auto_now_add=True)

    prdSlug = models.SlugField(
        blank=True, null=True, verbose_name=_("Product Url"))
    prdIsNew = models.BooleanField(default=True, verbose_name=_("New Product"))
    prdIsBestSeller = models.BooleanField(
        default=False, verbose_name=_("Best Seller"))

    def save(self, *args, **kwargs):
        if not self.prdSlug:
            self.prdSlug = slugify(self.prdName)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-prdCreated',)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"slug": self.prdSlug})

    def __str__(self):
        return self.prdName
# ====================================================


class ProductImage(models.Model):

    prdIProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product"))
    prdImage = models.ImageField(
        upload_to='product\images\item', verbose_name=_("Image"))

    def __str__(self):
        return str(self.prdIProduct)
# =====================================================


class Category(models.Model):

    catName = models.CharField(max_length=50, verbose_name=_('name'))
    catParent = models.ForeignKey(
        'self', limit_choices_to={'catParent__isnull': True}, verbose_name=_('main category'), on_delete=models.CASCADE, blank=True, null=True)
    catDesc = models.TextField(verbose_name=_('description'))
    catImg = models.ImageField(
        upload_to='product\images\category', verbose_name=_('Image'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.catName)

#==========================================================


class Product_Alternative(models.Model):

    prdAltProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=_('product'))
    prdAlternatives = models.ManyToManyField(
        Product, related_name='alternative_products', verbose_name=_('Alternatives'))

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.prdAltProduct)

#===============================================================


class Product_Accessories(models.Model):
    prdAccProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='main_acc_product', verbose_name=_('product'))
    prdAccessory = models.ManyToManyField(
        Product, related_name='accessory_products', verbose_name=_('Accessories'))

    class Meta:
        verbose_name = _("Product_Accessory")
        verbose_name_plural = _("Product_Accessories")

    def __str__(self):
        return str(self.prdAccProduct)
