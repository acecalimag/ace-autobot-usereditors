*** Variables ***

#       ****************** AUTH SECTION **************************
&{auth_alpha}
...                         username=b110
...                         password=kjt

#       ****************** AUTH SECTION **************************
&{auth_beta}
...                         username=wmaximoff
...                         password=kjt

#       ****************** RESTAURANT DATA **************************
&{restaurant_alpha}
...                         restaurant_name=ASIAN BOWL ( R88207 )
...                         username=b110
...                         full_name=B110
...                         position=General
...                         call_skills=NW,CH,SP
...                         difficult_skills=1
...                         agent_rank=0
...                         client_rank=0
...                         uid=16775553-51c6-4282-8080-306f7953b9df
...                         rid=209ce5ef-e9d3-11e4-b5e5-80ee733c5b56



#       ********************** B110 AGENT **********************************
&{agent_alpha}
...                         auth=&{auth_alpha}

#       ********************** WMAXIMOFF AGENT *****************************
&{agent_beta}
...                         auth=&{auth_beta}

#       ********************** DATA ****************************************
&{data}
...                         restaurant_alpha=&{restaurant_alpha}