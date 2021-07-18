from instabot import Bot
import requests
from PIL import Image, ImageDraw, ImageFont

api = 'http://api.quotable.io/random'


def quote_generator():
    random_quote = requests.get(api).json()
    content = random_quote['content']
    split_cont = content.split()

    if len(split_cont) > 5:
        print(split_cont[5])
        split_cont.insert(5, '\n')

        if len(split_cont) > 12:
            print(split_cont[12])
            split_cont.insert(12, '\n')

            if len(split_cont) > 19:
                print(split_cont[19])
                split_cont.insert(19, '\n')

                if len(split_cont) > 24:
                    print(split_cont[24])
                    split_cont.insert(24, '\n')

                    if len(split_cont) > 29:
                        print(split_cont[29])
                        split_cont.insert(29, '\n')

        print(split_cont)
        final_sentence = ' '.join(split_cont)
        author = random_quote['author']

        quote = final_sentence + '\n\n' + "-" + author
        return quote


def auto_gram():
    bot = Bot()
    bot.login(username='luke1.temp16', password='luke1temp')
    quote = quote_generator()
    image = Image.open('pic.jfif')
    font_type = ImageFont.truetype('arial.ttf', 60)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(30, 150), text=quote, fill=(0, 0, 0), font=font_type)
    image.save('image.png')
    image.show()
    bot.upload_photo('image.png', caption='This is a randomly generated Quote put on a random picture, then uploaded without using instagram')


if __name__ == '__main__':
    auto_gram()
