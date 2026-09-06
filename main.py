from flask import Flask, render_template_string

app = Flask(__name__)

    HOME = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DIY Builder</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #050b18;
    color: white;
    font-family: Arial, sans-serif;
}

.container {
    max-width: 600px;
    margin: auto;
    padding: 25px 18px 120px;
}

/* HEADER */

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
}

.small {
    color: #8d96aa;
    font-size: 13px;
    letter-spacing: 1px;
}

h1 {
    margin: 5px 0;
    font-size: 31px;
}

.sub {
    color: #8d96aa;
    font-size: 15px;
}

.avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg,#7c5cff,#4b35db);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
}

/* SEARCH */

.search {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #101a30;
    border: 1px solid #293758;
    border-radius: 18px;
    padding: 15px 17px;
    margin-bottom: 18px;
}

.search input {
    width: 100%;
    border: 0;
    outline: 0;
    background: transparent;
    color: white;
    font-size: 16px;
}

.search input::placeholder {
    color: #7e879b;
}

/* SCAN */

.scan {
    position: relative;
    overflow: hidden;
    border-radius: 25px;
    padding: 23px;
    background:
        linear-gradient(
            135deg,
            rgba(94,74,235,.95),
            rgba(35,24,110,.98)
        );
    box-shadow: 0 15px 40px rgba(75,55,220,.25);
}

.scan:after {
    content: "";
    position: absolute;
    width: 190px;
    height: 190px;
    border-radius: 50%;
    background: rgba(255,255,255,.06);
    right: -70px;
    top: -70px;
}

.scan-icon {
    width: 52px;
    height: 52px;
    border-radius: 16px;
    background: rgba(255,255,255,.16);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
}

.scan h2 {
    margin: 18px 0 6px;
    font-size: 24px;
}

.scan p {
    color: #d4d0ff;
    margin: 0;
}

.scan-btn {
    display: inline-block;
    margin-top: 20px;
    padding: 13px 20px;
    background: white;
    color: #5142df;
    border-radius: 14px;
    font-weight: bold;
}

/* MANUAL */

.manual {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 13px;
    padding: 18px;
    background: #101a30;
    border: 1px solid #1d2a45;
    border-radius: 20px;
    color: white;
    text-decoration: none;
}

.manual-left {
    display: flex;
    align-items: center;
    gap: 13px;
}

.manual-icon {
    width: 40px;
    height: 40px;
    border-radius: 13px;
    background: #283a70;
    display: flex;
    align-items: center;
    justify-content: center;
}

.manual small {
    color: #7f8ba3;
    display: block;
    margin-top: 3px;
}

/* SECTION */

.section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 30px;
    margin-bottom: 14px;
}

.section h2 {
    margin: 0;
    font-size: 20px;
}

.count {
    color: #8b94a9;
    font-size: 13px;
}

/* PARTS */

.parts {
    display: flex;
    gap: 12px;
    overflow-x: auto;
}

.parts::-webkit-scrollbar {
    display: none;
}

.part {
    min-width: 95px;
    padding: 12px;
    border-radius: 19px;
    background: #101a30;
    border: 1px solid #1d2a45;
    text-align: center;
}

.part-img {
    width: 65px;
    height: 65px;
    margin: auto;
    border-radius: 16px;
    background: #e9e9ed;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
}

.part-name {
    margin-top: 9px;
    font-size: 13px;
}

/* BUILDS */

.builds {
    display: flex;
    gap: 14px;
    overflow-x: auto;
}

.builds::-webkit-scrollbar {
    display: none;
}

.card {
    min-width: 245px;
    overflow: hidden;
    background: #101a30;
    border: 1px solid #1d2a45;
    border-radius: 23px;
}

.card-img {
    height: 145px;
    background: #e9e9ed;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 75px;
}

.card-content {
    padding: 15px;
}

.card h3 {
    margin: 0 0 8px;
    font-size: 19px;
}

.match {
    color: #39cf8b;
    font-size: 13px;
    font-weight: bold;
}

.time {
    color: #7f8ba3;
    margin-top: 8px;
    font-size: 13px;
}

/* NAVIGATION */

.bottom {
    position: fixed;
    left: 15px;
    right: 15px;
    bottom: 14px;
    max-width: 570px;
    margin: auto;
    height: 70px;
    border-radius: 25px;
    background: rgba(12,20,38,.94);
    border: 1px solid #26334f;
    display: flex;
    justify-content: space-around;
    align-items: center;
    z-index: 20;
}

.nav {
    color: #7e899f;
    text-align: center;
    font-size: 11px;
}

.nav-icon {
    font-size: 21px;
    margin-bottom: 4px;
}

.active {
    color: #826bff;
}

