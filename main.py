from record_voice import record
from audio_play import play
from ifly_t2a import text_to_audio
from ifly_a2t import audio_to_text,clear_text

file = 'user_voice.wav'           # 语音录制，识别文件
synth_file = "generated_voice.mp3"    # 语音合成文件 

record(file)                # 录制音频 
txt_str = audio_to_text(file)               # 语音识别
print(txt_str)                              # 打印识别结果

ret = text_to_audio(synth_file,txt_str)    # 语音合成
if ret == 1:
    play(synth_file)                        # 播放合成结果
    clear_text()                            # 清空识别结果