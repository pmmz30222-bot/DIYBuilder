from flask import Flask, render_template_string

app = Flask(__name__)

HOME = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DIY Builder</title>

<style>
body {
    margin: 0;
    background: #f8f7fc;
    font-family: Georgia, serif;
    color: #222;
}

.container {
    padding: 25px 30px 110px;
}

h1 {
    font-size: 38px;
    margin: 0;
}

.subtitle {
    color: #777;
    font-size: 20px;
    margin: 8px 0 25px;
}

.search {
    background: white;
    border: 1px solid #ddd;
    border-radius: 40px;
    padding: 20px;
    font-size: 20px;
    margin-bottom: 25px;
}

.buttons {
    display: flex;
    gap: 20px;
}

.button {
    flex: 1;
    width: 80;
    box-sizing: border-box;
    padding: 30px 10px;
    border-radius: 25px;
    text-align: center;
    font-size: 22px;
    display: block;
    cursor: pointer;
}

.scan {
    background: #5142df;
    color: white;
}

.manual {
    background: white;
}

.section {
    font-size: 30px;
    margin-top: 35px;
}

.parts {
    display: flex;
    gap: 12px;
    overflow-x: auto;
}

.part {
    min-width: 110px;
    background: white;
    border-radius: 20px;
    padding: 20px 10px;
    text-align: center;
    font-size: 18px;
}

.icon {
    font-size: 45px;
}

.builds {
    display: flex;
    gap: 18px;
    overflow-x: auto;
}

.card {
    min-width: 270px;
    background: white;
    border-radius: 25px;
    padding: 15px;
    cursor: pointer;
}

.card-img {
    background: #f0eff5;
    border-radius: 20px;
    height: 170px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 80px;
}

.card h2 {
    margin-bottom: 5px;
}

.match {
    color: #3ba86b;
}

.bottom {
    position: fixed;
    bottom: 15px;
    left: 20px;
    right: 20px;
    height: 75px;
    background: white;
    border-radius: 35px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    box-shadow: 0 3px 20px #ddd;
}

.plus {
    background: #5142df;
    color: white;
    width: 65px;
    height: 65px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 40px;
}
</style>
</head>

<body>

<div class="container">

<h1>Hi, Aung! 👋</h1>
<div class="subtitle">What will you build today?</div>

<div class="search">🔍 &nbsp; Search parts...</div>

<label class="button scan" for="cameraInput">
    📷<br><br>Scan a Part<br>
    <small>Use Camera</small>
</label>

<input
    id="cameraInput"
    type="file"
    accept="image/*"
    capture="environment"
    style="display:none"
    onchange="showScan(event)"
>

<script>
function showScan(event) {
    const file = event.target.files[0];

    if (file) {
        const url = URL.createObjectURL(file);

        document.body.innerHTML = `
            <div style="
                background:#f8f7fc;
                min-height:100vh;
                padding:25px;
                font-family:Arial;
                box-sizing:border-box;
            ">
                <h2>← Scan a Part</h2>

                <div style="
                    background:white;
                    padding:20px;
                    border-radius:25px;
                    text-align:center;
                ">
                    <h2>Part Photo</h2>

                    <img src="${url}" style="
                        width:100%;
                        max-height:400px;
                        object-fit:contain;
                        border-radius:20px;
                        background:#eeeef3;
                    ">

                    <p style="font-size:18px;margin-top:20px;">
                        📷 Photo captured successfully!
                    </p>

                    <button onclick="location.href='/'"
                    style="
                        width:100%;
                        border:0;
                        background:#5142df;
                        color:white;
                        padding:18px;
                        border-radius:15px;
                        font-size:20px;
                    ">
                        Back to Home
                    </button>
                </div>
            </div>
        `;
    }
}
</script>

    <div class="button manual">➕<br><br>Add Manually<br>
    <small>Select from list</small></div>
</div>

<div class="section">Your Parts</div>

<div class="parts">
    <div class="part"><div class="icon">⚙️</div>Motor</div>
    <div class="part"><div class="icon">⚫</div>Wheel</div>
    <div class="part"><div class="icon">⚙️</div>Gear</div>
    <div class="part"><div class="icon">🔴</div>LED</div>
    <div class="part"><div class="icon">🔋</div>Battery</div>
</div>

<div class="section">Suggested Builds</div>

<div class="builds">

<a href="/mini-fan" style="text-decoration:none;color:#222">
<div class="card">
    <div class="card-img">🌀</div>
    <h2>Mini Fan</h2>
    <div class="match">● 95% Match</div>
    <p>Easy · 30 min</p>
</div>
</a>

<div class="card">
    <div class="card-img">🚗</div>
    <h2>RC Car</h2>
    <div class="match">● 88% Match</div>
    <p>Medium · 2-3 hrs</p>
</div>

<div class="card">
    <div class="card-img">💡</div>
    <h2>Desk Lamp</h2>
    <div class="match">● 75% Match</div>
    <p>Easy · 45 min</p>
</div>

</div>

</div>

<div class="bottom">
    <span>🏠<br>Home</span>
    <span>🔍<br>Search</span>
    <span class="plus">+</span>
    <span>📁<br>Projects</span>
    <span>👤<br>Profile</span>
</div>

