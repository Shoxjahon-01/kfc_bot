import logging
from knopka import bosh_menu,ichimliklar_menu,twister_menu,pitsa_menu,burger_menu,shirinlik_menu

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6201008607:AAEotr9XXvU9ABJOED7ITZaPc4-AOQuO6tw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("welcome to kfc ", reply_markup=bosh_menu)
    await message.answer_photo('https://s.yimg.com/ny/api/res/1.2/Qdb.gpME8XFgRqsKzGokUg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MA--/https://s.yimg.com/os/creatr-uploaded-images/2023-02/bc798840-a81e-11ed-8b87-ceb4d61b21db')

# ichimliklar bo'limini boshi

@dp.message_handler(text="🍹Ichimliklar")
async def echo(message: types.Message):
    await message.answer_photo("https://zamin.uz/uploads/posts/2022-08/220808091235.jpg")
    await message.answer("Ichimliklar bo'limi",reply_markup=ichimliklar_menu)

@dp.message_handler(text='🥤Fanta')
async def echo(message: types.Message):
    await message.answer_photo("https://olcha.uz/image/600x600/products/2023-01-17/gazirovannyy-napitok-fanta-orange-05-l-190963-0.jpg")
    await message.answer('''
    fanta:0,5 litr
    narxi:9000 so'm
    ''')



@dp.message_handler(text='🥤pepsi')
async def echo(message: types.Message):
    await message.answer_photo("https://babymarket.uz/wp-content/uploads/2020/05/peps_cola_05-l.jpg")
    await message.answer('''
    pepsi:0,5 litr
    narxi:9000 so'm
    ''')
    


@dp.message_handler(text='🥤CocaCola')
async def echo(message: types.Message):
    await message.answer_photo("https://babymarket.uz/wp-content/uploads/2020/07/coca-cola-05-l.jpg")
    await message.answer('''
    coca-cola:0,5 litr
    narxi:9000 so'm
    ''')




@dp.message_handler(text='🥤Sprite')
async def echo(message: types.Message):
    await message.answer_photo("https://hotei.by/files/products/sprite400x400.400x400.jpg?f92d566139ca5c5bd1bd7c03a89a35b8")
    await message.answer('''
    sprite:0,5 litr
    narxi:9000 so'm
    ''')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('siz ortga qaytdingiz',reply_markup=bosh_menu)


# ichimliklar bo'limini oxiri
# twister bo'limi boshi

@dp.message_handler(text="🌯Twister")
async def echo(message: types.Message):
    await message.answer_photo("https://www.kfc.co.at/img/asset/YXNzZXRzL3Byb2R1Y3RzL0tGQ19Ud2lzdGVyX05ldy5wbmc=?fm=png&w=1000&h=1000&s=1044ebe8017b85f9a3ff87c02eefaff9")
    await message.answer("Twisterlar bo'limi",reply_markup=twister_menu)

@dp.message_handler(text='🌯Twister-vedji:ostriy')
async def echo(message: types.Message):
    await message.answer_photo("hhttps://static.wikia.nocookie.net/kfc/images/5/55/Kfc5162-tenders_twister.jpg/revision/latest?cb=20160228012036")
    await message.answer('''
    tvister-vedji:ostriy
    narxi:27000 so'm
    ''')
    
@dp.message_handler(text='🌯Twister-vedji:original')
async def echo(message: types.Message):
    await message.answer_photo("https://static.wikia.nocookie.net/kfc/images/5/55/Kfc5162-tenders_twister.jpg/revision/latest?cb=20160228012036")
    await message.answer('''
    tvister-vedji:original
    narxi:22000 so'm
    ''')

@dp.message_handler(text='🌯Box master:ostriy')
async def echo(message: types.Message):
    await message.answer_photo("https://kfc.ee/wp-content/uploads/2021/10/Boxmaster_.png")
    await message.answer('''
    box-master: ostriy
    narxi:28000 so'm
    ''')


@dp.message_handler(text='🌯Box master:original')
async def echo(message: types.Message):
    await message.answer_photo("https://kfc.ee/wp-content/uploads/2021/10/Boxmaster_.png")
    await message.answer('''
    box-master: originalniy
    narxi:26000 so'm
    ''')


@dp.message_handler(text='🌯Twister:ostriy')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9rtL6AvJYjXazWD_g06oRetNyuR3Npv4CTQ&usqp=CAU")
    await message.answer('''
    twister:ostriy
    narxi:30000 so'm
    ''')


@dp.message_handler(text='🌯Twister:original')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9rtL6AvJYjXazWD_g06oRetNyuR3Npv4CTQ&usqp=CAU")
    await message.answer('''
    twister:originalniy
    narxi:30000 so'm
    ''')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('siz ortga qaytdingiz',reply_markup=bosh_menu)
# twister bo'limi oxiri
# pitsa bo'limi boshi

