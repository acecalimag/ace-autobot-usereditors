*** Variables ***

#       ****************** AUTH SECTION **************************
&{auth_alpha}
...                         username=b110
...                         password=kjt

#       ****************** AUTH SECTION **************************
&{auth_beta}
...                         username=wmaximoff
...                         password=kjt

#       ****************** AGENT DETAILS **************************
&{alpha_agent_details}
...                         username=b110
...                         fullname=B110
...                         position=General
...                         location=MNL
...                         startDate=
...                         workforceId=90004
...                         uid=16775553-51c6-4282-8080-306f7953b9df

#       ****************** END OF AGENT DETAILS **************************

#       ****************** CHECKBOX STATUS ******************************
&{alpha_checkbox_status}
...                         mgmt=Unchecked
...                         callback=Checked
...                         wonders=Unchecked
...                         coaching=Unchecked
...                         pullout=Unchecked
...                         sbs=Unchecked
...                         meeting=Unchecked
...                         restroom=Unchecked
...                         other=Unchecked
#       ****************** END OF CHECKBOX STATUS **************************


#       ********************** B110 AGENT **********************************
&{agent_alpha}
...                         auth=&{auth_alpha}
...                         agent_details=&{alpha_agent_details}
...                         checkbox_status=&{alpha_checkbox_status}

#       ********************** WMAXIMOFF AGENT **********************************
&{agent_beta}
...                         auth=&{auth_beta}
