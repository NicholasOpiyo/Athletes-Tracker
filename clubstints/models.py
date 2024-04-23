
from django.db import models

# Player profiles model

class PlayerProfiles(models.Model):
    player_name = models.CharField(max_length = 100)
    player_first_name = models.CharField(max_length = 100)
    player_last_name = models.CharField(max_length = 100)
    player_nationality = models.CharField(max_length = 100) 
    current_league = models.CharField(max_length = 100)
    current_club = models.CharField(max_length = 100)
    current_contract_start_date = models.DateField()
    
    class Meta:
        models.constraints = [models.UniqueConstraint(fields = ['player_name'], name = 'distinct_player')]

    def __str__(self):
        return self.player_name
