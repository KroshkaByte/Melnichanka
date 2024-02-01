from .models import LogisticsAuto


def get_dep_choices():
    return LogisticsAuto.objects.order_by().values_list("departure_city", "departure_city").distinct()



def get_dest_choices():
    return LogisticsAuto.objects.order_by().values_list("destination_city", "destination_city").distinct()


def get_all_choices():
    return [(trip.id, trip) for trip in LogisticsAuto.objects.all()]
