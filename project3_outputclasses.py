
class STEPS:
    def generate(self, json_text: 'json') -> None:
        '''generates the STEPS output'''
        print('DIRECTIONS')
        for item in json_text['route']['legs']:
            for i in item['maneuvers']:
                print(i['narrative'])
        print(' ')

class TOTALDISTANCE:
    '''generates and prints the TOTALDISTANCE output'''
    def generate(self, json_text: 'json') -> None:
        distance = 0
        for item in json_text['route']['legs']:
            distance += round(item['distance'])
        print('Total Distance: ' + str(distance) + ' miles')
        print(' ')

class TOTALTIME:
    '''generatws and prints the TOTALTIME output'''
    def generate(self, json_text: 'json') -> None:
        time = 0
        for item in json_text['route']['legs']:
            time += round(item['time']/60)  
        print('Total Time: ' + str(time)+ ' minutes')
        print(' ')

class LATLONG:
    '''generates and prints the LATLONG output'''
    def generate(self, json_text: 'json') -> None:
        latlong = None
        lat = None
        long = None
        lat_direction = None
        long_direction = None
        print('LATLONGS')
        for item in json_text['route']['locations']:
            latlong = item['latLng']
            
            long = latlong['lng']
            lat = latlong['lat']
            if int(lat) > 0:
                lat_direction = 'N'
            else:
                lat_direction = 'S'
            if int(long) > 0:
                long_direction = 'E'
            else:
                long_direction = 'W'
            print('{:.2f}{} {:.2f}{}'.format((abs(lat)), str(lat_direction), (abs(long)), str(long_direction)))
        print(' ')

class ELEVATION:
    '''generates and prints the elevation in feet of each location'''
    def generate(self, json_text: 'json') -> None:
        print("ELEVATIONS")
        for item in json_text['elevationProfile']:
            height = item['height']
            print(int(height))
        print(' ')


def run_generators(outputs: ['output'], json_text, e_json_text):
    '''runs a list of output types and generates the print output'''
    for output in outputs:
        if type(output) == ELEVATION:
            output.generate(e_json_text)
        else:
            output.generate(json_text)


