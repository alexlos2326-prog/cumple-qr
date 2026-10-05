from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¡Feliz Cumpleaños Scarlet!</title>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background-color: #fce4ec;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: #ffffff;
            padding: 30px 20px;
            border-radius: 16px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            max-width: 360px;
            width: 100%;
            text-align: center;
        }

        h1 {
            color: #d81b60;
            font-size: 22px;
            margin-bottom: 15px;
        }

        p {
            color: #444444;
            font-size: 16px;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        .btn {
            display: block;
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            font-size: 15px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        .btn-yes {
            background-color: #e91e63;
            color: white;
        }

        .btn-no {
            background-color: #e0e0e0;
            color: #333333;
        }

        .hidden {
            display: none;
        }
    </style>
</head>
<body>

    <!-- Paso 1: Pregunta Inicial -->
    <div id="step-1" class="container">
        <h1>Hola Scarlet 👋</h1>
        <p>Antes de ver tu regalo, responde esto:<br><strong>¿Te caigo bien?</strong></p>
        <button class="btn btn-yes" onclick="showOption('yes')">Sí, me caes bien ❤️</button>
        <button class="btn btn-no" onclick="showOption('no')">No te caigo bien 😅</button>
    </div>

    <!-- Paso 2: Opción "No me caes bien" -->
    <div id="step-no" class="container hidden">
        <h1>🤪 ¡No me importa!</h1>
        <p>Igual me caes super bien tú, Scarlet. Así que aquí tienes tu mensaje de todos modos:</p>
        <button class="btn btn-yes" onclick="showBirthday()">Ver mi mensaje 🎁</button>
    </div>

    <!-- Paso 3: Mensaje Final de Cumpleaños -->
    <div id="step-birthday" class="container hidden">
        <h1>🎉 ¡Feliz Cumpleaños, Scarlet! 🎂</h1>
        <p>Te deseo un día muy especial, lleno de momentos bonitos y mucha alegría.</p>
        <p>¡Espero que la pases increíble hoy y siempre! Se que ya paso hace varios dias pero igual
        te deseo lo mejor ya que eres una personita que ya es especial para mi✨</p>
    </div>

    <script>
        function showOption(option) {
            document.getElementById('step-1').classList.add('hidden');
            if (option === 'yes') {
                showBirthday();
            } else {
                document.getElementById('step-no').classList.remove('hidden');
            }
        }

        function showBirthday() {
            document.getElementById('step-no').classList.add('hidden');
            document.getElementById('step-birthday').classList.remove('hidden');
            
            // Lluvia de confeti
            confetti({
                particleCount: 80,
                spread: 60,
                origin: { y: 0.6 }
            });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
