from PIL import Image, ImageFilter


image = Image.open('/workspaces/multimedia-python/Gambar/IamMarvelJesus.jpg')
image.save('.././Gambar/hasil_MJ.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('.././Gambar/hasil_cropan_MarvelJesus.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save ('.././Gambar/resize_MJ.jpg')

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('.././Gambar/hasil_filter_MJ.jpg')

#! ini bagian musiknya MJ (Marvel Jesus)

from pydub import AudioSegment

audio = AudioSegment.from_file('/workspaces/multimedia-python/Audio/Deadpool_Intro.mp3')
audio.export('.././Audio/intronya_MJ.mp3', format='mp3')

clipped_audio= audio[:10000]
clipped_audio.export('.././Audio/klip_MJ.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('.././Audio/gabungan_MJ.mp3', format='mp3')

audio.export('.././Audio/MJ_Intro_but_WAV.wav', format='wav')

louder_audio = audio+10
louder_audio.export('.././Audio/MJ_tapiGede.mp3', format='mp3')