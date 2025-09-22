#fast rub : 1.6
from fast_rub import Client,filters
from fast_rub.type import Update
from httpx import AsyncClient as asyhttpx

bot = Client("rubino_downloader")

user_name_bot = "@rubino_downloader01_bot"

@bot.on_message(filters=filters.and_filter(filters.is_text(),filters.is_user()))
async def rubino_dow(msg:Update):
    print(msg)
    if msg.text.startswith("https://rubika.ir/post/"):
        await msg.reply("در حال جستجو ...")
        link_post = msg.text
        try:
            async with asyhttpx(timeout=15) as client:
                response = (await client.get(f"https://api.parssource.ir/rubino_downloader/?url={link_post}")).json()
        except:
            await msg.reply("خطا ! مجدد تلاش کنید !")
            return None
        if response["status"]:
            result = response["result"]
            await msg.reply_image(result["thumb"],"image.png",f"""پست روبینو پیدا شد ✅

کپشن پست : {result["caption"]}
تعداد کامنت ها : {int(result["comment"]):,}
تعداد دنبال کننده های صفحه : {int(result["follower_page"]):,}
تعداد لایک های پست : {int(result["like"]):,}
نام کاربری صفحه : @{result["page_username"]}
تعداد ویو های پست : {int(result["view"]):,}

در حال ارسال پست ...""")
            try:
                await msg.reply_video(result["url"],"video.mp4",f"پست با موفقیت دانلود شد ✅\n\nربات ما 🤖 : {user_name_bot}\nکانال های ما :\n@O_and_ONE_bot\n@DeepPars")
            except:
                await msg.reply_image(result["url"],"image.png",f"پست با موفقیت دانلود شد ✅\n\nربات ما 🤖 : {user_name_bot}\nکانال های ما :\n@O_and_ONE_bot\n@DeepPars")
        else:
            await msg.reply("پست موجود نیست ❌\nنمونه آدرس درست پست روبینو : https://rubika.ir/post/OcZKFCSYuk")
    else:
        await msg.reply("""درود 👋

خوش اومدی به ربات روبینو دانلودر 📥
برای دانلود پست روبینو کافیه لینک اونو واسم بفرستی :)""")


bot.run()
