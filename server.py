from flask import Flask
import random

INTRO_GIF_URL = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2c3MjVrOWRiemg0MDIwdGFhdXlpbndjcGh0ZG80d2llcXZlZm0yNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlSH2gsSrxJySnS/giphy.webp"
FAIL_GIF_URL = "https://media2.giphy.com/media/yMN6JhJDWwygo/200.webp?cid=ecf05e47b4wvofadyfvz12829josx9ietuyf9vb7412i5ofi&ep=v1_gifs_search&rid=200.webp&ct=g"
SUCCESS_GIF_URL = "https://media3.giphy.com/media/l2Sq2CgD97kJatmgM/200.webp?cid=790b7611d6yxt0wzfq9qovxolpmbqtdypeoqdm06kmupkzxj&ep=v1_gifs_search&rid=200.webp&ct=g"
app = Flask(__name__)


@app.route("/")
def start():
    return (f'<h1>Guess a number between 0 and '
            '9</h1><img src="https://media4.giphy.com/media/v1'
            '.Y2lkPTc5MGI3NjExb2c3MjVrOWRiemg0MDIwdGFhdXlpbndjcGh0ZG80d2llcXZlZm0yNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlSH2gsSrxJySnS/giphy.webp">')

winning_number = random.randint(0, 9)
print(winning_number)
@app.route("/<int:guess>")
def guessing(guess):
    if guess == winning_number:
        return (f'<h1 style="color:green">You win gg</h1><img '
                f'src="https://media3.giphy.com/media/l2Sq2CgD97kJatmgM/200'
                f'.webp?cid=790b7611d6yxt0wzfq9qovxolpmbqtdypeoqdm06kmupkzxj&ep=v1_gifs_search&rid=200.webp&ct=g">')
    else:
        return (f'<h1 style="color:red">You lose xd</h1><img '
                f'src="https://media2.giphy.com/media/yMN6JhJDWwygo/200.webp'
                f'?cid=ecf05e47b4wvofadyfvz12829josx9ietuyf9vb7412i5ofi&ep'
                f'=v1_gifs_search&rid=200.webp&ct=g">')


if __name__ == "__main__":
    app.run(debug=True)