@dp.message_handler(text="🍕Pitsalar")
async def echo(message: types.Message):
    await message.answer_photo("https://zira.uz/wp-content/uploads/2018/03/pizza-main-1300x746.jpg")
    await message.answer("Pitsalar bo'limi",reply_markup=pitsa_menu)

@dp.message_handler(text='🍕pitsa-peperoni')
async def echo(message: types.Message):
    await message.answer_photo("https://s1.eda.ru/StaticContent/Photos/120131085053/171027192707/p_O.jpg")
    await message.answer('''
    pitsa:peperrony
    narxi:38000 so'm
    ''')

@dp.message_handler(text='🍕pitsa-qazili')
async def echo(message: types.Message):
    await message.answer_photo("https://bravopizza.uz/wp-content/uploads/2020/04/kazironi.jpg")
    await message.answer('''
    pitsa:qazili
    narxi:98000 so'm
    ''')


@dp.message_handler(text='🍕pitsa-kuriniy')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdxHHD4X_yH9dHLqfVSXzmVFMd-oWQVZv8-CgobLi7IgIiJDw0eT_ILo2-z45RcncTjwc&usqp=CAU")
    await message.answer('''
    pitsa:kuriniy
    narxi:54000 so'm
    ''')

@dp.message_handler(text='🍕pitsa-osartiy')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3Xpehbsr266NblTL0VpP6uyRsbfiYa9kuHVfHvQ_iIci_NaXYnlRKbOjqSDOc5Hp4wgM&usqp=CAU")
    await message.answer('''
    pitsa:osartiy
    narxi:79000 so'm
    ''')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('siz ortga qaytdingiz',reply_markup=bosh_menu)

# pitsa bo'limi oxiri
# burger bo'limi boshi
@dp.message_handler(text="🍔Burgerlar")
async def echo(message: types.Message):
    await message.answer_photo("https://s82079.cdn.ngenix.net/295x0/q3ayfr1erngfi7fpo7vmracz5gog")
    await message.answer("Burgerlar bo'limi",reply_markup=burger_menu)

@dp.message_handler(text='🍔cheesburger')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY0Dw5qv5iCvIyxSxNdiNYSqmNdNcEERH4eTURsGOJneKzPmwMsiL-MuXLV_RliHRwd04&usqp=CAU")
    await message.answer('''
    pitsa:osartiy
    narxi:20000 so'm
    ''')

@dp.message_handler(text='🍔shefburger')
async def echo(message: types.Message):
    await message.answer_photo("https://kfc-gid.ru/wp-content/uploads/2020/11/shefburger-ostryj-335x220.jpg")
    await message.answer('''
    pitsa:osartiy
    narxi:25000 so'm
    ''')


@dp.message_handler(text='🍔sanders-burger')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3l54iD55WIbB_atJf12UYLQQavFD-AitGFg&usqp=CAU")
    await message.answer('''
    pitsa:osartiy
    narxi:35000 so'm
    ''')


@dp.message_handler(text='🍔burger')
async def echo(message: types.Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6Srx6LzbpzmI04fe7MG8HbbNTgQj52HWv6s5lcNqfyW1roeli4SPHyJxS5NW8IQIgp8U&usqp=CAU")
    await message.answer('''
    pitsa:osartiy
    narxi:20000 so'm
    ''')

@dp.message_handler(text='⬅️Ortga')
async def send_welcome(message: types.Message):
    await message.reply('siz ortga qaytdingiz',reply_markup=bosh_menu)

# burger bo'limini oxiri
# shirinlik bolimili boshi


@dp.message_handler(text='🍰Shirinliklar')
async def echo(message: types.Message):
    await message.answer_photo("https://zira.uz/wp-content/uploads/2018/03/pizza-main-1300x746.jpg")
    await message.answer("Shirinliklar bo'limi",reply_markup=shirinlik_menu)

@dp.message_handler(text='🍰cheescake')
async def echo(message: types.Message):
    await message.answer_photo("https://www.jocooks.com/wp-content/uploads/2018/11/cheesecake-1-22.jpg")
    await message.answer('''
    cheescake
    narxi:10000 so'm
    ''')

@dp.message_handler(text='🍰asalli-tort')
async def echo(message: types.Message):
    await message.answer_photo("https://zira.uz/wp-content/uploads/2018/07/medovik-35.jpg")
    await message.answer('''
    asalli-tort
    narxi:10000 so'm
    ''')

@dp.message_handler(text='🍰puding')
async def echo(message: types.Message):
    await message.answer_photo("https://cdn.lifehacker.ru/wp-content/uploads/2022/09/shutterstock_2139465649_1664468404-scaled-e1664468467565-1280x640.jpg")
    await message.answer('''
    puding
    narxi:10000 so'm
    ''')


@dp.message_handler(text='⬅️Ortga')
async def send_welcome(message: types.Message):
    await message.reply('siz ortga qaytdingiz',reply_markup=bosh_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)