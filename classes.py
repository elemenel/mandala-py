#Classes
# import My_template as t

# class ActivePens:
#     pass
# print(ActivePens)
# 
# lg = ActivePens
# print(ActivePens)

class MyMandala:
        
    def __init__(self):
        self.PenName = ' '
        self.ProjectAngle = 0
        self.PenDistance = 0
        self.ProjectTitle = ' '
        self.LoopCount = 0

fresh_mandala = MyMandala()
print(fresh_mandala.ProjectTitle)
print(fresh_mandala.ProjectAngle)

fresh_mandala.ProjectTitle = 'Brand New Mandala'
fresh_mandala.ProjectAngle = 144
print(fresh_mandala.ProjectTitle)
print(fresh_mandala.ProjectAngle)
print(f'{MyMandala}')



