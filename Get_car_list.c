import os
import csv


class CarBase: 												# основной класс

    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext (self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase): 									

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        lst_str = body_whl.split('x')
        if len(lst_str) != 3:
            length, width, height = 0.0, 0.0, 0.0
        else:
            try:
                length = float(lst_str[0])
                width = float(lst_str[1])
                height = float(lst_str[2])
            except:
                length, width, height = 0.0, 0.0, 0.0

        self.body_length = length
        self.body_width = width
        self.body_height = height
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


												 # car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra


def get_car_list(csvfile):
    car_list = []
    common_ext = ['.png', '.jpeg', '.jpg', '.gif']
    with open(csvfile) as rfile:
        for lin in rfile.readlines()[1:]:
            lst_atr_str = lin.split(';')

            car_type = lst_atr_str[0]
            brand = lst_atr_str[1]

           											 # car == car_type;brand;passenger_seats_count;photo_file_name;***;carrying;***
          											 # truck == car_type;brand;***;photo_file_name;body_whl;carrying;***
         											 # spec_machine = car_type;brand;***;photo_file_name;***;carrying;extra
												 # *** = optional param 

            if car_type != '' and len(lst_atr_str) >= 6:

                passenger = lst_atr_str[2]
                ph = lst_atr_str[3]
                whl = lst_atr_str[4]
                carrying = lst_atr_str[5]
                try:
                    extra = lst_atr_str[6].strip()
                except:
                    extra = ''
                if car_type == 'spec_machine' and len(lst_atr_str) == 7:
                    pass
                elif car_type =='spec_machine':
                    carrying = lst_atr_str[4]
                    extra = lst_atr_str[5].split()

                ph_check = os.path.splitext(ph)[1] in common_ext    # needed for all

                passenger_check = passenger.isdigit()
                carrying_check = True
                try:
                    l = float(carrying)
                except:
                    carrying_check = False
                extra_check = extra != '' and extra !='\n'
                if ph_check and brand and carrying_check:  					 # если все проверки пройдены, то создаем соответствующий класс
                    if car_type == 'car' and passenger_check and not extra_check and not whl:
                        car_list.append(Car(brand, ph, carrying, passenger))
                    if car_type == 'truck'and not passenger_check and not extra_check:
                        car_list.append(Truck(brand, ph, carrying, whl))
                    if car_type == 'spec_machine' and extra_check and not passenger_check and not whl:
                        car_list.append(SpecMachine(brand, ph, carrying, extra))
    return car_list
# print(get_car_list('C:/virtual/coursera_week3_cars.csv'))