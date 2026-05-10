import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Amma 💖", layout="centered")

# FUNCTION TO LOAD IMAGES

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# LOAD IMAGES FROM photos FOLDER

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
  background:linear-gradient(135deg,#ffe0ec,#fff4f8,#fff0f5);
  font-family:'Noto Sans Tamil',sans-serif;
}}

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

.book{{
  width:92vw;
  max-width:390px;
  height:88vh;
  max-height:720px;
  position:relative;
  perspective:3000px;
  border-radius:30px;
  box-shadow:0 25px 60px rgba(255,105,180,0.25);
}}

.page{{
  position:absolute;
  width:100%;
  height:100%;
  transform-origin:left;
  transition:transform 1.2s ease;
  border-radius:30px;
  overflow:hidden;
  backface-visibility:hidden;
  box-shadow:0 10px 30px rgba(0,0,0,0.12);
}}

.page.flipped{{
  transform:rotateY(-180deg);
}}

.full-img{{
  width:100%;
  height:100%;
  object-fit:cover;
  position:absolute;
  inset:0;
  filter:brightness(0.82) saturate(1.08);
}}

.page::after{{
  content:'';
  position:absolute;
  inset:0;
  background:linear-gradient(
  to top,
  rgba(0,0,0,0.45),
  rgba(0,0,0,0.05)
  );
}}

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
  text-shadow:0 4px 10px rgba(0,0,0,0.5);
  background:rgba(255,255,255,0.16);
  backdrop-filter:blur(10px);
  padding:12px 24px;
  border-radius:40px;
  white-space:nowrap;
}}

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
  text-shadow:0 6px 18px rgba(0,0,0,0.5);
}}

.cover-text p{{
  margin-top:15px;
  font-size:20px;
  background:rgba(255,255,255,0.18);
  padding:12px 20px;
  border-radius:30px;
  backdrop-filter:blur(8px);
}}

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
  background:linear-gradient(135deg,#ff6fa5,#ff93bc);
  color:white;
  font-size:24px;
  cursor:pointer;
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

<div class="book">

  <div class="page" style="z-index:7;">
    <img src="data:image/jpg;base64,{cover}" class="full-img">

    <div class="cover-text">
      <h1>அம்மாவுக்கு 💖</h1>
      <p>அன்னையர் தின வாழ்த்துக்கள் ✨</p>
    </div>
  </div>

  <div class="page" style="z-index:6;">
    <img src="data:image/jpg;base64,{photo1}" class="full-img">
    <div class="short-text">என் உலகம் 💖</div>
  </div>

  <div class="page" style="z-index:5;">
    <img src="data:image/jpg;base64,{photo2}" class="full-img">
    <div class="short-text">என் அம்மா 🌸</div>
  </div>

  <div class="page" style="z-index:4;">
    <img src="data:image/jpg;base64,{photo3}" class="full-img">
    <div class="short-text">என் செல்லம் ✨</div>
  </div>

  <div class="page" style="z-index:3;">
    <img src="data:image/jpg;base64,{photo4}" class="full-img">
    <div class="short-text">என் தேவதை 👑</div>
  </div>

  <div class="page" style="z-index:2;">
    <img src="data:image/jpg;base64,{photo5}" class="full-img">
    <div class="short-text">என்றும் அன்பு 💕</div>
  </div>

  <div class="page" style="z-index:1;">
    <img src="data:image/png;base64,{last}" class="full-img">
    <div class="short-text">LOVE U அம்மா 🥺</div>
  </div>

</div>

<div class="nav-buttons">
  <button id="prevBtn">⬅</button>
  <button id="nextBtn">➡</button>
</div>

<script>

let currentPage = 0;

const pages = document.querySelectorAll('.page');

const nextBtn = document.getElementById('nextBtn');

const prevBtn = document.getElementById('prevBtn');

nextBtn.addEventListener('click',()=>{{

  if(currentPage < pages.length-1){{

    pages[currentPage].classList.add('flipped');

    currentPage++;
  }}

}});

prevBtn.addEventListener('click',()=>{{

  if(currentPage > 0){{

    currentPage--;

    pages[currentPage].classList.remove('flipped');
  }}

}});

</script>

</body>
</html>

"""

components.html(html_code, height=760, scrolling=False)
