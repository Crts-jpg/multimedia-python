# from PIL import Image, ImageFilter


# image = Image.open('../Gambar/IamMarvelJesus.jpg')
# image.save('../Gambar/hasil_MJ.jpg')

# cropped_image = image.crop((10, 10, 200, 200))
# cropped_image.save('.././Gambar/hasil_cropan_MarvelJesus.jpg')

# resized_image = cropped_image.resize((100, 100))
# resized_image.save ('.././Gambar/resize_MJ.jpg')

# filtered_image = resized_image.filter(ImageFilter.BLUR)
# filtered_image.save('.././Gambar/hasil_filter_MJ.jpg')

# #! ini bagian musiknya MJ (Marvel Jesus)

# from pydub import AudioSegment

# audio = AudioSegment.from_file('../Audio/Deadpool_Intro.mp3')
# audio.export('.././Audio/intronya_MJ.mp3', format='mp3')

# clipped_audio= audio[:10000]
# clipped_audio.export('.././Audio/klip_MJ.mp3', format='mp3')

# combined_audio = audio + clipped_audio
# combined_audio.export('.././Audio/gabungan_MJ.mp3', format='mp3')

# audio.export('.././Audio/MJ_Intro_but_WAV.wav', format='wav')

# louder_audio = audio+10
# louder_audio.export('.././Audio/MJ_tapiGede.mp3', format='mp3')






# !!! Task 1

from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input_path, output_path):
    try:
        image = Image.open(input_path)
        print('✅ Image opened successfully')
        
        if image.width > 200 and image.height > 200:
            cropped_image = image.crop((10, 10, 200, 200))
            cropped_image.save(f'../Gambar/cropped_{output_path}')
            print('✅ Cropped image successfully')
        else:
            raise ValueError('Gambar terlalu kecil untuk di-crop ke ukuran 200x200')
        
        resized_image = cropped_image.resize((100, 100), Image.Resampling.LANCZOS)
        resized_image.save(f'../Gambar/resized_{output_path}')
        print('✅ Resized image successfully')
        
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        filtered_image.save(f'../Gambar/filtered_{output_path}')
        print('✅ Filtered image successfully')
        
        enhancer = ImageEnhance.Brightness(filtered_image)
        bright_image = enhancer.enhance(1.5)
        bright_image.save(f'../Gambar/bright_{output_path}')
        print('✅ Brightened image successfully')
        
        combined_image = Image.blend(resized_image, bright_image, alpha=0.5)
        combined_image.save(f'../Gambar/combined_{output_path}')
        print('✅ Combined image successfully')
        
    except Exception as e:
        print(f'❌ Error: {e}')
            
if __name__ == '__main__':
    manipulate_image('../Gambar/IamMarvelJesus.jpg', 'MarvelJesus.jpg')