import unittest
from chatbot import ChatbotAI

class TestChatbotAI(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatbotAI("TestBot")

    def test_greet(self):
        expected_greeting = "Bonjour ! Je suis TestBot, votre chatbot IA préféré."
        self.assertEqual(self.chatbot.greet(), expected_greeting)

    def test_generate_response(self):
        user_input = "Bonjour"
        response = self.chatbot.generate_response(user_input)
        self.assertIn(response, self.chatbot.responses)

    def test_joke(self):
        joke = self.chatbot.joke()
        self.assertIn(joke, self.chatbot.jokes)

    def test_calculate_expression(self):
        expression = "2 + 2"
        expected_result = "Le résultat du calcul 2 + 2 est 4"
        self.assertEqual(self.chatbot.calculate_expression(expression), expected_result)

        expression = "10 / 0"
        expected_result = "Erreur : division par zéro !"
        self.assertEqual(self.chatbot.calculate_expression(expression), expected_result)

if __name__ == '__main__':
    unittest.main()
