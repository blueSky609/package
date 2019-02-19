import unittest
from mulit import getMulit


class TestMulitConfigInterface(unittest.TestCase):
    def setUp(self):
        self.str1 = "11111111111111111111111111111"
        self.str2 = "123456789111111111111111111111"
        self.except_value = "1371742101234567901234567901219615912320987654320987654321"

    def test_multi(self):
        fsm_instance = getMulit()
        res = fsm_instance.multi(self.str1,self.str2)
        self.assertEqual(res, self.except_value)

def suite():
    suite = unittest.TestSuite()
    # 往此添加需要测试的方法testgetSize()
    suite.addTest(TestMulitConfigInterface("test_multi"))
    return suite


if __name__ == "__main__":
    # 在主函数中调用全局方法suite.
    unittest.main(defaultTest='suite')
