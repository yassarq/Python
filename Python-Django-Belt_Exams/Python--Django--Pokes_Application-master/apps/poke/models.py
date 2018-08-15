from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=False, max_length=20, null=True)
	last_name = models.TextField(blank=False, max_length=20,null=True)
	email = models.TextField(blank=False, max_length=20,null=True)
	description = models.TextField(blank=False, max_length=500,null=True)
	password = models.TextField(blank=False, max_length=20,null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'user'

class Poke(models.Model):
	poker = models.ForeignKey(User, related_name="pokerpokes")
	poked = models.ForeignKey(User, related_name="pokedpokes")
	created_at = models.DateField(null=True)
	counter = models.IntegerField(blank=False, default=0, null=True)
	total = models.IntegerField(blank=False, default=0, null=True)
	class Meta:
		db_table = 'poke'