from urllib import response
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_ip_info = request.remote_addr
    response = make_response(redirect("/show_info"))
    response.set_cookie("user_ip_info", user_ip_info)
    return response

@app.route("/show_info")
def show_information():
    user_ip = request.cookies.get("user_ip_info")
    return render_template("ip_information.html", user_ip=user_ip)

app.run(host="0.0.0.0", port=81, debug=True)