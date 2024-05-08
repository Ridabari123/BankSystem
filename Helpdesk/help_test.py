import unittest
from PyQt5.QtWidgets import QApplication
from help import HelpdeskWidget

class TestHelpdeskWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_toggle_answer(self):
        # Create an instance of HelpdeskWidget
        helpdesk_widget = HelpdeskWidget()

        # Test toggling the visibility of answers
        for index in range(len(helpdesk_widget.question_buttons)):
            # Initially, answer should be hidden
            self.assertTrue(helpdesk_widget.answer_texts[index].isHidden())

            # Click the question button
            helpdesk_widget.toggle_answer(index)

            # After clicking, answer should be visible
            self.assertFalse(helpdesk_widget.answer_texts[index].isHidden())

            # Click the question button again
            helpdesk_widget.toggle_answer(index)

            # After clicking again, answer should be hidden
            self.assertTrue(helpdesk_widget.answer_texts[index].isHidden())

    def tearDown(self):
        self.app.quit()

if __name__ == '__main__':
    unittest.main()
