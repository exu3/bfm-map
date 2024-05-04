"""
main.py
"""

import folium


m = folium.Map(location=(44.469288, -73.215117),
               tiles="OpenStreetMap", zoom_start=16)


parking_markers = {
    "s_champlain_st": {"location": [44.471932, -73.216820],
                       "tooltip": "Parking",
                       "desc": "Street parking on South Champlain St."},
    "kilburn_lot": {"location": [44.471177, -73.215073],
                    "tooltip": "Parking",
                    "desc": "Kilburn Lot on the corner of Kilburn St. and Pine St. Do not park in 'tenant parking.'"},
    "maltex": {"location": [44.467378, -73.215969],
               "tooltip": "Parking",
               "desc": "Paid parking at the Maltex Building."},
    "howard_st": {"location": [44.467128, -73.214309],
                  "tooltip": "Parking",
                  "desc": "Street parking on Howard St."},
    "dealer_com": {"location": [44.46687407290227, -73.21448874842086],
                   "tooltip": "Parking",
                   "desc": "Parking in the Dealer.com north lot."},
    "btv_electric": {"location": [44.46373665090995, -73.21546543771963],
                     "tooltip": "Parking",
                     "desc": "Burlington Electric parking lot."},

    "btv_dpw": {"location": [44.46159968224294, -73.21482328691013],
                "tooltip": "Parking",
                "desc": "Burlington DPW parking lot."}
}

# find icons on https://getbootstrap.com/docs/3.3/components/
for k in parking_markers:
    folium.Marker(
        location=parking_markers[k]["location"],
        tooltip=parking_markers[k]["tooltip"],
        popup=parking_markers[k]["desc"],
        icon=folium.Icon(icon="map-marker", color="blue"),
    ).add_to(m)


folium.Marker(
    location=[44.469524480854666, -73.21545503014707],
    tooltip="Burlington Farmers Market",
    popup="Market entrance.",
    icon=folium.Icon(icon="apple", color="orange")
).add_to(m)


# docs directory for gh pages
m.save("./docs/index.html")