</body>
</html>
"""


MINI_FAN = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mini Fan</title>

<style>
body {
    margin: 0;
    background: #f8f7fc;
    font-family: Georgia, serif;
}

.header {
    padding: 25px;
    font-size: 22px;
}

.image {
    height: 330px;
    background: #dddde5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 150px;
}

.content {
    background: white;
    margin-top: -20px;
    border-radius: 30px 30px 0 0;
    padding: 30px;
}

h1 {
    font-size: 35px;
}

.match {
    color: #42a56c;
    font-size: 20px;
}

.info {
    display: flex;
    justify-content: space-between;
    margin: 25px 0;
}

.parts {
    display: flex;
    gap: 15px;
    overflow-x: auto;
}

.part {
    min-width: 85px;
    text-align: center;
}

.part-icon {
    background: #f2f1f6;
    padding: 18px;
    border-radius: 15px;
    font-size: 35px;
}

.start {
    display: block;
    background: #5142df;
    color: white;
    text-align: center;
    padding: 20px;
    border-radius: 15px;
    margin-top: 35px;
    font-size: 22px;
    text-decoration: none;
}
</style>
</head>

<body>

<div class="header">
    ← &nbsp; Mini Fan
</div>

<div class="image">
    🌀
</div>

<div class="content">

<h1>Mini Fan</h1>

<div class="match">● 95% Match</div>

<p>A simple table fan using DC motor and your available parts. Perfect for summer!</p>

<div class="info">
    <div>🟢<br><b>Easy</b><br>Difficulty</div>
    <div>⏱️<br><b>30 min</b><br>Time</div>
    <div>📦<br><b>6 items</b><br>Parts</div>
</div>

<h2>Parts You Need</h2>

<div class="parts">

<div class="part">
<div class="part-icon">⚙️</div>
DC Motor<br>x1
</div>

<div class="part">
<div class="part-icon">🌀</div>
Fan Blade<br>x1
</div>

<div class="part">
<div class="part-icon">🔘</div>
Switch<br>x1
</div>

<div class="part">
<div class="part-icon">🔋</div>
Battery<br>x1
</div>

<div class="part">
<div class="part-icon">〰️</div>
Wire<br>x2
</div>

<div class="part">
<div class="part-icon">▰</div>
Base<br>x1
</div>

</div>

<a class="start" href="/building">
Start Building
</a>

</div>

</body>
</html>
"""

BUILDING = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Assembly Guide</title>
</head>

<body style="background:#f8f7fc; font-family:Arial; padding:25px;">

    <h2>← Assembly Guide</h2>

    <div style="background:white; padding:25px; border-radius:25px;">

        <h2>Step 1</h2>

        <p style="font-size:20px;">
            Attach the fan blade to the motor shaft.
        </p>

        <div style="
            height:250px;
            background:#eeeef3;
            border-radius:20px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:100px;
        ">
            ⚙️🌀
        </div>

        <a href="/building/2"
           style="
           display:block;
           background:#5142df;
           color:white;
           text-align:center;
           padding:18px;
           margin-top:20px;
           border-radius:15px;
           text-decoration:none;
           ">
           Next →
        </a>

    </div>

</body>
</html>
"""
@app.route("/")
def home():
    return render_template_string(HOME)


@app.route("/mini-fan")
def mini_fan():
    return render_template_string(MINI_FAN)


@app.route("/building")
def building():
    return render_template_string(BUILDING)


@app.route("/building/2")
def building2():
    return """
    <body style="background:#f8f7fc;font-family:Arial;padding:25px">
        <h2>← Assembly Guide</h2>
        <div style="background:white;padding:25px;border-radius:25px">
            <h2>Step 2</h2>
            <p style="font-size:20px">Connect the switch to the motor.</p>
            <div style="height:250px;background:#eeeef3;border-radius:20px;
            display:flex;align-items:center;justify-content:center;font-size:80px">
            ⚙️🔘
            </div>
            <a href="/building/3"
            style="display:block;background:#5142df;color:white;text-align:center;
            padding:18px;margin-top:20px;border-radius:15px;text-decoration:none">
            Next →
            </a>
        </div>
    </body>
    """


@app.route("/building/3")
def building3():
    return """
    <body style="background:#f8f7fc;font-family:Arial;padding:25px">
        <h2>← Assembly Guide</h2>
        <div style="background:white;padding:25px;border-radius:25px">
            <h2>Step 3</h2>
            <p style="font-size:20px">Connect the battery and test the fan.</p>
            <div style="height:250px;background:#eeeef3;border-radius:20px;
            display:flex;align-items:center;justify-content:center;font-size:80px">
            🔋⚙️🌀
            </div>
            <a href="/complete"
            style="display:block;background:#5142df;color:white;text-align:center;
            padding:18px;margin-top:20px;border-radius:15px;text-decoration:none">
            Complete ✓
            </a>
        </div>
    </body>
    """


@app.route("/complete")
def complete():
    return """
    <body style="background:#f8f7fc;font-family:Arial;padding:25px;text-align:center">
        <div style="background:white;padding:40px 20px;border-radius:30px;margin-top:80px">
            <div style="font-size:90px">🎉</div>
            <h1>Build Complete!</h1>
            <p style="font-size:20px">Your Mini Fan is ready!</p>
            <a href="/"
            style="display:block;background:#5142df;color:white;padding:18px;
            border-radius:15px;text-decoration:none;margin-top:30px">
            Back to Home
            </a>
        </div>
    </body>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
