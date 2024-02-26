import gizeh as gz
import numpy as np
import moviepy.editor as mpy

w = w = 150
D = 2 # duration
nballs = 60

# Generate random values of radius, color, center
radii = np.random.randint(.1*w,.2*w, nballs)
colors = np.random.rand(nballs,3)
centers = np.random.randint(0,w, (nballs,2))

def make_frame(t):
    surface = gz.Surface(W,H)
    for r, color, center in zip(radii, colors, centers):
        angle = 2*np.pi*(t/D*np.sign(color[0]-.5)+color[1])
        xy = center+gz.polar2cart(W/5, angle) # center of ball
        gradient = gz.colorGradient(type = "radial",
                   stops_colors = [(0,color), (1,color/10)],
                   xy1 = [0.3, -0.3], xy2 = [0,0], xy3 = [0,1.4])
        ball = gz.circle(r=1, fill = gradient).scale(r).translate(xy)
        ball.draw(surface)
        return surface.get_npimage()
    
    clip = mpy.VideoClip(make_frame, duration=0)
    clip.write_gif("balls.gif", fps=15, opt="OptimizePlus")
                                                     