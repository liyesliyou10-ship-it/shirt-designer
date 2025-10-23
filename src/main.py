from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Shirt Designer</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f5f5f5;
                    margin-top: 40px;
                }
                button {
                    padding: 10px 20px;
                    margin: 10px;
                    font-size: 16px;
                    border: none;
                    background-color: #007BFF;
                    color: white;
                    border-radius: 8px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
                form {
                    background-color: white;
                    display: inline-block;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    margin-top: 30px;
                }
                input, select {
                    margin: 10px;
                    padding: 8px;
                    width: 80%;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                }
                .price {
                    font-size: 20px;
                    color: green;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Shirt Designer!</h1>
            <p>Customize your shirt and order it anywhere in Algeria 🇩🇿</p>

            <div>
                <button onclick="alert('Start Designing coming soon!')">Start Design</button>
                <button onclick="alert('Contact us at shirt-designer@wasmer.app')">Contact Us</button>
            </div>

            <form method="post" action="/order">
                <h3>Order Form</h3>
                <input type="text" name="name" placeholder="Full Name" required><br>
                <input type="tel" name="phone" placeholder="Phone Number" required><br>
                <select name="wilaya" required>
                    <option value="">Select Wilaya</option>
                    <option value="Algiers">Algiers</option>
                    <option value="Oran">Oran</option>
                    <option value="Constantine">Constantine</option>
                    <option value="Annaba">Annaba</option>
                    <option value="Blida">Blida</option>
                </select><br>
                <div class="price">Price: 2500 DZD</div>
                <button type="submit">Place Order</button>
            </form>
        </body>
    </html>
    """

@app.post("/order", response_class=HTMLResponse)
def order(name: str = Form(...), phone: str = Form(...), wilaya: str = Form(...)):
    return f"""
    <html>
        <head><title>Order Confirmed</title></head>
        <body style='text-align:center; font-family:sans-serif;'>
            <h2>Thank you, {name}!</h2>
            <p>Your order has been received.</p>
            <p>We’ll contact you at <b>{phone}</b> and deliver to <b>{wilaya}</b>.</p>
            <p>Total Price: <b>2500 DZD</b></p>
            <a href="/">← Go back</a>
        </body>
    </html>
    """

