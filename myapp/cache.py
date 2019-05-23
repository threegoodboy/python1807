from redis import Redis

rd=Redis(host='localhost',db=0)

def save_code(phone,code):
    rd.set(phone,code)
    rd.expire(phone,120)

def get_code(phone):
    if rd.exists(phone):
        return rd.get(phone)
    return None
