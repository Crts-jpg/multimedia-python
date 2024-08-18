
# !!! Audio Manipulation

from pydub import AudioSegment
from pydub.playback import play
    
def manipulate_audio(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        print('✅ Audio opened successfully')
        
        if len(audio) > 10000:
            clipped_audio = audio[:10000]
            clipped_audio.export(f'../Audio/klip_{output_path}', format='mp3')
            print('✅ Clipped audio successfully')
        else:
            raise ValueError('Audio terlalu pendek untuk dipotong 10 detik')
        
        combined_audio = audio + clipped_audio
        combined_audio.export(f'../Audio/gabungan_{output_path}', format='mp3')
        print('✅ Combined audio successfully')
        
        audio.export(f'../Audio/MJ_Intro_but_WAV.wav', format='wav')
        print('✅ Converted to WAV successfully')
        
        if audio.dBFS < -10:
            louder_audio = audio + 10
            louder_audio.export(f'../Audio/MJ_tapiGede_{output_path}', format='mp3')
            print('✅ Made audio louder successfully')
        else:
            raise ValueError('Audio terlalu kecil untuk meningkatkan volume')
            
        print('✅ Done!')
        play(louder_audio)
        
    except Exception as e:
        print(f'❌ Error: {e}')
        
if __name__ == '__main__':
    manipulate_audio('../Audio/Deadpool_Intro.mp3', 'Deadpool_Intro.mp3')