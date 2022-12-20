from datetime import datetime

def get_time():

    now = datetime.now()
    time_now = ("São {} horas e {} minutos".format(now.hour, now.minute))
    return time_now

def get_date():

    now = datetime.now()
    date_now = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime("%B"), now.year)
    return date_now