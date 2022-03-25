# w33schoool dz
"получає дані, красіво виводить, всьо до джойнов, |гіт до бренч(веток) віртуалка лінукс|, получить названія полей класа і валідувати"
"своя база даних"



class Pilot():

    def __init__(self, name:str, position:str, age:int, salary:int, working_time:(float,int)):
        if isinstance(name,str) and isinstance(position,str) and isinstance(age,int) and \
                isinstance(salary,int) and isinstance(working_time,(int,float)):
            self.name = name
            self.age = age
            self.position = position
            self.salary = salary
            self.working_time = working_time

        else:
            raise ValueError

    def names(self):
        pass


    def values(self):
        return self.name, self.position, self.age, self.salary, self.working_time,

    def __dir__(self):
        return (self.name, self.position, self.age, self.salary, self.working_time)

    @staticmethod
    def make_info():
        # получаем инфу с клавы для инициализации
        name, position, \
        age, selery, working_time = input("name:"),input("position"), \
                                    int(input("age:")), int(input("salary:")), int(input("working_time:"))
        return name, position, age, selery, working_time

    def __repr__(self):
        return f"name:{self.name},age:{self.age}, position:{self.position}, salary:{self.salary}" \
               f", hours:{self.working_time}"

# initialization_data = Pilot.make_info()
# obj = Pilot(*initialization_data)
# print(obj.__dict__.keys())






# class Army():
#     def __init__(self, army_name,location, pilot: pilot):
#         self.army_name = army_name
#         self.pilot = pilot
#         self.location = location
#
#     def print_smth(self):
#         print(self.pilot.values())
#
#     @staticmethod
#     def make_info():
#         # получаем инфу с клавы для инициализации
#         army_name, location= input("army_name:"), input("location:")
#         return army_name, location
#
#     def __repr__(self):
#         return f"Army: {self.army_name}, WORKER {pilot.repr(self.pilot)} LOCATION: {self.location}"

# info=Army.make_info()
# x=Army(*info,obj)
# print(x)



