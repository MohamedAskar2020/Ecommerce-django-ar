from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils.translation import gettext_lazy as _
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

# Create your models here.


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField()
    details = models.ManyToManyField(Product, through='Order_details')
    is_finished = models.BooleanField()
    total = 0
    items_count = 0

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return 'User: ' + self.user.username + ' Order Id : ' + str(self.id)

    # def get_absolute_url(self):
    #     return reverse("Order_detail", kwargs={"pk": self.pk})

#=========================================================================


class Order_details(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(_('Price'), max_digits=6, decimal_places=2)
    quantity = models.IntegerField(_('Quantity'), )

    class Meta:

        ordering = ('-id',)
        verbose_name = _("Order_details")
        verbose_name_plural = _("Order_detailss")

    def __str__(self):
        return "User: " + self.order.user.username + ", product : " + self.product.name + ' Order Id : ' + str(self.id)

    # def get_absolute_url(self):
    #     return reverse("Order_details_detail", kwargs={"pk": self.pk})

#==============================================================================


class Payment(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment_address = models.CharField(_("Shipment Address"), max_length=150)
    shipment_phone = models.CharField(_(""), max_length=30)
    card_number = CardNumberField()
    expire = CardExpiryField()
    security_code = SecurityCodeField()

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return self.order

    # def get_absolute_url(self):
    #     return reverse("Payment_detail", kwargs={"pk": self.pk})
