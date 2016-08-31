=========
CHANGELOG
=========

0.3 (2016-08-31)
-----------------

* Intervention length field (readonly if geometry is line)
* Fix apparence bug if no rights to add treks and pois (fixes #713)
* Fix extremities snapping (fixes #718)
* Show information desk in trek detail page (fixes #719)
* Fix topology adjustments after path split (fixes #720)
* On edition show global line orientation instead of individual paths (fixes #679)
* Fix invalid topology if trek goes twice on same path (fixes #671)
* Overlapping is now more precise (fixes #710)
* Reworked trek print layout
* Fix topology building if paths are taken twice (fixes #722)
* Fix tiling offset with horizontal bboxes
* Fix display of POI layer by default on list (fixes #696)
* Fix translation of not validated paths (fixes #730)
* Fix error if topology is required and empty (fixes #745)
* Fix duplication of N-N relations on path split (fixes #738)
* Fix project map in detail page (fixes #734)
* Fix project listed deleted interventions (fixes #739)
* Fix project listed infrastructures through interventions (fixes #740)
* Fix saving intervention form on infrastructure
* Repair serializing of properties after upgrade of django-geojson (fixes #755)
* Added ``public_transport`` and ``advised_parking`` to trek JSON detail API (fixes #758)
* Repair land layers colors after upgrade of django-geojson
* Upgraded to django-geojson 2.0
* Upgraded to Django 1.5

:notes:

    Specify allowed host (server IP) in ``etc/settings.ini`` (*for example*):
    * ``host = 45.56.78.90``
    Empty object caches:
    * ``sudo /etc/init.d/memcached restart``
    * ``rm -rf ./var/cache/*``


0.2 (2016-08-06)
-----------------

* Add pretty trek duration in JSON
* Add information desk field in Trek (fixes #624)
