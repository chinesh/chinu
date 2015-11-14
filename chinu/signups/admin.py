

from django.contrib import admin
# Create your models here.

from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp

admin.site.register(SignUp,SignUpAdmin)
