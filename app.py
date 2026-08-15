from flask import Flask, request, redirect, url_for, render_template_string
from datetime import datetime

app = Flask(
    __name__,
    static_folder="Static",
    static_url_path="/static"
)

MESSAGE_FILE = "gbemi_messages.txt"


HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>For Gbemi ❤️</title>

<style>

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #080808;
    color: white;
    overflow-x: hidden;
}

/* =========================
   OPENING SCREEN
========================= */

.opening {
    position: fixed;
    inset: 0;
    z-index: 9999;

    display: flex;
    justify-content: center;
    align-items: center;

    text-align: center;

    background:
        radial-gradient(
            circle at center,
            #4d0024,
            #16000b 45%,
            #050505 100%
        );

    transition: opacity 1s ease;
}

.opening-content {
    width: 90%;
    max-width: 430px;
}

.big-heart {
    font-size: 80px;

    animation: heartbeat 1.4s infinite;
}

.opening h1 {
    font-size: 38px;
    margin: 15px 0 10px;
}

.opening p {
    color: #ddd;
    font-size: 17px;
    line-height: 1.6;
}

.open-button {
    margin-top: 25px;

    padding: 15px 34px;

    border: none;
    border-radius: 40px;

    background: #ff3f78;
    color: white;

    font-size: 17px;
    font-weight: bold;

    box-shadow:
        0 0 25px rgba(255, 63, 120, 0.5);

    cursor: pointer;
}

/* =========================
   MAIN PAGE
========================= */

.main {
    display: none;
}

section {
    min-height: 100vh;

    padding: 75px 20px;

    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    width: 100%;
    max-width: 480px;
    text-align: center;
}

/* =========================
   HERO
========================= */

.hero {
    background:
        radial-gradient(
            circle at top,
            #62002f,
            #100008 55%,
            #050505 100%
        );
}

.hero-heart {
    font-size: 75px;

    animation: heartbeat 1.5s infinite;
}

.hero h1 {
    font-size: 50px;
    margin: 15px 0 8px;
}

.hero p {
    color: #ff9fbd;
    font-size: 19px;
}

.scroll-text {
    margin-top: 60px;

    color: #aaa;

    animation: bounce 2s infinite;
}

/* =========================
   LOVE LETTER
========================= */

.letter {
    background:
        linear-gradient(
            180deg,
            #100008,
            #19000e
        );
}

.letter-card {
    padding: 30px 23px;

    border-radius: 25px;

    background:
        rgba(255,255,255,0.055);

    border:
        1px solid rgba(255,255,255,0.1);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.45);
}

.letter-card h2 {
    color: #ff719d;
    font-size: 29px;
    margin-bottom: 25px;
}

.letter-card p {
    color: #ddd;

    font-size: 17px;

    line-height: 1.85;

    text-align: left;
}

.highlight {
    color: #ff9fbd;
    font-weight: bold;
}

/* =========================
   PHOTO GALLERY
========================= */

.photos {
    background: #080808;
}

.photos h2 {
    font-size: 30px;
    margin-bottom: 8px;
}

.photos-subtitle {
    color: #999;
    margin-bottom: 30px;
}

.photo-card {
    margin-bottom: 30px;

    padding: 10px;

    border-radius: 22px;

    background:
        rgba(255,255,255,0.05);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.5);

    animation: photoAppear 1s ease;
}

.photo-card img {
    display: block;

    width: 100%;

    border-radius: 16px;

    /* The original photo itself is NOT edited */
    object-fit: cover;
}

.photo-caption {
    padding: 12px 5px 5px;

    color: #ddd;

    font-size: 15px;
}

/* =========================
   APPRECIATION
========================= */

.appreciation {
    background:
        linear-gradient(
            180deg,
            #080808,
            #17000c
        );
}

.appreciation h2 {
    font-size: 29px;
}

.love-item {
    margin: 16px 0;

    padding: 18px;

    border-radius: 18px;

    background:
        rgba(255,255,255,0.055);

    text-align: left;

    color: #ddd;

    line-height: 1.6;
}

.love-item span {
    font-size: 25px;
    margin-right: 8px;
}

/* =========================
   THINGS I HOPE FOR YOU
========================= */

.hope {
    background:
        radial-gradient(
            circle at center,
            #39001b,
            #080808 70%
        );
}

.hope h2 {
    font-size: 31px;
}

.hope-intro {
    color: #ccc;
    line-height: 1.7;
}

.hope-item {
    margin: 18px 0;

    padding: 20px;

    border-left: 3px solid #ff4f87;

    background:
        rgba(255,255,255,0.05);

    border-radius: 0 15px 15px 0;

    text-align: left;

    color: #ddd;

    line-height: 1.7;
}

