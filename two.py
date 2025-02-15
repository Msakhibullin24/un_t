import unittest
from unittest.mock import Mock


class CreditCard:  # Класс карты
    def charge(self, amount):
        # Тут типа списываются деньги.
        if amount > 1000:  # Простое ограничение для примера
            raise ValueError("Слишком много!")
        return True  # Типа списалось


class PaymentForm:  # Класс формы
    def __init__(self, card):
        self.card = card

    def pay(self, amount):
        try:
            self.card.charge(amount)  # Вызываем метод карты
            return "Оплачено!"  # Если всё ок
        except ValueError as e:
            return f"Ошибка: {e}"  # Если ошибка


class TestPayment(unittest.TestCase):  # Тесты

    def test_pay_ok(self):
        mock_card = Mock()  # Создаём мок-объект
        mock_card.charge.return_value = True # говорим что charge возвращает
        form = PaymentForm(mock_card)  # Форма с мок-картой
        result = form.pay(10)  # Платим
        self.assertEqual(result, "Оплачено!")  # Проверяем
        mock_card.charge.assert_called_with(10)  # Проверяем, что charge вызвали

    def test_pay_fail(self):
        mock_card = Mock()
        mock_card.charge.side_effect = ValueError("Нельзя!")  # Типа ошибка
        form = PaymentForm(mock_card)
        result = form.pay(2000)
        self.assertEqual(result, "Ошибка: Нельзя!")
        mock_card.charge.assert_called_with(2000)
    def test_another_fail(self):
        card_mock = Mock()
        card_mock.charge.side_effect = ValueError("Недостаточно!")
        form = PaymentForm(card_mock)

        result = form.pay(50)
        self.assertEqual(result,"Ошибка: Недостаточно!")
        card_mock.charge.assert_called_with(50)

if __name__ == '__main__':
    unittest.main()