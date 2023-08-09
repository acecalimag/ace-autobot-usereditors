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
...                         Restaurant Name=xpath:(//th[@role='columnheader'])[2]
...                         Auto Assign=xpath:(//th[@role='columnheader'])[3]
...                         Tenure Required=xpath:(//th[@role='columnheader'])[4]
...                         SP=xpath:(//th[@role='columnheader'])[5]
...                         CH=xpath:(//th[@role='columnheader'])[6]
...                         NW=xpath:(//th[@role='columnheader'])[7]
...                         MGR=xpath:(//th[@role='columnheader'])[8]
...                         PO=xpath:(//th[@role='columnheader'])[9]
...                         SME=xpath:(//th[@role='columnheader'])[10]
...                         CA=xpath:(//th[@role='columnheader'])[11]
...                         CL=xpath:(//th[@role='columnheader'])[12]
...                         TIER 3=xpath:(//th[@role='columnheader'])[13]

&{expected_restaurant_alpha_checkbox_status}
...                         Auto Assign=Unchecked
...                         SP=Unchecked
...                         CH=Unchecked
...                         NW=Unchecked
...                         MGR=Unchecked
...                         PO=Unchecked
...                         SME=Unchecked
...                         CA=Unchecked
...                         CL=Unchecked
...                         Tier 3=Unchecked

&{actual_restaurant_alpha_checkbox_status}
...                         Auto Assign=xpath:(//input[contains(@type,'checkbox')])[1]
...                         SP=xpath:(//input[contains(@type,'checkbox')])[2]
...                         CH=xpath:(//input[contains(@type,'checkbox')])[3]
...                         NW=xpath:(//input[contains(@type,'checkbox')])[4]
...                         MGR=xpath:(//input[contains(@type,'checkbox')])[5]
...                         PO=xpath:(//input[contains(@type,'checkbox')])[6]
...                         SME=xpath:(//input[contains(@type,'checkbox')])[7]
...                         CA=xpath:(//input[contains(@type,'checkbox')])[8]
...                         CL=xpath:(//input[contains(@type,'checkbox')])[9]
...                         TIER 3=xpath:(//input[contains(@type,'checkbox')])[10]

&{expected_test_restaurant_value}
...                         Restaurant Name=ASIAN BOWL (R88207)
...                         Tenure Required=${EMPTY}

&{others}
...                         restaurant_name_no_RID=ASIAN BOWL

#       ********************** B110 AGENT **********************************
&{agent_alpha}
...                         auth=&{auth_alpha}

#       ********************** WMAXIMOFF AGENT *****************************
&{agent_beta}
...                         auth=&{auth_beta}

#       ********************** DATA ****************************************
&{data}
...                         restaurant_alpha=&{restaurant_alpha}
...                         common=&{others}
...                         expected_checkbox=&{expected_restaurant_alpha_checkbox_status}
...                         actual_checkbox=&{actual_restaurant_alpha_checkbox_status}
...                         value=&{expected_test_restaurant_value}