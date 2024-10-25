from flask import Flask, render_template, redirect
import random

app = Flask('')

@app.route("/")
def home():
  global aleatorio
  with open("contas.txt") as f:
    liness = [line.rstrip('\n') for line in f]
  aleatorio = str(random.choice(liness))
  return render_template("home.html", conta=aleatorio)

@app.route("/deletar_conta/", methods=['POST'])
def deletarconta():
  with open("contas.txt", "r") as w:
    lines =  w.readlines()
  with open("users.txt", "w") as w:
    for line in lines:
      if aleatorio not in line:
          w.write(line)
  return redirect("https://generatorcontasx.onrender.com/")

@app.route("/nova_conta/", methods=['POST'])
def novaconta():
  return redirect("https://generatorcontasx.onrender.com/")

if __name__ == '__main__':
  app.run(debug=True)
