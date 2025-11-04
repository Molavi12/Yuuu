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
        
        # استفاده از session جدید
        async with TelegramClient('new_session', api_id, api_hash) as client:
            print("✅ Connected to Telegram successfully!")
            
            stickers = ["🏓🥇", "🏓🥈", "🏓🥉"]
            sticker_index = 0
            
            while True:
                try:
                    # زمان ایران
                    utc_time = datetime.utcnow()
                    iran_time = utc_time + timedelta(hours=3, minutes=30)
                    current_time = iran_time.strftime('%H:%M')
                    current_sticker = stickers[sticker_index]
                    
                    display_name = f"{current_time} {current_sticker}"
                    
                    print(f"🔄 Updating to: {display_name}")
                    
                    # به روزرسانی پروفایل
                    await client(UpdateProfileRequest(
                        first_name=display_name,
                        last_name=""
                    ))
                    
                    print(f'✅ Updated: {display_name}')
                    
                    # تغییر استیکر
                    sticker_index = (sticker_index + 1) % len(stickers)
                    
                    # انتظار ۲ دقیقه
                    await asyncio.sleep(120)
                    
                except Exception as e:
                    print(f'❌ Error: {e}')
                    await asyncio.sleep(120)
                    
    except Exception as e:
        print(f'🚨 Critical Error: {e}')
        # اگر session مشکل داشت، فایل session را پاک کن
        if os.path.exists('new_session.session'):
            os.remove('new_session.session')
            print("🗑️ Corrupted session file deleted")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(update_time())
