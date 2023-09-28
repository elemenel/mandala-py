#Templates and code snippets

# This is the most recent preamble for a mandala
global my_mandala_name
global my_project
global my_angle
global my_title
global str_angles
a.pick_angles()
a.i_angle = a.i_angle_auto
str_angles = [str(i) for i in (a.i_angle)]
Lg.logger.info(f'The value of str_angles is {str_angles}')
my_mandala_name = f'Fantastic Mandala with {str_angles}'
my_project = f'Reversing Awesome Mandala-{str_angles}-degrees angles-{Tm.project_time}' # Employing f-script
startup_script()
make_folder()
t.my_angles = str_angles
t.my_splash = f'{my_project} with {au.my_track}' 
for a.i  in range(len(a.i_angle)):
    my_angle = a.i_angle_auto[a.i]
    Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
    t.my_title = f'Fantastic Mandala: {my_angle:.2f} Degrees Angle and {au.my_track}'
    turtle.title(f'Fantastic Mandala: {my_angle:.2f} Angle with {au.my_track}')
    count = 0
