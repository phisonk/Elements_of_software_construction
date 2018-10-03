import Code
import unittest
class TestCode(unittest.TestCase):
    #def test_simple(self):
    #    self.assertEqual(Code.return_zero(),0)
    #def test_login(self):
    #    self.assertEqual(Code.login(),None)
    def test_verify_correct_user_password(self):
        self.assertEqual(Code.verify('phison','gg'),1)
    def test_verify_correct_user_incorrect_password(self):
        self.assertEqual(Code.verify('phison','ggg'),0)
    def test_verify_incorrect_user_correct_password(self):
        self.assertEqual(Code.verify('phisonk','gg'),0)
    def test_verify_incorrect_user_incorrect_password(self):
        self.assertEqual(Code.verify('phisonk','gggg'),0)

if __name__ == '__main__':
    unittest.main()
