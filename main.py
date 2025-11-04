from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from datetime import datetime, timedelta
import os
import sys

# اطلاعات API شما
api_id = 26600960
api_hash = '73746434553a3b392291b51a49cd41fc'

async def update_time():
    try:
        print("🟢 Starting Telegram Live Clock with Rotating Stickers...")
        
        async with TelegramClient('session_name', api_id, api_hash) as client:
            print("✅ Connected to Telegram successfully!")
            
            # لیست استیکرها به ترتیب چرخش
            stickers = ["🏓🥇", "🏓🥈", "🏓🥉"]
            sticker_index = 0
            
            # شمارنده برای ردیابی
            update_count = 0
            
            while True:
                try:
                    # زمان ایران (UTC+3:30)
                    utc_time = datetime.utcnow()
                    iran_time = utc_time + timedelta(hours=3, minutes=30)
                    current_time = iran_time.strftime('%H:%M')
                    
                    # انتخاب استیکر فعلی
                    current_sticker = stickers[sticker_index]
                    
                    # به روزرسانی نام پروفایل
                    await client(UpdateProfileRequest(
                        first_name=current_time,
                        last_name=current_sticker
                    ))
                    
                    update_count += 1
                    print(f'✅ #{update_count} Updated to: {current_time} {current_sticker}')
                    
                    # تغییر به استیکر بعدی برای دفعه بعد
                    sticker_index = (sticker_index + 1) % len(stickers)
                    
                    # انتظار ۶۰ ثانیه (همزمان با تغییر زمان)
                    await asyncio.sleep(60)
                    
                except Exception as e:
                    print(f'❌ Error: {e}')
                    await asyncio.sleep(60)  # در صورت خطا هم ۶۰ ثانیه صبر کن
                    
    except Exception as e:
        print(f'🚨 Critical Error: {e}')
        sys.exit(1)

# اجرای برنامه
if __name__ == "__main__":
    asyncio.run(update_time())
