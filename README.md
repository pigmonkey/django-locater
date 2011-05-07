Django Locater
==============

Django Locater is an experiment in geolocation.

A database is populated with locations. The user enters his location and a search radius. He is given a list of locations within his search criteria, sorted by distance. The locations are both plotted on a Google Map and printed as an ordered list.


Installation
------------
1.  Put the `locater` directory somewhere in your Python path (like inside your Django project folder).
2.  Add `locater` to your `settings.INSTALLED_APPS`.


Requirements
------------
*   [geopy](https://code.google.com/p/geopy/) does all the heavy lifting.


Feedback
---------

If you use Django Locator, I'd be interested to hear any feedback you might have. [Contact me via email](mailto:pm@pig-monkey.com).

A Word to the Wise
-------------------
This code is just a proof-of-concept. It has never been used in a production environment. So, in the words of Mystikal, "Watch youself!" (Further advice: "Shake ya ass. Show me watch you're working with.")
