from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from datetime import datetime, timedelta
import os

# اطلاعات API شما
api_id = 26600960
api_hash = '73746434553a3b392291b51a49cd41fc'

async def update_time():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        print("✅ Connected to Telegram successfully!")
        
        error_count = 0
        while True:
            try:
                # زمان ایران (UTC+3:30)
                utc_time = datetime.utcnow()
                iran_time = utc_time + timedelta(hours=3, minutes=30)
                current_time = iran_time.strftime('%H:%M')
                
                # به روزرسانی نام پروفایل
                await client(UpdateProfileRequest(
                    first_name=current_time,
                    last_name=''
                ))
                print(f'✅ Updated to: {current_time} (Iran Time)')
                error_count = 0  # ریست شمارش خطا
                
            except Exception as e:
                error_count += 1
                print(f'❌ Error #{error_count}: {e}')
                
                if error_count >= 5:
                    print('🔄 Too many errors, waiting 5 minutes...')
                    await asyncio.sleep(300)  # 5 دقیقه انتظار
                else:
                    await asyncio.sleep(30)   # 30 ثانیه انتظار
                continue
            
            # انتظار 60 ثانیه
            await asyncio.sleep(60)

print("🟢 Starting Telegram Live Clock on Railway...")
asyncio.run(update_time())
