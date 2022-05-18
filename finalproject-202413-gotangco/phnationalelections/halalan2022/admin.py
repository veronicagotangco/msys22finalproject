from django.contrib import admin
from .models import Position
from .models import Candidate
from .models import Users
from .models import Vote

# Register your models here.
admin.site.register(Position)
admin.site.register(Candidate)
admin.site.register(Users)
admin.site.register(Vote)