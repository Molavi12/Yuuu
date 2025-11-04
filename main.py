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
        print("🟢 Starting Telegram Live Clock...")
        print("📁 Checking session file...")
        
        # بررسی وجود فایل session
        if not os.path.exists('session_name.session'):
            print("❌ Session file not found!")
            print("📂 Files in directory:")
            for file in os.listdir('.'):
                print(f"   - {file}")
            return
        
        print("✅ Session file found")
        
        async with TelegramClient('session_name', api_id, api_hash) as client:
            print("✅ Connected to Telegram successfully!")
            
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
                    
                    await asyncio.sleep(60)
                    
                except Exception as e:
                    print(f'❌ Update Error: {e}')
                    await asyncio.sleep(30)
                    
    except Exception as e:
        print(f'🚨 Critical Error: {e}')
        sys.exit(1)

# اجرای برنامه
if __name__ == "__main__":
    asyncio.run(update_time())
