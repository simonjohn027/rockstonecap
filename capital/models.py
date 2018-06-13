from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import  DecimalException


class ClientPortfolio(models.Model):
    """This is the client portfolio this is dealing with the user's data and information"""
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    date = models.DateTimeField(auto_now=True)

    principalAmount = models.DecimalField(decimal_places=2,
                                          max_digits=12,
                                          default=1)
    lastBalance = models.DecimalField(decimal_places=2,
                                      max_digits=12,
                                      default=1)
    currentBalance = models.DecimalField(decimal_places=2,
                                         max_digits=12,
                                         default=principalAmount)

    def __str__(self):
        return  self.name.username;

    #This is growth since the begin of time
    # so it express the changes in platform since the begin of time
    def growth(self):
        diff = self.currentBalance - self.principalAmount
        try:
            perf = round((diff / self.principalAmount) * 100, 2)
        except ZeroDivisionError:
            return 0

        return perf

    #Current performance of the portfolio
    def performance(self):
        diff = self.currentBalance - self.lastBalance
        try:
            perf = (diff / self.lastBalance)
        except (ZeroDivisionError,DecimalException):
            return 0
        return  round(perf*100,2)

    #Excess amount since the first Investment
    def roi(self):
       return  round((self.growth()/100) * self.principalAmount,2)

    def fee(self):
        return  round(0.2 * (float)(self.roi()),2)





class CapitalPortfolio(models.Model):
    """ This is for the portfolio management where the admin will be able to put the initial money they invested in
    a particular market and the in the night the will be able to indicate the new amount they had at the begin.
    """
    date = models.DateField(auto_now =True)
    principal_amount = models.DecimalField(verbose_name="Principal",decimal_places=2, max_digits=12,default=1)
    open_amount = models.DecimalField(verbose_name='Opening Amount', decimal_places=2, max_digits=12,default=1)
    closing_amount = models.DecimalField(verbose_name='Closing Amount', decimal_places=2, max_digits=12,default=0)

    def ROI(self):
        return self.closing_amount - self.open_amount

    def performance(self):

        diff = self.closing_amount - self.open_amount
        try:
            perf = round((diff / self.open_amount) * 100, 2)
        except ZeroDivisionError:
            return 0

        return perf

    def profit(self):

        return 0.2 * (float)(self.ROI());



@receiver(post_save,sender=CapitalPortfolio)
def updateCurrentBalance(sender,created,**kwargs):
    clients = ClientPortfolio.objects.all()
    lens = len(CapitalPortfolio.objects.all())
    capital = CapitalPortfolio.objects.all().reverse()[lens-1]
    print(capital.performance())
    perf = capital.performance()
    for client in clients:
        client.lastBalance = client.currentBalance
        if (client.currentBalance == 0):
            client.currentBalance = 1
        else:
            client.currentBalance += (client.currentBalance*perf/100)
        client.save()