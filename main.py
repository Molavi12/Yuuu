from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from datetime import datetime, timedelta
import os
import base64

# اطلاعات API شما
api_id = 26600960
api_hash = '73746434553a3b392291b51a49cd41fc'

# کد base64 فایل session که در GitHub آپلود کردید
SESSION_BASE64 = """
PASTE_THE_BASE64_CODE_HERE
"""

async def update_time():
    try:
        print("🟢 Starting Telegram Live Clock...")
        
        # ایجاد فایل session از base64 اگر وجود ندارد
        if not os.path.exists('session_name.session'):
            print("📦 Creating session file from base64...")
            
            if SESSION_BASE64.strip() == "PASTE_THE_BASE64_CODE_HERE" or not SESSION_BASE64.strip():
                print("❌ Please replace SESSION_BASE64 with your actual base64 code")
                return
            
            try:
                # حذف spaces و newlines از کد base64
                clean_base64 = SESSION_BASE64.strip().replace('\n', '').replace(' ', '')
                
                # decode base64 و ایجاد فایل session
                session_data = base64.b64decode(clean_base64)
                
                with open('session_name.session', 'wb') as f:
                    f.write(session_data)
                
                file_size = os.path.getsize('session_name.session')
                print(f"✅ Session file created! Size: {file_size} bytes")
                
            except Exception as decode_error:
                print(f"❌ Error decoding base64: {decode_error}")
                print("📋 Please check if the base64 code is complete and correct")
                return
        
        # بررسی وجود فایل session
        if os.path.exists('session_name.session'):
            file_size = os.path.getsize('session_name.session')
            print(f"📁 Using session file, Size: {file_size} bytes")
        else:
            print("❌ Session file not found after creation attempt")
            return
        
        async with TelegramClient('session_name', api_id, api_hash) as client:
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
                    
                    await asyncio.sleep(60)
                    
                except Exception as e:
                    print(f'❌ Error: {e}')
                    await asyncio.sleep(60)
                    
    except Exception as e:
        print(f'🚨 Critical Error: {e}')

if __name__ == "__main__":
    asyncio.run(update_time())
