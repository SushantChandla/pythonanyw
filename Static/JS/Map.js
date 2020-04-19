function placeCircle(lat, log,State,District,Confirmed,Death) {




    map.on('load', function () {

        map.addSource(lat + "" + log + "", {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [lat, log]
                        },
                        "properties": {
                            "modelId": lat + log,
                            "description": '<strong>'+State +'('+District+')</strong><h6>Confirmed Cases</h6><p>'+Confirmed+'</p><h6>Death</h6><p>'+Death+'</p>'
                        }
                    }
                ]
            }
        });
        map.addLayer({
            "id": lat + "" + log + "",
            "source": lat + "" + log + "",
            "type": "circle",
            "paint": {
                "circle-radius": 10,
                "circle-color": "#FF0000",
                "circle-opacity": 0.5,
                "circle-stroke-width": 0,
            },
            "filter": ["==", "modelId", lat + log],
        });


        var popup = new mapboxgl.Popup({
            closeButton: false,
            closeOnClick: false
        });

        map.on('mouseenter',  lat + "" + log + "", function (e) {
            // Change the cursor style as a UI indicator.
            map.getCanvas().style.cursor = 'pointer';

            var coordinates = e.features[0].geometry.coordinates.slice();
            var description = e.features[0].properties.description;

            // Ensure that if the map is zoomed out such that multiple
            // copies of the feature are visible, the popup appears
            // over the copy being pointed to.
            while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
                coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
            }

            // Populate the popup and set its coordinates
            // based on the feature found.
            popup
                .setLngLat(coordinates)
                .setHTML(description)
                .addTo(map);
        });

        map.on('mouseleave',  lat + "" + log + "", function () {
            map.getCanvas().style.cursor = '';
            popup.remove();
        });
    });

    //     map.on('click', lat + "" + log + "", function (e) {
    //         var coordinates = e.features[0].geometry.coordinates.slice();
    //         var description = e.features[0].properties.description;

    //         // Ensure that if the map is zoomed out such that multiple
    //         // copies of the feature are visible, the popup appears
    //         // over the copy being pointed to.
    //         while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
    //             coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
    //         }

    //         new mapboxgl.Popup()
    //             .setLngLat(coordinates)
    //             .setHTML(description)
    //             .addTo(map);
    //     });

    //     // Change the cursor to a pointer when the mouse is over the places layer.
    //     map.on('mouseenter', lat + "" + log + "", function () {
    //         map.getCanvas().style.cursor = 'pointer';
    //     });

    //     // Change it back to a pointer when it leaves.
    //     map.on('mouseleave', lat + "" + log + "", function () {
    //         map.getCanvas().style.cursor = '';
    //     });
    // });
}