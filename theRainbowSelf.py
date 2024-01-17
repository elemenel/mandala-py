import master_mandala_maker_production as Mm
import turtle


# ***********************************************************************************
# The Rainbow Self
# +++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def the_rainbow_self():
    #     global my_angle
    #     Lg.logger.info('Selecting Angle from Input Box')
    #     select_angle()
    #     Lg.logger.info('Current Angle to be Drawn is ' + str(my_angle))
    Mm.my_mandala_name = "The Rainbow Self"
    Mm.Lg.logger.info("Selecting track from runtime-generated list")
    Mm.au.pick_custom_length_track()
    global my_project
    global log
    Mm.my_project = "The Rainbow Self v." + Mm.Tm.project_time
    Mm.startup_script()
    Mm.Lg.logger.info("Located @ line 5860 - 6215, 49th module of 49")
    Mm.make_folder()
    Mm.Lg.logger.info(
        "The soundtrack being used for this show is:   " + str(Mm.au.my_track)
    )
    Mm.turtle.bgcolor(7, 7, 5)
    my_range = 24
    my_length = 200
    my_pensize = 0.5
    my_speed = 0
    Mm.t.my_angle = 59

    def crown_chakra():
        # 1
        el = turtle.Turtle()
        el.shape("blank")
        el.pencolor(255, 255, 250)
        el.speed(my_speed)
        el.pensize(my_pensize)
        el.penup()
        el.setpos(0, 300)
        el.pendown()
        for i in range(my_range * 2):
            el.left(Mm.t.my_angle)
            el.fd(my_length)
            Mm.f.save_thumb()
            el.setpos(0, 300)
            Mm.f.save_thumb()
            el.left(Mm.t.my_angle)
            el.fd(my_length / 6)
            Mm.f.save_thumb()

    def third_eye():
        # 2
        ed = turtle.Turtle()
        ed.shape("blank")
        ed.pencolor("indigo")
        ed.speed(my_speed)
        ed.pensize(my_pensize * 2)
        ed.penup()
        ed.setpos(0, 200)
        ed.pendown()

        for i in range(my_range * 2):
            ed.left(Mm.t.my_angle)
            ed.fd(my_length)
            Mm.f.save_thumb()
            ed.setpos(0, 200)
            Mm.f.save_thumb()
            ed.left(Mm.t.my_angle)
            ed.fd(my_length / 6)
            Mm.f.save_thumb()

    def throat_chakra():
        # 3
        ef = turtle.Turtle()
        ef.shape("blank")
        ef.pencolor(0, 255, 255)
        ef.speed(my_speed)
        ef.pensize(my_pensize)
        ef.penup()
        ef.setpos(0, 100)
        ef.pendown()

        for i in range(my_range * 2):
            ef.left(Mm.t.my_angle)
            ef.fd(my_length)
            Mm.f.save_thumb()
            ef.setpos(0, 100)
            Mm.f.save_thumb()
            ef.left(Mm.t.my_angle)
            ef.fd(my_length / 6)
            Mm.f.save_thumb()

    def heart_chakra():
        # 4
        eg = turtle.Turtle()
        eg.shape("blank")
        eg.pencolor(0, 255, 0)
        eg.speed(my_speed)
        eg.pensize(my_pensize)
        eg.penup()
        eg.setpos(0, 0)
        eg.pendown()

        for i in range(my_range * 2):
            eg.left(Mm.t.my_angle)
            eg.fd(my_length)
            Mm.f.save_thumb()
            eg.setpos(0, 0)
            Mm.f.save_thumb()
            eg.left(Mm.t.my_angle)
            eg.fd(my_length / 6)
            Mm.f.save_thumb()

    def solar_plexus_chakra():
        # 5
        ee = turtle.Turtle()
        ee.shape("blank")
        ee.pencolor(255, 255, 0)
        ee.speed(my_speed)
        ee.pensize(my_pensize)
        ee.penup()
        ee.setpos(0, -100)
        ee.pendown()

        for i in range(my_range * 2):
            ee.left(Mm.t.my_angle)
            ee.fd(my_length)
            Mm.f.save_thumb()
            ee.setpos(0, -100)
            Mm.f.save_thumb()
            ee.left(Mm.t.my_angle)
            ee.fd(my_length / 6)
            Mm.f.save_thumb()

    def seat_of_soul_chakra():
        # 6
        ei = turtle.Turtle()
        ei.shape("blank")
        ei.pencolor("orange")
        ei.speed(my_speed)
        ei.pensize(my_pensize)
        ei.penup()
        ei.setpos(0, -200)
        ei.pendown()

        for i in range(my_range * 2):
            ei.left(Mm.t.my_angle)
            ei.fd(my_length)
            Mm.f.save_thumb()
            ei.setpos(0, -200)
            Mm.f.save_thumb()
            ei.left(Mm.t.my_angle)
            ei.fd(my_length / 6)
            Mm.f.save_thumb()

    def sacral_chakra():
        # 7
        ej = turtle.Turtle()
        ej.shape("blank")
        ej.pencolor(255, 0, 0)
        ej.speed(my_speed)
        ej.pensize(my_pensize * 2)
        ej.penup()
        ej.setpos(0, -300)
        ej.pendown()

        for i in range(my_range * 2):
            ej.left(Mm.t.my_angle)
            ej.fd(my_length)
            Mm.f.save_thumb()
            ej.setpos(0, -300)
            Mm.f.save_thumb()
            ej.left(Mm.t.my_angle)
            ej.fd(my_length / 6)
            Mm.f.save_thumb()

    #  my_chakras = [sacral_chakra(), seat_of_soul_chakra(), solar_plexus_chakra(), heart_chakra(), throat_chakra(), third_eye(), crown_chakra()]

    def play_chakras():
        global my_range
        #         global Mm.t.my_angle
        global my_length
        for count in range(6):
            if count == 0:
                print(str(count))
                Mm.t.my_angle = 40
                my_range = 9
                my_length = 30
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 1:
                Mm.t.my_angle = 30
                my_range = 12
                my_length = 60
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 2:
                Mm.t.my_angle = 20
                my_range = 18
                my_length = 90
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 3:
                Mm.t.my_angle = 10
                my_range = 36
                my_length = 120
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 4:
                Mm.t.my_angle = 5
                my_range = 72
                my_length = 70
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 5:
                Mm.t.my_angle = 4
                my_range = 90
                my_length = 150
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 6:
                Mm.t.my_angle = 2
                my_range = 180
                my_length = 180
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            else:
                Mm.t.my_angle = 1
                my_range = 360
                my_length = 200
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()

    play_chakras()
    Mm.stage_reverse_video()
    Mm.finalize()


the_rainbow_self()
