from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=
    [
    [
        KeyboardButton(text="🍹Ichimliklar"),
        KeyboardButton(text="🌯Twister"),
        
    ],
    [
        KeyboardButton(text="🍕Pitsalar"),
        KeyboardButton(text="🍔Burgerlar"),
       
    ],
    [
        KeyboardButton(text="🍰Shirinliklar")
    ],
],
)

ichimliklar_menu = ReplyKeyboardMarkup(
    keyboard = 
    [
        [
            KeyboardButton(text="🥤CocaCola"),
            KeyboardButton(text="🥤Fanta"),

        ],
         [
            KeyboardButton(text="🥤Sprite"),
            KeyboardButton(text="🥤pepsi"),

        ],
        [
        KeyboardButton(text="⬅️Ortga")
    ]
    ]
)

ichimliklar_menu = ReplyKeyboardMarkup(
    keyboard = 
    [
        [
            KeyboardButton(text="🥤CocaCola"),
            KeyboardButton(text="🥤Fanta"),

        ],
         [
            KeyboardButton(text="🥤Sprite"),
            KeyboardButton(text="🥤pepsi"),

        ],
        [
        KeyboardButton(text="⬅️Ortga")
    ]
    ]
)

twister_menu = ReplyKeyboardMarkup(
    keyboard=
    [
       [
            KeyboardButton(text="🌯Twister:original"),
            KeyboardButton(text="🌯Twister:ostriy"),

        ],  
          [
            KeyboardButton(text="🌯Box master:original"),
            KeyboardButton(text="🌯Box master:ostriy"),

        ], 
        [
             KeyboardButton(text="🌯Twister-vedji:original"),
            KeyboardButton(text="🌯Twister-vedji:ostriy"),
        ],
        [
        KeyboardButton(text="⬅️Ortga")
    ]
    ]
)

pitsa_menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
          KeyboardButton(text='🍕pitsa-peperoni'),
          KeyboardButton(text='🍕pitsa-qazili')
        ],
        [
            KeyboardButton(text='🍕pitsa-kuriniy'),
            KeyboardButton(text='🍕pitsa-osartiy')
        ],
        [
        KeyboardButton(text="⬅️Ortga")
    ]
    ]
)


burger_menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text='🍔cheesburger'),
            KeyboardButton(text='🍔shefburger')
        ],
        [
            KeyboardButton(text='🍔sanders-burger')
        ],
        [
            KeyboardButton(text='🍔burger')
        ],
        [
        KeyboardButton(text="⬅️Ortga")
    ]
    ]
)


shirinlik_menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text='🍰cheescake'),
            KeyboardButton(text='🍰asalli-tort')
        ],
        [
            KeyboardButton(text='🍰puding')
        ],
        [
        KeyboardButton(text="⬅️Ortga")
    ]
    ]
)