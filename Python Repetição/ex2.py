i = 600
while (i>=0):
    minutos = i // 60
    segundos = i % 60
    print(f"{minutos}:{segundos:02d}")
    i = i - 1
