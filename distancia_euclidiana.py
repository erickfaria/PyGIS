from math import cos, sin, acos 
rad = 3.14159/180.0 
bh = [-20.,-45.] 
cidade = ['Buenos_Aires', 'Paris', 'Montreal', 'Tokio', 'Sydney', 'New_York', 'Cape_Town'] 
lat = [-34.6,49.,45.,36.,-33.,40.,-33.] 
lon =[-58.4,4.,-72.,140.,151.,-74.,18.5] 

aaa = 0 
bbb = 0
for i in range(0,len(cidade)): 
    ccc = (sin(bh[0]*rad) * sin(lat[i]*rad)) + (cos(bh[0]*rad) * cos(lat[i]*rad) * cos((bh[1] - lon[i])*rad))
    arco = acos(ccc)/rad 
    eee = 111*arco
    print ('A distancia entre Belo Horizonte e', cidade[i], 'e de', eee, 'km', '(', arco, 'graus)') 
    if eee > aaa: 
        aaa = eee 
        bbb = i
    print ('\nA cidade mais distante de Belo Horizonte e', cidade[bbb], 'com', aaa, 'km')