# pynput 테스트용 실험실
# 목표:
# 1. 키보드 입력을 raw 로그로 저장
# 2. ESC 입력 시 로그를 재구성
# 3. 문장 + 문장 시작 시간 형태로 출력

from pynput.keyboard import Key, Listener
from datetime import datetime
import re

LOG_FILE = 'key_logger/key_log.txt'
OUTPUT_FILE = 'key_logger/new_logs.txt'
KOR_TO_ENG = {
    "ㄱ":"r","ㄲ":"R","ㄴ":"s","ㄷ":"e","ㄸ":"E","ㄹ":"f","ㅁ":"a","ㅂ":"q","ㅃ":"Q",
    "ㅅ":"t","ㅆ":"T","ㅇ":"d","ㅈ":"w","ㅉ":"W","ㅊ":"c","ㅋ":"z","ㅌ":"x","ㅍ":"v","ㅎ":"g",
    "ㅏ":"k","ㅐ":"o","ㅑ":"i","ㅒ":"O","ㅓ":"j","ㅔ":"p","ㅕ":"u","ㅖ":"P",
    "ㅗ":"h","ㅘ":"hk","ㅙ":"ho","ㅚ":"hl","ㅛ":"y",
    "ㅜ":"n","ㅝ":"nj","ㅞ":"np","ㅟ":"nl","ㅠ":"b",
    "ㅡ":"m","ㅢ":"ml","ㅣ":"l"
}


def write_logs(message: str):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(message + "\n")


def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        ch = key.char
        if not ch:
            return
        if ch in KOR_TO_ENG:
            ch = KOR_TO_ENG[ch]
        log = f"[{timestamp}]: {ch}"
    except AttributeError:
        # space / enter / backspace
        log = f"[{timestamp}]: {key}"

    write_logs(log)


def on_release(key):
    if key == Key.esc:
        write_logs("=== ESC 입력으로 프로그램 종료 ===")
        reconstruct_logs()
        return False


def reconstruct_logs():
    buffer = []
    lines_out = []
    current_sentence_time = None
    skip_cmd_next = False

    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # 타임스탬프 추출
            time_match = re.search(
                r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]", line
            )
            timestamp = time_match.group(1) if time_match else None
            # Backspace
            if "Key.backspace" in line:
                if buffer:
                    buffer.pop()
                continue
            # Space
            if "Key.space" in line:
                if not buffer and timestamp:
                    current_sentence_time = timestamp
                buffer.append(" ")
                continue
            # Enter 입력 시 문장 확정
            if "Key.enter" in line:
                if buffer:
                    lines_out.append(
                        f"[{current_sentence_time}]: {''.join(buffer)}"
                    )
                    buffer = []
                    current_sentence_time = None
                continue
            if "Key.cmd" in line:
                skip_cmd_next = True
                continue
            # 상태 키 무시
            if any(k in line for k in ["Key.shift", "Key.caps_lock"]):
                continue
            # 실제 문자 추출
            match = re.search(r":\s(.+)$", line)
            if match:
                ch = match.group(1)
                if not ch.startswith("Key."):
                    if skip_next_char:
                        skip_next_char = False
                        continue
                    if not buffer and timestamp:
                        current_sentence_time = timestamp
                    buffer.append(ch)

    # 파일 끝났는데 buffer 남아 있으면 처리
    if buffer:
        lines_out.append(
            f"[{current_sentence_time}]: {''.join(buffer)}"
        )

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines_out))


if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# 안녕하세요 이은찬입니다.
# 파이썬 키보드 트래커 연습중입니다.

