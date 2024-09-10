# Meminta input dari pengguna
event_time_str = input("Masukkan waktu acara dalam format HH:MM:SS (GMT+2): ")
current_time_str = input("Masukkan waktu saat ini dalam format HH:MM:SS (GMT+7): ")

# Memisahkan input menjadi jam, menit, dan detik
event_hour, event_minute, event_second = map(int, event_time_str.split(':'))
current_hour, current_minute, current_second = map(int, current_time_str.split(':'))

# Menyesuaikan waktu acara dari GMT+2 ke GMT+7 dengan mengurangi 5 jam
event_hour_adjusted = event_hour - 5

# Menormalkan waktu jika hasilnya negatif
if event_hour_adjusted < 0:
    event_hour_adjusted += 24

# Menghitung selisih detik
diff_seconds = event_second - current_second
if diff_seconds < 0:
    diff_seconds += 60
    event_minute_adjusted = event_minute - 1
else:
    event_minute_adjusted = event_minute

# Menghitung selisih menit
diff_minutes = event_minute_adjusted - current_minute
if diff_minutes < 0:
    diff_minutes += 60
    event_hour_adjusted -= 1

# Menghitung selisih jam
diff_hours = event_hour_adjusted - current_hour
if diff_hours < 0:
    diff_hours += 24

# Cek apakah Ali sudah melewatkan acara
if event_hour_adjusted < current_hour or (event_hour_adjusted == current_hour and event_minute_adjusted < current_minute) or (event_hour_adjusted == current_hour and event_minute_adjusted == current_minute and event_second < current_second):
    print("See you on the next Pear Event!")
else:
    print(f"{diff_hours:02}:{diff_minutes:02}:{diff_seconds:02}")