/* =========================
   FINAL MESSAGE
========================= */

.final {
    background:
        radial-gradient(
            circle,
            #500027,
            #080808 70%
        );
}

.final-heart {
    font-size: 70px;

    animation: heartbeat 1.5s infinite;
}

.final h2 {
    font-size: 32px;
}

.final p {
    color: #ddd;

    line-height: 1.8;

    font-size: 17px;
}

/* =========================
   REPLY
========================= */

.reply {
    background: #060606;
}

.reply h2 {
    font-size: 29px;
}

.reply p {
    color: #999;
}

textarea {
    width: 100%;

    min-height: 140px;

    padding: 16px;

    border-radius: 18px;

    border: 1px solid #444;

    background: #121212;

    color: white;

    font-size: 16px;

    outline: none;

    resize: vertical;
}

textarea:focus {
    border-color: #ff4f87;
}

.send-button {
    width: 100%;

    margin-top: 15px;

    padding: 15px;

    border: none;

    border-radius: 35px;

    background: #ff3f78;

    color: white;

    font-size: 17px;

    font-weight: bold;
}

/* =========================
   FLOATING HEARTS
========================= */

.floating-heart {
    position: fixed;

    bottom: -40px;

    font-size: 22px;

    pointer-events: none;

    z-index: 100;

    animation:
        floatUp 6s linear forwards;
}

/* =========================
   ANIMATIONS
========================= */

@keyframes heartbeat {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.18);
    }

}

@keyframes bounce {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(12px);
    }

}

@keyframes floatUp {

    0% {
        transform:
            translateY(0)
            rotate(0deg);

        opacity: 0;
    }

    15% {
        opacity: 1;
    }

    100% {
        transform:
            translateY(-110vh)
            rotate(360deg);

        opacity: 0;
    }

}

@keyframes photoAppear {

    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }

}

</style>

</head>


<body>


<!-- =========================
     OPENING
========================= -->

<div class="opening" id="opening">

    <div class="opening-content">

        <div class="big-heart">
            ❤️
        </div>

        <h1>
            Hey Gbemi...
        </h1>

        <p>
            I made something for you.
            <br>
            Take your time with it.
        </p>

        <button
            class="open-button"
            onclick="openLovePage()">

            Open it ❤️

        </button>

    </div>

</div>


<!-- =========================
     MAIN
========================= -->

<div class="main" id="main">


<!-- HERO -->

<section class="hero">

    <div class="container">

        <div class="hero-heart">
            ❤️
        </div>

        <h1>
            Gbemi
        </h1>

        <p>
            This little page is just for you.
        </p>

        <div class="scroll-text">
            ↓ Scroll slowly ↓
        </div>

    </div>

</section>


<!-- LOVE LETTER -->

<section class="letter">

    <div class="container">

        <div class="letter-card">

            <h2>
                A Little Something From Me ❤️
            </h2>


            <p>
                Gbemi,
            </p>


            <p>
                I honestly don't even know the perfect way
                to put everything I feel into words,
                but I want to try.
            </p>


            <p>
                I really love how you are.
                The little things about you,
                the way you talk,
                the way you carry yourself,
                and the way some of our conversations
                can stay on my mind even after we've stopped talking.
                There is just something about you
                that makes you special to me.
            </p>


            <p>
                And honestly, I don't just want good things
                for you because I care about you.
                I genuinely want to see you win.
            </p>


            <p>
                I want to see you happy,
                successful, peaceful,
                and proud of the person you're becoming.
                I want you to achieve the things you dream about,
                even the ones you haven't told me about.
            </p>


            <p class="highlight">
                I want the best for you, always.
            </p>


            <p>
                Sometimes I may not know exactly what to say
                or how to express myself.
                Sometimes I may get things wrong.
                But underneath all of that,
                there is something very simple:
                I genuinely care about you.
            </p>


            <p>
                I appreciate having you in my life.
                I appreciate every conversation,
                every laugh,
                every little moment,
                and even the moments that have taught me something.
            </p>


            <p>
                You are important to me, Gbemi.
            </p>


            <p>
                And whatever life brings,
                I hope you never forget that there is someone
                out here who genuinely wants to see you happy,
                doing well,
                and becoming everything you want to become.
            </p>


            <p>
                Maybe that's one of the simplest ways
                I can explain how I feel about you:
            </p>


            <p class="highlight">
                I care about you,
                I appreciate you,
                and I genuinely want the best for you. ❤️
            </p>


            <p>
                — Sammy
            </p>

        </div>

    </div>

</section>


<!-- PHOTOS -->

