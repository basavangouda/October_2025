import datetime

def generate_email():
    now=datetime.datetime.now()
    print(now)
    time_stamp=(now.strftime("%Y-%m-%d %H:%M:%S").replace("-","_")
                .replace(":","_").replace(" ","_"))
    print(time_stamp)
    return "basava"+time_stamp+"@gmail.com"

print(generate_email())