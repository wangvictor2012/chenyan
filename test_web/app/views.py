from app import app
from flask import Flask, redirect, url_for, render_template, request, send_from_directory


@app.route('/')
def index():
    return render_template('index.html');

