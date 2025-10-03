segundos = int(input ("Insira os segundos: "))
    
horas = segundos // 3600
minutos = (segundos % 3600) // 60

total_seg = segundos % 60

print(horas, "horas", minutos, "minutos", total_seg, "segundos")