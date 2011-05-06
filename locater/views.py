from django.shortcuts import render_to_response
from django.template import RequestContext
from locater.models import Location
from locater.forms import SearchForm
from geopy import geocoders
from geopy import distance

def find_nearest(request):
    errors = []
    if request.method == 'POST':
        form = SearchForm(request.POST)

        # If the form is valid, clean the data
        if form.is_valid():
            cd = form.cleaned_data
            g = geocoders.Google()
            search = ''

            # Get the radius and geocode the user's search location
            radius = int(cd['radius'])
            try:
                search = g.geocode(cd['search'])
            except:
                errors.append("I could not find that location! Try another search.")

            if search:
                # Get all locations
                locations = Location.objects.all()

                # Create an empty list that will hold the nearest locations
                nearest_locations = []

                # Find the distance between each location and the user's search
                # If the distance is less than the search radius, add it to the list
                for location in locations:
                    d = distance.distance(search[1], location.latlong).miles
                    if d <= radius:
                        nearest_locations.append((d, location))


                if nearest_locations:
                    # Sort the nearest locations by distance
                    # By default, the sort method will sort by the first item in the tuple
                    nearest_locations.sort()

                    # Create an empty list to hold the resulting, sorted data to pass back to the user
                    results = []

                    for nearest_location in nearest_locations:
                        results.append({
                            'name': nearest_location[1].name,
                            'url': nearest_location[1].url,
                            'phone': nearest_location[1].phone,
                            'street_address': nearest_location[1].street_address,
                            'city': nearest_location[1].city,
                            'state': nearest_location[1].state,
                            'zip': nearest_location[1].zip,
                            'distance': int(nearest_location[0]),
                            'lat': nearest_location[1].latlong[0],
                            'long': nearest_location[1].latlong[1],
                        })

                    return render_to_response('locater/results.html',
                        {'locations': results,
                        'search': search[0],
                        'radius': radius,
                        'lat': search[1][0],
                        'long': search[1][1],
                        'form': form}, context_instance=RequestContext(request))

                # If no locations met the search criteria, return an error
                else:
                    errors.append("Whoops, there does not appear to be any results for %s! Try entering a different location, or changing the search radius." % (search[0]))

    else:
        form = SearchForm()

    return render_to_response('locater/search.html', {'form': form, 'errors': errors}, context_instance=RequestContext(request))
