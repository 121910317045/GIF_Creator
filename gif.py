from moviepy.editor import *

clip = (VideoFileClip("Oh my Kadavule.mkv")
        .subclip((1,14.65),(1,20.2))
        .resize(0.5))
clip.write_gif("gif_output.gif")