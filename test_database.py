import unittest
import pymongo

class TestPromotion(unittest.TestCase):
    def test_increase_votes(self):
        collection = pymongo.MongoClient().db.collection
        objects = [
    {"Product Code": "CH1", "Name": "Chai", "Price": 3.11},
    {"Product Code": "AP1", "Name": "Apples", "Price": 6.00},
    {"Product Code": "CF1", "Name": "Coffee", "Price": 11.23},
    {"Product Code": "MK1", "Name": "Milk", "Price": 4.75},
    {"Product Code": "OM1", "Name": "Oatmeal", "Price": 3.69}]

        for obj in objects:
            obj['_id'] = collection.insert_one(obj)
        stored_obj = collection.find_one({'Name': "Chai"})
        self.assertEqual( stored_obj["Price"] , 3.11)
        collection.remove({})

if __name__ == "__main__":
    unittest.main()