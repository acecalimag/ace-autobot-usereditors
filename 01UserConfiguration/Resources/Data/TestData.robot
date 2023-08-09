*** Variables ***

#       ****************** AUTH SECTION *********************************
&{auth}
...                         username=wmaximoff
...                         password=kjt

#       ****************** DELIVERY INFO SECTION **************************


#       ****************** DELIVERY INFO SECTION END *********************

#       ********************** AMBER'S GARDEN ****************************
&{restaurant_1}
...                         editor=Restaurant Editor
...                         auth=&{auth}
...                         rnumber=R987652
...                         primary=&{primary_details}
...                         address=&{address_details}
...                         contact=&{contact_details}
...                         order=&{order_details}
...                         delivery=&{delivery_details}