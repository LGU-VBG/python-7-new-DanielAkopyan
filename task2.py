def update_car_info(**kwargs):
    car=kwargs
    car['is_available']=True
    return car

result=update_car_info(marka='BMW',cena=5000000)

print(result)