.plus {
    width: 53px;
    height: 53px;
    border-radius: 18px;
    background: linear-gradient(135deg,#765cff,#4935dc);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    box-shadow: 0 8px 25px rgba(92,70,230,.4);
}
</style>
</head>

<body>

<div class="container">

<!-- HEADER -->

<div class="header">

    <div>
        <div class="small">WELCOME BACK</div>
        <h1>Hi, Everyone 👋</h1>
        <div class="sub">Build something amazing today.</div>
    </div>

    <div class="avatar">E</div>

</div>


<!-- SEARCH -->

<div class="search">

    🔍

    <input
        id="searchParts"
        type="text"
        placeholder="Search your parts..."
        oninput="searchParts()"
    >

</div>


<!-- SCAN -->

<div class="scan">

    <div class="scan-icon">▣</div>

    <h2>Scan a Part</h2>

    <p>Identify your components with your camera.</p>

    <label class="scan-btn" for="cameraInput">
        Scan with Camera
    </label>

</div>

<input
    id="cameraInput"
    type="file"
    accept="image/*"
    capture="environment"
    style="display:none"
    onchange="showScan(event)"
>


<!-- MANUAL -->

<a href="/parts" class="manual">

    <div class="manual-left">

        <div class="manual-icon">＋</div>

        <div>
            <b>Add parts manually</b>
            <small>Browse and add your components</small>
        </div>

    </div>

    <b>›</b>

</a>


<!-- YOUR PARTS -->

<div class="section">

    <h2>Your Parts</h2>

    <div class="count">5 parts</div>

</div>


<div class="parts">

    <div class="part">
        <div class="part-img">⚙</div>
        <div class="part-name">Motor</div>
    </div>

    <div class="part">
        <div class="part-img">◉</div>
        <div class="part-name">Wheel</div>
    </div>

    <div class="part">
        <div class="part-img">⚙</div>
        <div class="part-name">Gear</div>
    </div>

    <div class="part">
        <div class="part-img">●</div>
        <div class="part-name">LED</div>
    </div>

    <div class="part">
        <div class="part-img">▭</div>
        <div class="part-name">Battery</div>
    </div>

</div>


<!-- SUGGESTED BUILDS -->

<div class="section">

    <h2>Suggested Builds</h2>

    <div class="count">See all ›</div>

</div>


<div class="builds">

<a href="/mini-fan">

<div class="card">

    <div class="card-img">🌀</div>

    <div class="card-content">

        <h3>Mini Fan</h3>

        <div class="match">● 95% Match</div>

        <div class="time">
            Easy · 30 min
        </div>

    </div>

</div>

</a>


<div class="card">

    <div class="card-img">🚗</div>

    <div class="card-content">

        <h3>RC Car</h3>

        <div class="match">● 88% Match</div>

        <div class="time">
            Medium · 2–3 hrs
        </div>

    </div>

</div>


<div class="card">

    <div class="card-img">💡</div>

    <div class="card-content">

        <h3>Desk Lamp</h3>

        <div class="match">● 75% Match</div>

        <div class="time">
            Easy · 45 min
        </div>

    </div>

</div>

</div>

</div>


<!-- BOTTOM NAV -->

<div class="bottom">

    <div class="nav active">
        <div class="nav-icon">⌂</div>
        Home
    </div>

    <div class="nav">
        <div class="nav-icon">⌕</div>
        Search
    </div>

    <div class="plus">+</div>

    <div class="nav">
        <div class="nav-icon">▣</div>
        Projects
    </div>

    <div class="nav">
        <div class="nav-icon">○</div>
        Profile
    </div>

</div>


<script>

function searchParts() {

    const text =
        document.getElementById("searchParts")
        .value
        .toLowerCase()
        .trim();

    document.querySelectorAll(".parts .part").forEach(part => {

        const name =
            part.innerText.toLowerCase();

        if (name.includes(text)) {
            part.style.display = "block";
        } else {
            part.style.display = "none";
        }

    });

}


function showScan(event) {

    const file = event.target.files[0];

    if (!file) return;

    const url = URL.createObjectURL(file);

    document.body.innerHTML = `

        <div style="
            min-height:100vh;
            background:#050b18;
            color:white;
            padding:25px;
            font-family:Arial;
        ">

            <h2>← Scan Result</h2>

            <div style="
                background:#101a30;
                padding:20px;
                border-radius:25px;
                text-align:center;
            ">

                <img
                    src="${url}"
                    style="
                        width:100%;
                        max-height:400px;
                        object-fit:contain;
                        border-radius:20px;
                    "
                >

                <h2>Part scanned successfully ✓</h2>

                <button
                    onclick="location.href='/'"
                    style="
                        width:100%;
                        border:0;
                        padding:18px;
                        border-radius:15px;
                        background:#624cff;
                        color:white;
                        font-size:18px;
                    "
                >
                    Back to Home
                </button>

            </div>

        </div>
    `;
}

</script>

</body>
</html>
"""
