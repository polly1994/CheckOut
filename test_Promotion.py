import unittest
from unittest.mock import MagicMock, patch
import unittest.mock
import promotion
import setup


class TestPromotion(unittest.TestCase):

    # get_input will return 'yes' during this test
    def setUp(self):
        self.promo = promotion.Promotion("CH1", "MK1", 1, 1, "CHMK", "UpdatePrice", 1, 4.75, 4.75)

        self.mock_numberitem = unittest.mock.patch.object(
            setup, 'GetNumber', return_value=2
        )

    def test_ConvPercentFloat(self):
        discount = self.promo.ConvPercentFloat("40%", 4)
        print (type(discount))
        self.assertEqual(discount,1.6)

    def test_LimitationBool_True(self):
        boo = self.promo.LimitationBool( 0)
        self.assertEqual(True, boo)

    def test_LimitationBool_False(self):
        boo = self.promo.LimitationBool(3)
        self.assertEqual(False, boo)

    def test_PromoApplys_NoApplyItemBought1(self):
        boo = self.promo.PromoApplys("CH1",1)
        self.assertEqual(False, boo)

    def test_PromoApplys_NoApplyItemBought2(self):
        boo = self.promo.PromoApplys("CH1",3)
        self.assertEqual(False, boo)

    # have bought 5 MK1, buy 3th CH1 now, return False because promotion has applied
    def test_PromoApplys_BoughtPreItem1(self):
        with unittest.mock.patch.object(setup, 'GetNumber', return_value=4):
            boo = self.promo.PromoApplys("CH1", 3)
            self.assertEqual(False, boo)

    # bought 1 milk, and 4 ch1
    def test_PromoApplys_BoughtApplyItem3(self):
        with unittest.mock.patch.object(setup, 'GetNumber', return_value=4):
            boo = self.promo.PromoApplys("MK1", 1)
            self.assertEqual(True, boo)

    # buy 1 MK1, but haven't bought CH1
    def test_PromoApplys_BoughtApplyItem2(self):
        with unittest.mock.patch.object(setup, 'GetNumber', return_value=0):
            boo = self.promo.PromoApplys("MK1", 2)
            self.assertEqual(False, boo)

    # didn't get the number of the item, return False
    def test_PromoApplys_BoughtApplyItem8(self):
        with unittest.mock.patch.object(setup, 'GetNumber'):
            boo = self.promo.PromoApplys("MK1", 2)
            self.assertEqual(False, boo)

    # discount doesn't apply to the pre_item
    def test_discount_NoDiscount(self):
        with unittest.mock.patch.object(promotion.Promotion, "PromoApplys", return_value = True):
            result = self.promo.discount("CH1", 1)
            self.assertEqual((0, ''), result)

    # discount applys to the apply_item if the number is 1
    def test_discount_NoDiscount(self):
        with unittest.mock.patch.object(promotion.Promotion, "PromoApplys", return_value = True):
            result = self.promo.discount("MK1", 1)
            self.assertEqual((-4.75, 'CHMK'), result)

    # discount applys to the apply_item if the number is 1
    def test_discount_NoDiscount(self):
        with unittest.mock.patch.object(promotion.Promotion, "PromoApplys", return_value = False):
            result = self.promo.discount("MK1", 3)
            self.assertEqual((0, ''), result)

if __name__ == "__main__":
    unittest.main()
