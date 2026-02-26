from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>NGINX Info</title>

<style>
    body {
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(120deg, #1f4037, #99f2c8);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        color: #333;
    }

    .container {
        background: white;
        width: 800px;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        animation: fadeIn 1s ease;
    }

    h1 {
        text-align: center;
        color: #1f4037;
        margin-bottom: 20px;
    }

    p {
        line-height: 1.7;
        margin-bottom: 15px;
    }

    .highlight {
        background: #e8f8f5;
        padding: 15px;
        border-left: 5px solid #1f4037;
        border-radius: 8px;
        margin-top: 20px;
    }

    footer {
        text-align: center;
        margin-top: 25px;
        color: #777;
        font-size: 14px;
    }

    @keyframes fadeIn {
        from {opacity:0; transform: translateY(20px);}
        to {opacity:1; transform: translateY(0);}
    }
</style>
</head>

<body>

<div class="container">
    <h1>🚀 NGINX Server Overview</h1>

    <p>
        NGINX is a high-performance web server and reverse proxy server widely used to handle large amounts
        of traffic efficiently. It can serve static content, manage load balancing, and act as an API gateway
        in microservices architectures.
    </p>

    <p>
        One of the main reasons developers prefer NGINX is its event-driven architecture, which allows it
        to handle thousands of connections simultaneously with low resource consumption.
    </p>

    <div class="highlight">
        <strong>Key Uses:</strong>
        <ul>
            <li>Reverse proxy for backend services</li>
            <li>Load balancing across servers</li>
            <li>Serving static files</li>
            <li>SSL termination</li>
        </ul>
    </div>

    <footer>
        Flask Demo • DevOps Learning
    </footer>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)