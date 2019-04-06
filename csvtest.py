import csv
from django.http import HttpResponse


def csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'age', 'height', 'weight'])
    writer.writerow(['zhiliao', '18', '180', '110'])
    return response