<section class="photos">

    <div class="container">

        <h2>
            A Few Pictures of You 📸
        </h2>

        <p class="photos-subtitle">
            Just because I like seeing you smile.
        </p>


        <div class="photo-card">

            <img
                src="/static/Image/Gbemi1.jpg"
                alt="Gbemi">

            <div class="photo-caption">
                You look beautiful here. ❤️
            </div>

        </div>


        <div class="photo-card">

            <img
                src="/static/Image/Gbemi2.jpg"
                alt="Gbemi">

            <div class="photo-caption">
                Another one I really like. 💕
            </div>

        </div>


        <div class="photo-card">

            <img
                src="/static/Image/Gbemi3.jpg"
                alt="Gbemi">

            <div class="photo-caption">
                And this one has its own vibe. 🖤
            </div>

        </div>

    </div>

</section>


<!-- APPRECIATION -->

<section class="appreciation">

    <div class="container">

        <h2>
            Things I Appreciate About You ❤️
        </h2>


        <div class="love-item">

            <span>😊</span>

            Your smile and the way you can make
            a conversation interesting.

        </div>


        <div class="love-item">

            <span>💬</span>

            The little conversations that somehow
            stay in my head.

        </div>


        <div class="love-item">

            <span>🫶</span>

            The person you are,
            beyond everything else.

        </div>


        <div class="love-item">

            <span>✨</span>

            The little things that make you,
            you.

        </div>

    </div>

</section>


<!-- THINGS I HOPE FOR HER -->

<section class="hope">

    <div class="container">

        <h2>
            Things I Hope For You 🌷
        </h2>


        <p class="hope-intro">
            Since I genuinely want the best for you,
            these are some of the things I hope life gives you.
        </p>


        <div class="hope-item">

            🌷 I hope you find happiness
            in the things you do.

        </div>


        <div class="hope-item">

            ✨ I hope you achieve the goals
            you're working toward,
            even the ones that seem far away right now.

        </div>


        <div class="hope-item">

            💪 I hope you never forget
            how capable you are.

        </div>


        <div class="hope-item">

            🫶 I hope you always have people around you
            who genuinely value and appreciate you.

        </div>


        <div class="hope-item">

            🌸 I hope life gives you
            more beautiful moments
            than difficult ones.

        </div>


        <div class="hope-item">

            ❤️ And most importantly,
            I hope you become the person
            you truly want to be.

        </div>

    </div>

</section>


<!-- FINAL -->

<section class="final">

    <div class="container">

        <div class="final-heart">
            ❤️
        </div>


        <h2>
            One Last Thing...
        </h2>


        <p>
            I don't know exactly where life takes us,
            but I'm genuinely glad our paths crossed.
        </p>


        <p>
            You mean more to me than I probably
            manage to say sometimes.
        </p>


        <p>
            And I hope when you look back at this,
            you remember that someone cared enough
            to make something like this just to make you smile.
        </p>


        <p class="highlight">
            Keep being you, Gbemi. ❤️
        </p>


        <p>
            — Sammy
        </p>

    </div>

</section>


<!-- REPLY -->

<section class="reply">

    <div class="container">

        <h2>
            Leave Something For Me 💌
        </h2>


        <p>
            If you want,
            leave me a little message.
        </p>


        <form
            method="POST"
            action="/reply">

            <textarea
                name="message"
                placeholder="Write something here..."
                required></textarea>


            <button
                class="send-button"
                type="submit">

                Send to Sammy ❤️

            </button>

        </form>

    </div>

</section>


</div>


<script>

/* =========================
   OPEN PAGE
========================= */

function openLovePage() {

    const opening =
        document.getElementById("opening");

    const main =
        document.getElementById("main");


    opening.style.opacity = "0";


    setTimeout(function() {

        opening.style.display = "none";

        main.style.display = "block";

        startHearts();

    }, 1000);

}


/* =========================
   FLOATING HEARTS
========================= */

function startHearts() {

    setInterval(function() {

        const heart =
            document.createElement("div");


        heart.className =
            "floating-heart";


        const hearts = [
            "❤️",
            "💕",
            "💗",
            "💖",
            "💓"
        ];


        heart.innerHTML =
            hearts[
                Math.floor(
                    Math.random() * hearts.length
                )
            ];


        heart.style.left =
            Math.random() * 100 + "%";


        heart.style.animationDuration =
            (4 + Math.random() * 4) + "s";


        document.body.appendChild(heart);


        setTimeout(function() {

            heart.remove();

        }, 8000);


    }, 800);

}

</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(HTML)


@app.route("/reply", methods=["POST"])
def reply():

    message = request.form.get(
        "message",
        ""
    ).strip()


    if message:

        with open(
            MESSAGE_FILE,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                "\\n-------------------------\\n"
            )

            file.write(
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )

            file.write("\\n")

            file.write(message)

            file.write("\\n")


    return redirect(
        url_for("home")
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )