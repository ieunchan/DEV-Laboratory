from datetime import datetime
import time

timer = 10
while timer != 0:
    now, when = datetime.now(),'18:00'
    home = datetime.strptime(when, '%H:%M')
    end_time = now.replace(hour=home.hour, minute=home.minute, second=home.second)
    remain = end_time - now
    total_sec = int(remain.total_seconds())
    remain_hour, remain_min, remain_sec = total_sec // 3600, (total_sec % 3600) // 60, total_sec % 60
    print(
        f"\n퇴근까지 남은 시간: "
        f"{remain_hour:02d}시간 "
        f"{remain_min:02d}분 "
        f"{remain_sec:02d}초 "
        f"(총 {total_sec}초)"
    )
    timer = total_sec
    time.sleep(1)