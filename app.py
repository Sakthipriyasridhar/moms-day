import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Amma 💖", layout="centered")

# LOAD IMAGES

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

cover = get_base64("photos/COVER.jfif")
photo1 = get_base64("photos/PHOTO1.jfif")
photo2 = get_base64("photos/PHOTO2.jfif")
photo3 = get_base64("photos/PHOTO3.jfif")
photo4 = get_base64("photos/PHOTO4.jfif")
photo5 = get_base64("photos/PHOTO5.jfif")
last = get_base64("photos/FINAL.png")

html_code = f"""

<!DOCTYPE html>
<html lang="ta">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@300;400;700&display=swap" rel="stylesheet">

<style>

*{{
  margin:0;
  padding:0;
  box-sizing:border-box;
}}

body{{
  height:100vh;
  overflow:hidden;

  display:flex;
  justify-content:center;
  align-items:center;

  background:
  linear-gradient(135deg,#ffe0ec,#fff4f8,#fff0f5);

  font-family:'Noto Sans Tamil',sans-serif;
}}

/* HEARTS */

.hearts span{{
  position:absolute;
  bottom:-100px;

  font-size:22px;

  animation:floatHeart 10s linear infinite;

  opacity:0.7;
}}

.hearts span:nth-child(1){{left:10%;}}
.hearts span:nth-child(2){{left:30%;animation-delay:2s;}}
.hearts span:nth-child(3){{left:50%;animation-delay:4s;}}
.hearts span:nth-child(4){{left:70%;animation-delay:1s;}}
.hearts span:nth-child(5){{left:90%;animation-delay:3s;}}

@keyframes floatHeart{{

  0%{{
    transform:translateY(0) scale(0.5);
    opacity:0;
  }}

  10%{{
    opacity:1;
  }}

  100%{{
    transform:translateY(-120vh) scale(1.3);
    opacity:0;
  }}

}}

/* BUTTERFLIES */

.butterflies span{{
  position:absolute;

  font-size:28px;

  animation:butterflyFly 14s linear infinite;

  opacity:0.7;
}}

.butterflies span:nth-child(1){{
  left:15%;
  top:80%;
}}

.butterflies span:nth-child(2){{
  left:50%;
  top:85%;
  animation-delay:4s;
}}

.butterflies span:nth-child(3){{
  left:80%;
  top:75%;
  animation-delay:7s;
}}

@keyframes butterflyFly{{

  0%{{
    transform:
    translateY(0)
    translateX(0)
    rotate(0deg);
  }}

  100%{{
    transform:
    translateY(-120vh)
    translateX(100px)
    rotate(25deg);
  }}

}}

/* BOOK */

.book{{
  width:92vw;
  max-width:390px;

  height:88vh;
  max-height:720px;

  position:relative;

  perspective:3000px;

  border-radius:30px;

  box-shadow:
  0 25px 60px rgba(255,105,180,0.25);
}}

/* PAGE */

.page{{
  position:absolute;

  width:100%;
  height:100%;

  transform-origin:left;

  transition:transform 1.2s ease;

  border-radius:30px;

  overflow:hidden;

  backface-visibility:hidden;

  box-shadow:
  0 10px 30px rgba(0,0,0,0.12);
}}

.page.flipped{{
  transform:rotateY(-180deg);
}}

/* IMAGE */

.full-img{{
  width:100%;
  height:100%;

  object-fit:cover;

  position:absolute;
  inset:0;

  filter:
  brightness(0.82)
  saturate(1.08);

  animation:zoomEffect 12s ease-in-out infinite;
}}

@keyframes zoomEffect{{

  0%,100%{{
    transform:scale(1);
  }}

  50%{{
    transform:scale(1.05);
  }}

}}

/* OVERLAY */

.page::after{{
  content:'';

  position:absolute;
  inset:0;

  background:
  linear-gradient(
  to top,
  rgba(0,0,0,0.45),
  rgba(0,0,0,0.05)
  );
}}

/* TEXT */

.short-text{{
  position:absolute;

  bottom:40px;
  left:50%;

  transform:translateX(-50%);

  z-index:10;

  color:white;

  font-size:28px;
  font-weight:bold;

  text-align:center;

  text-shadow:
  0 4px 10px rgba(0,0,0,0.5);

  background:
  rgba(255,255,255,0.16);

  backdrop-filter:blur(10px);

  padding:12px 24px;

  border-radius:40px;

  white-space:nowrap;
}}

/* COVER */

.cover-text{{
  position:absolute;

  top:50%;
  left:50%;

  transform:translate(-50%,-50%);

  z-index:10;

  color:white;

  text-align:center;
}}

.cover-text h1{{
  font-size:42px;

  text-shadow:
  0 6px 18px rgba(0,0,0,0.5);
}}

.cover-text p{{
  margin-top:15px;

  font-size:20px;

  background:
  rgba(255,255,255,0.18);

  padding:12px 20px;

  border-radius:30px;

  backdrop-filter:blur(8px);
}}

/* BUTTONS */

.nav-buttons{{
  position:fixed;

  bottom:18px;
  left:50%;

  transform:translateX(-50%);

  display:flex;
  gap:18px;

  z-index:99999;
}}

.nav-buttons button{{
  width:58px;
  height:58px;

  border:none;
  border-radius:50%;

  background:
  linear-gradient(135deg,#ff6fa5,#ff93bc);

  color:white;

  font-size:24px;

  cursor:pointer;

  transition:0.3s;
}}

.nav-buttons button:hover{{
  transform:scale(1.12);

  box-shadow:
  0 0 25px rgba(255,105,180,0.6);
}}

</style>

</head>

<body>

<div class="hearts">

  <span>💖</span>
  <span>✨</span>
  <span>🌸</span>
  <span>💕</span>
  <span>🦋</span>

</div>

<div class="butterflies">

  <span>🦋</span>
  <span>🦋</span>
  <span>🦋</span>

</div>

<div class="book">

  <!-- COVER -->

  <div class="page" style="z-index:7;">

    <img src="data:image/jpg;base64,{cover}" class="full-img">

    <div class="cover-text">

      <h1>அம்மாவுக்கு 💖</h1>

      <p>அன்னையர் தின வாழ்த்துக்கள் ✨</p>

    </div>

  </div>

  <!-- PAGE 1 -->

  <div class="page" style="z-index:6;">

    <img src="data:image/jpg;base64,{photo1}" class="full-img">

    <div class="short-text">
      என் உலகம் 💖
    </div>

  </div>

  <!-- PAGE 2 -->

  <div class="page" style="z-index:5;">

    <img src="data:image/jpg;base64,{photo2}" class="full-img">

    <div class="short-text">
      என் அம்மா 🌸
    </div>

  </div>

  <!-- PAGE 3 -->

  <div class="page" style="z-index:4;">

    <img src="data:image/jpg;base64,{photo3}" class="full-img">

    <div class="short-text">
      என் செல்லம் ✨
    </div>

  </div>

  <!-- PAGE 4 -->

  <div class="page" style="z-index:3;">

    <img src="data:image/jpg;base64,{photo4}" class="full-img">

    <div class="short-text">
      என் தேவதை 👑
    </div>

  </div>

  <!-- PAGE 5 -->

  <div class="page" style="z-index:2;">

    <img src="data:image/jpg;base64,{photo5}" class="full-img">

    <div class="short-text">
      என்றும் அன்பு 💕
    </div>

  </div>

  <!-- LAST -->

  <div class="page" style="z-index:1;">

    <img src="data:image/png;base64,{last}" class="full-img">

    <div class="short-text">
      LOVE U அம்மா 🥺
    </div>

  </div>

</div>

<!-- BUTTONS -->

<div class="nav-buttons">

  <button id="prevBtn">⬅</button>

  <button id="nextBtn">➡</button>

</div>

<script>

let currentPage = 0;

const pages =
document.querySelectorAll('.page');

const nextBtn =
document.getElementById('nextBtn');

const prevBtn =
document.getElementById('prevBtn');

/* POPPERS */

function createPopper(){{

  for(let i=0;i<40;i++){{

    const pop=document.createElement("div");

    pop.innerHTML=
    ["💖","✨","🌸","🎉","🦋","💕"]
    [Math.floor(Math.random()*6)];

    pop.style.position="fixed";

    pop.style.left=
    Math.random()*100+"vw";

    pop.style.top="65vh";

    pop.style.fontSize=
    (Math.random()*24+18)+"px";

    pop.style.pointerEvents="none";

    pop.style.zIndex="999999";

    pop.style.transition=
    "all 1.8s ease";

    document.body.appendChild(pop);

    setTimeout(()=>{{

      pop.style.transform=
      `translate(
      ${{(Math.random()-0.5)*600}}px,
      ${{-Math.random()*700}}px
      ) rotate(${{Math.random()*720}}deg)`;

      pop.style.opacity="0";

    }},50);

    setTimeout(()=>{{
      pop.remove();
    }},2000);

  }}

}}

/* NEXT */

nextBtn.addEventListener('click',()=>{{

  if(currentPage < pages.length-1){{

    pages[currentPage]
    .classList.add('flipped');

    createPopper();

    currentPage++;

  }}

}});

/* PREVIOUS */

prevBtn.addEventListener('click',()=>{{

  if(currentPage > 0){{

    currentPage--;

    pages[currentPage]
    .classList.remove('flipped');

  }}

}});

</script>

</body>
</html>

"""

components.html(
    html_code,
    height=760,
    scrolling=False
)
