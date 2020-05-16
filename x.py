from moviepy.editor import *

video = VideoFileClip("xx.mp4")

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('bottom')
             .set_duration(3) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.mp4",fps=25)