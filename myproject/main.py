from flask import Flask, render_template_string

app = Flask(__name__)

HOME = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DIY Builder</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#f6f5fa;font-family:Arial;color:#222}
.container{max-width:500px;margin:auto;padding:25px 25px 100px}
h1{font-size:28px;margin-bottom:5px}
.sub{color:#777;margin-bottom:25px}
.search{background:white;padding:17px;border-radius:18px;color:#999;margin-bottom:18px}
.buttons{display:flex;gap:12px}
.btn{flex:1;padding:17px;border-radius:16px;text-align:center;text-decoration:none;font-weight:bold}
.scan{background:#5142df;color:white}
.manual{background:white;color:#333}
h2{margin-top:30px}
.parts{display:flex;gap:12px;overflow-x:auto}
.part{min-width:115px;background:white;padding:18px;border-radius:20px;text-align:center}
.icon{font-size:45px;margin-bottom:10px}
.build{background:white;padding:20px;border-radius:22px;margin-bottom:15px}
.build-icon{text-align:center;font-size:70px}
.build-btn{display:block;background:#5142df;color:white;padding:16px;border-radius:15px;text-align:center;text-decoration:none;margin-top:15px}
nav{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #ddd;display:flex;justify-content:space-around;padding:14px}
nav div{text-align:center;color:#777;font-size:13px}
</style>
</head>
<body>

<div class="container">

<h1>Hi, Builder 👋</h1>
<div class="sub">Let's build something amazing today.</div>

<div class="search">🔍 Search parts...</div>

<div class="buttons">
<a class="btn scan" href="#">📷 Scan a Part</a>
<a class="btn manual" href="#">＋ Add Manually</a>
</div>

<h2>Your Parts</h2>

<div class="parts">
<div class="part"><div class="icon">⚙️</div>Motor</div>
<div class="part"><div class="icon">🛞</div>Wheel</div>
<div class="part"><div class="icon">⚙️</div>Gear</div>
<div class="part"><div class="icon">💡</div>LED</div>
<div class="part"><div class="icon">🔋</div>Battery</div>
</div>

<h2>Suggested Builds</h2>

<div class="build">
<div class="build-icon">🌀</div>
<h3>Mini Fan</h3>
<p>Simple motor powered mini fan.</p>
<a class="build-btn" href="/mini-fan">View Build →</a>
</div>

<div class="build">
<div class="build-icon">🚗</div>
<h3>RC Car</h3>
<p>Build your own remote car.</p>
<a class="build-btn" href="#">Coming Soon</a>
</div>

<div class="build">
<div class="build-icon">💡</div>
<h3>Desk Lamp</h3>
<p>Simple LED desk lamp.</p>
<a class="build-btn" href="#">Coming Soon</a>
</div>

</div>

<nav>
<div>🏠<br>Home</div>
<div>🔍<br>Search</div>
<div>📁<br>Projects</div>
<div>👤<br>Profile</div>
</nav>

</body>
</html>
"""


DETAIL = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mini Fan</title>
<style>
body{margin:0;background:#f6f5fa;font-family:Arial}
.container{max-width:500px;margin:auto;padding:25px}
.back{color:#333;text-decoration:none;font-size:18px}
.box{background:white;border-radius:25px;padding:25px;margin-top:20px}
.hero{text-align:center;font-size:110px}
h1{font-size:30px}
.part{background:#f1f0f6;padding:15px;border-radius:15px;margin:10px 0}
.start{display:block;background:#5142df;color:white;text-align:center;padding:18px;border-radius:15px;text-decoration:none;font-weight:bold;margin-top:25px}
</style>
</head>
<body>
<div class="container">

<a class="back" href="/">← Back</a>

<div class="box">
<div class="hero">🌀</div>

<h1>Mini Fan</h1>

<p>
Build a small working fan using simple electronic parts.
</p>

<h3>Required Parts</h3>

<div class="part">⚙️ DC Motor</div>
<div class="part">🌀 Fan Blade</div>
<div class="part">🔋 Battery</div>
<div class="part">🔌 Wires</div>

<a class="start" href="/building">Start Building →</a>

</div>
</div>
</body>
</html>
"""


STEP1 = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Step 1</title>
<style>
body{margin:0;background:#f6f5fa;font-family:Arial}
.container{max-width:500px;margin:auto;padding:25px}
.box{background:white;border-radius:25px;padding:25px}
.visual{height:250px;background:#eeeef3;border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:90px;margin:20px 0}
.next{display:block;background:#5142df;color:white;text-align:center;padding:18px;border-radius:15px;text-decoration:none}
</style>
</head>
<body>
<div class="container">

<a href="/mini-fan">← Back</a>

<div class="box">
<p>Assembly Guide</p>
<h1>Step 1</h1>

<h2>Attach the fan blade</h2>

<p>
Push the fan blade onto the motor shaft carefully.
</p>

<div class="visual">⚙️🌀</div>

<a class="next" href="/building/2">Next →</a>
</div>

</div>
</body>
</html>
"""


STEP2 = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Step 2</title>
<style>
body{margin:0;background:#f6f5fa;font-family:Arial}
.container{max-width:500px;margin:auto;padding:25px}
.box{background:white;border-radius:25px;padding:25px}
.visual{height:250px;background:#eeeef3;border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:80px;margin:20px 0}
.next{display:block;background:#5142df;color:white;text-align:center;padding:18px;border-radius:15px;text-decoration:none}
</style>
</head>
<body>
<div class="container">

<a href="/building">← Back</a>

<div class="box">
<p>Assembly Guide</p>
<h1>Step 2</h1>

<h2>Connect the battery</h2>

<p>
Connect the motor wires to the battery terminals.
</p>

<div class="visual">🔋🔌⚙️</div>

<a class="next" href="/building/3">Next →</a>
</div>

</div>
</body>
</html>
"""


STEP3 = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Step 3</title>
<style>
body{margin:0;background:#f6f5fa;font-family:Arial}
.container{max-width:500px;margin:auto;padding:25px}
.box{background:white;border-radius:25px;padding:25px;text-align:center}
.visual{height:250px;background:#eeeef3;border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:90px;margin:20px 0}
.done{display:block;background:#5142df;color:white;text-align:center;padding:18px;border-radius:15px;text-decoration:none}
</style>
</head>
<body>
<div class="container">

<div class="box">

<p>Assembly Guide</p>

<h1>Step 3</h1>

<h2>Test your Mini Fan</h2>

<p>
Turn on the battery and check that the fan is spinning.
</p>

<div class="visual">🔋🌀</div>

<a class="done" href="/complete">Finish Build ✓</a>

</div>

</div>
</body>
</html>
"""


COMPLETE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Complete</title>
<style>
body{margin:0;background:#f6f5fa;font-family:Arial}
.container{max-width:500px;margin:auto;padding:25px}
.box{background:white;border-radius:25px;padding:35px;text-align:center;margin-top:40px}
.icon{font-size:100px}
.home{display:block;background:#5142df;color:white;padding:18px;border-radius:15px;text-decoration:none;margin-top:25px}
</style>
</head>
<body>

<div class="container">

<div class="box">

<div class="icon">🎉🌀</div>

<h1>Build Complete!</h1>

<p>
Congratulations! Your Mini Fan is ready.
</p>

<p>
You successfully completed all 3 steps.
</p>

<a class="home" href="/">Back to Home</a>

</div>

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME)


@app.route("/mini-fan")
def mini_fan():
    return render_template_string(DETAIL)


@app.route("/building")
def building():
    return render_template_string(STEP1)


@app.route("/building/2")
def building2():
    return render_template_string(STEP2)


@app.route("/building/3")
def building3():
    return render_template_string(STEP3)


@app.route("/complete")
def complete():
    return render_template_string(COMPLETE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
