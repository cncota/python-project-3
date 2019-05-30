
from project3_API import *
from project3_outputclasses import *


def main_program():
    '''runs the main module, input is taken and gives different outputs for the given locations'''
    try:
        locations_num = int(input())
        locations_list = []
        outputs = []
        for one in range(locations_num):
           locations_list.append(input())
        output_num = int(input())
        for one in range(output_num):
            outputs.append((input()))
        print(' ')
        outputs_methods = []
        for i in outputs:
            if i == 'STEPS':
                outputs_methods.append(STEPS())
            elif i == 'TOTALDISTANCE':
                outputs_methods.append(TOTALDISTANCE())
            elif i == 'TOTALTIME':
                outputs_methods.append(TOTALTIME())
            elif i == 'LATLONG':
                outputs_methods.append(LATLONG())
            elif i == 'ELEVATION':
                outputs_methods.append(ELEVATION())
               
        json_text = HTTP_request(build_directions_url(locations_list))

        for message in json_text['info']['messages']:
            if message == "We are unable to route with the given locations.":
                raise SyntaxError
            elif message == "Unable to calculate route.":
                raise SyntaxError
            else:
                pass

        
        latlon_list = []
        for item in json_text['route']['locations']:
            latlon_list.append(item['latLng']['lat'])
            latlon_list.append(item['latLng']['lng'])
        e_j_text = HTTP_request(build_elevation_url(latlon_list))
        run_generators(outputs_methods, json_text, e_j_text)
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    except SyntaxError:
        print('NO ROUTE FOUND')
     
    except:
        print('MAPQUEST ERROR')
        
        
if __name__ == '__main__':
    main_program()

