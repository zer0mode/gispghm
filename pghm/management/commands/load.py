# coding=utf-8
import os
import json

from .models import Webcam

DATA_FILE = os.path.join(os.path.dirname(pghm.__file__),'data/webcam2.geojson')


# def run(verbose=True):
# with open(DATA_FILE) as data_file:
#     data = json.load(data_file)
#     for record in data:
#         Webcam.objects.create(

#             station = record['station'],
#             site = record['site'],
#             img = record['img'],
#             nom = record['nom'],
#             lat = record['lat'],
#             lon = record['lon'],
#             yaw = record['yaw'],
#             geom = models.PointField('longitude/latitude', blank=True, null=True)


#             first_name=record['first_name'],
#             last_name=record['last_name'],
#             gender=record['gender'],
#             email=record['email'],
#             ip_address=record['ip_address'])
#         print(record)