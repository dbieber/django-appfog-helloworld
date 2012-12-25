from django.db import models

class BetaUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
    	return "%s: %s" % (self.name, self.email)