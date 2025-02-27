def make_car(fabricante, modelo,**car_info):
    """Para crear un automovil"""
    car_info['fabricante']=fabricante
    car_info['modelo']=modelo
    return car_info