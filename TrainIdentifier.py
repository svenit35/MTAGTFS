#Converting Route_ID to a train name and direction tuple.
#Well route_ID is legit just the name "A", then search the trip_id for "N" or "S" for north or southbound
#but it's more fun to call them manhattan bound or brooklyn bound...

#takes a trip_update.trip and outputs a touple of ("train name", "direction") for example ("A", "Brooklyn bound") for a southbound A train.
def name_and_direction(trip_update_trip):
    if "S" in trip_update_trip.trip_id:
        return (trip_update_trip.route_id, "Brooklyn bound")
    else:
        return (trip_update_trip.route_id, "Manhattan bound")
