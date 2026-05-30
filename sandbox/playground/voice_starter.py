from datetime import timedelta
import sounddevice as sd
from datetime import datetime
import numpy as np

SAMPLE_RATE = 16000
BLOCK_SIZE = 1600

print('마이크 테스트 시작')
print('말하면 음성이 출력')
print('ctrl + c 누르면 종료')

def sound_callback(indata, frames, time, status):
    if status:
        print(status)
    current_volume = np.linalg.norm(indata)
    if current_volume > 1:
        print(f'음성 감지됨. 볼륨:: {current_volume:.2f}')
        print(f'현재시각: {datetime.now()}')

try:
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        blocksize=BLOCK_SIZE,
        callback=sound_callback,
    ):
        while True:
            sd.sleep(100)
except KeyboardInterrupt:
    print("\n프로그램 종료")