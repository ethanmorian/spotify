from datetime import datetime, timedelta

now_utc = datetime.utcnow()
now_kst = now_utc + timedelta(hours=9)
print(now_kst.strftime('%Y-%m-%d'))