from flask import Flask,request,render_template,flash
from pathlib import Path
import discord
import requests

app = Flask(
	__name__,
	template_folder=Path(__file__).parent)

@app.route('/',methods=["GET","POST"])
def index():
	if request.method == "POST":
		url = request.form["url"]
		name = request.form["name"]
		avatar = request.form["avatar"]
		message = request.form["message"]
		webhook = discord.Webhook.from_url(
			url,
			adapter=discord.RequestsWebhookAdapter())
		webhook.send(
			message,
			username=name,
			avatar_url=avatar)
		flash("Webhook Sent!")
		
	return render_template("index.html")

if __name__ == "__main__":
	app.secret_key = "secret123"
	app.run(
	host='0.0.0.0',
	port=8080)