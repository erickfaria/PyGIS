
#Code to calculate area and perimeter of a set of coordinates in Python. Exercise done using a mif file


#Autor: Erick Faria

from math import sqrt

def get_next_region(file_handle):

    region = None
    for line in file_handle:
        if line.find('Region')!=-1:
            return line.strip()
    return None
        
def get_coords(file_handle):

    n_coords = int(file_handle.readline())

    return [[float(v) for v in file.readline().split()] for _ in range(n_coords)]

def calc_perimeter(coords):

    def distance(point1, point2):
        diffx = point1[0] - point2[0]
        diffy = point1[1] - point2[1]
        return sqrt(diffx*diffx + diffy*diffy)
    
    perimetro = sum(distance(point1, point2) for point1, point2 in zip(coords[1:], coords))
    perimetro += distance(coords[0], coords[-1])
       
    return perimetro/1000.0 

def calc_area(coords):

    def area(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return (x1*y2 - y1*x2)/2

    total_area = sum(area(point1, point2) for point1, point2 in zip(coords[1:], coords))
    total_area += area(coords[0], coords[-1])
    return total_area/1e6 


with open('file.mif', 'rt') as file:
    
    while True:
        region = get_next_region(file)
        if region:
            print(f'{region} - ', end = '')
            coords = get_coords(file)
            perimeter = calc_perimeter(coords)
            area = calc_area(coords)
            print(f'Perimetro em km: {perimeter:.4f}; Área em km²: {area:.4f}') 
        else:
            break