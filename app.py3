from flask import Flask, render_template_string

app = Flask(Para scarlet)

# Código HTML, CSS y JavaScript todo en uno
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¡Feliz Cumpleaños!</title>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .card {
            background: white;
            padding: 30px 25px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            max-width: 400px;
            width: 100%;
            text-align: center;
            animation: fadeIn 0.5s ease-in-out;
        }

        h1 {
            color: #4a4a4a;
            font-size: 24px;
            margin-bottom: 20px;
        }

        .buttons {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 20px;
        }

        button {
            padding: 14px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
        }

        button:active {
            transform: scale(0.98);
        }

        .btn-yes {
            background-color: #ff6b81;
            color: white;
        }

        .btn-no {
            background-color: #e0e0e0;
            color: #555;
        }

        .hidden {
            display: none;
        }

        .message-box {
            line-height: 1.6;
            color: #333;
            font-size: 16px;
        }

        .emoji {
            font-size: 40px;
            margin-bottom: 10px;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <!-- Pantalla 1: La Pregunta Inicial -->
    <div id="step-question" class="card">
        <div class="emoji">👀</div>
        <h1>Una pregunta rápida...<br>¿Te caigo bien?</h1>
        <div class="buttons">
            <button class="btn-yes" onclick="selectOption('yes')">¡Sí, me caes bien! ❤️</button>
            <button class="btn-no" onclick="selectOption('no')">No te caigo bien 😅</button>
        </div>
    </div>

    <!-- Pantalla 2: Opción "No te caigo bien" -->
    <div id="step-no" class="card hidden">
        <div class="emoji">🤪</div>
        <h1>¡No me importa, igual me caes bien tú!</h1>
        <p style="margin-bottom: 20px; color: #666;">Y como hoy es un día especial, igual tienes tu mensaje:</p>
        <button class="btn-yes" onclick="showBirthdayMessage()">Ver mi mensaje de todos modos 🎁</button>
    </div>

    <!-- Pantalla 3: Mensaje Final de Cumpleaños -->
    <div id="step-birthday" class="card hidden">
        <div class="emoji">🎉🎂✨</div>
        <h1 style="color: #ff6b81;">¡FELIZ CUMPLEAÑOS!</h1>
        <div class="message-box">
            <p>¡Espero que tengas un día increíble rodeado de mucha alegría, risas y buena comida!</p>
            <br>
            <p>Gracias por ser una persona tan especial. Te deseo lo mejor en este nuevo año de vida. se te quiere un monton</p>
        </div>
    </div>

    <script>
        function selectOption(option) {
            document.getElementById('step-question').classList.add('hidden');
            if (option === 'yes') {
                triggerConfetti();
                document.getElementById('step-birthday').classList.remove('hidden');
            } else {
                document.getElementById('step-no').classList.remove('hidden');
            }
        }

        function showBirthdayMessage() {
            triggerConfetti();
            document.getElementById('step-no').classList.add('hidden');
            document.getElementById('step-birthday').classList.remove('hidden');
        }

        function triggerConfetti() {
            confetti({
                particleCount: 100,
                spread: 70,
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
