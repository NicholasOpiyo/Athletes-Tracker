from django.shortcuts import render


from clubstints.models import PlayerProfiles

def player_club_stint(request):
    #paths to images
    
    image_paths = []
    profiled_players = list(PlayerProfiles.objects.all())
    player_initial_name = [player.player_first_name for player in profiled_players]
    player_other_name = [player.player_last_name for player in profiled_players]
    for g, l in zip(player_initial_name, player_other_name):
        if g == 'mbala' or g == 'nicholas':
           path_to_image = "clubStints/images/" + g + "_" + l + ".png"
        else:
            path_to_image = "clubStints/images/" + g + "_" + l + ".jpg"
        image_paths.append(str(path_to_image))  
    
    #dictionaries of records

    player_records = []
    combined_player_records = {}
    record_count = len(profiled_players)
    
    for r in range(record_count):
        player_profile = {}
        player_profile['player_name'] = profiled_players[r].player_name
        player_profile['player_nationality'] = profiled_players[r].player_nationality
        player_profile['current_league'] = profiled_players[r].current_league
        player_profile['current_club'] = profiled_players[r].current_club
        player_profile['current_contract_date'] = profiled_players[r].current_contract_start_date
        player_profile['image_location'] = image_paths[r]
        player_records.append(player_profile)
        combined_player_records[profiled_players[r].player_first_name] = player_records[r]

    return render(request, 'clubstints/clubstints.html', {'combined_player_records': combined_player_records})

