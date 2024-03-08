import re
import random

class ChatbotAI:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Bonjour ! Je suis {self.name}, votre chatbot IA préféré."

    def generate_response(self, user_input):
        responses = [
            "Je suis désolé, je ne comprends pas.",
            "Pouvez-vous reformuler votre question s'il vous plaît ?",
            "Intéressant... Pourriez-vous en dire plus ?",
            "Hmm, laissez-moi y réfléchir un instant...",
            "C'est une question complexe, mais je vais faire de mon mieux pour y répondre !"
        ]
        return random.choice(responses)

    def joke(self):
        jokes = [
            "Pourquoi les ordinateurs ont-ils toujours froid ? Parce qu’ils ont le ventirad.",
            "Qu'est-ce qu'un algorithme? C'est un mot arabe, cela signifie : 'Tu as oublié un point-virgule'.",
            "Pourquoi les développeurs détestent-ils Noël ? Parce qu'il y a trop de branches dans l'arbre."
        ]
        return random.choice(jokes)

    def calculate_expression(self, expression):
        reponse = f"Le résultat du calcul {expression} est "
        match = re.match(r'(\d+)\s*([-+*/])\s*(\d+)', expression)
        if match:
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))
            if operator == '+':
                return reponse +str(num1 + num2)
            elif operator == '-':
                return reponse +str(num1 - num2)
            elif operator == '*':
                return reponse +str(num1 * num2)
            elif operator == '/':
                if num2 != 0:
                    return reponse +str(num1 / num2)
                else:
                    return "Erreur : division par zéro !"
        else:
            return "Expression mathématique invalide."

# Exemple d'utilisation :
chatbot = ChatbotAI("ChatGPT")
print(chatbot.calculate_expression("3+5"))
print(chatbot.calculate_expression("5-9"))
print(chatbot.calculate_expression("8*7"))
print(chatbot.calculate_expression("10/2"))
print(chatbot.calculate_expression("5/0"))
