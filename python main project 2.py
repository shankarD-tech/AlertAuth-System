import asyncio
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="alert"
    )
mycursor=mydb.cursor()
mycursor.execute("create database if not exists alert")
mycursor.execute("use alert")
mycursor.execute("create table if not exists data(email varchar(100),password varchar(10))")
sql = "insert into data(email,password) values(%s,%s)"
val=("shankardeva2004@gmail.com","12345678")
mycursor.execute(sql,val)
mycursor.execute("select * from alert.data")
l=mycursor.fetchall()
t=(l[0])
passcode=t[1]
password=input("login")
if(password==passcode):
    from telegram import Bot
    async def main():
        bot = Bot(token="8666657130:AAEO5DUJnt5vfD-paGHsgkI4ICrEZN3qRC8")
        import requests
        res = requests.get("https://ipinfo.io")
        a=(res.json())
        b=a["ip"]
        c=a["city"]
        d=a["region"]
        e=a["country"]
        f=a["loc"]
        g=a["org"]
        h=a["postal"]
        i=a["timezone"]
        j=a["readme"]
        await bot.send_message(chat_id="1242166619", text=f"ip={b}\ncity={c}\nregion={d}\ncountry={e}\nloc={f}\norg={g}\npostal={h}\ntimezone={i}\nreadme={j}\nyou were successfully logged in")
    asyncio.run(main())
else:
    from telegram import Bot
    async def main():
        bot = Bot(token="8666657130:AAEO5DUJnt5vfD-paGHsgkI4ICrEZN3qRC8")
        import requests
        res = requests.get("https://ipinfo.io")
        a=(res.json())
        b=a["ip"]
        c=a["city"]
        d=a["region"]
        e=a["country"]
        f=a["loc"]
        g=a["org"]
        h=a["postal"]
        i=a["timezone"]
        j=a["readme"]
        await bot.send_message(chat_id="1242166619", text=f"ip={b}\ncity={c}\nregion={d}\ncountry={e}\nloc={f}\norg={g}\npostal={h}\ntimezone={i}\nreadme={j}\nBe alert someone is trying to login your gmail")
        mycursor.execute("create table if not exists thirdparty(ip varchar(100),city varchar(100),region varchar(100),country varchar(100),loc varchar(100),org varchar(100),postal varchar(100),timezone varchar(100),readme varchar(100))")
        sql = "insert into thirdparty(ip,city,region,country,loc,org,postal,timezone,readme) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(f"{b}",f"{c}",f"{d}",f"{e}",f"{f}",f"{g}",f"{h}",f"{i}",f"{j}")
        mycursor.execute(sql,val)
asyncio.run(main())
    
'''import asyncio
from telegram import Bot

async def main():
    bot = Bot(token="8666657130:AAEO5DUJnt5vfD-paGHsgkI4ICrEZN3qRC8")
    await bot.send_message(chat_id="1242166619", text="Hello! It works 🎉")

asyncio.run(main())

import requests
res = requests.get("https://ipinfo.io")
a=(res.json())
print(a)'''




















