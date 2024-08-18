from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

video = VideoFileClip('../Video/Deadpool_Intro.mp4')

video.write_videofile('../Video/Deadpool_joget.mp4')

short_video = video.subclip(0, 10)
short_video.write_videofile('../Video/Short_DP.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('../Video/gabunganShort_dan_aslinya.mp4')

reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('../Video/MJ_tapi_reverse.mp4')

speed_up_video = short_video.fx(vfx.speedx, 2)
speed_up_video.write_videofile('../Video/DP_buutFastt.mp4')

# ? hasilnya ada di folder script