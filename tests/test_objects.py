import unittest
import a_file
import objects


class TestObjects(unittest.TestCase):
    def testing(self):
        obj1 = objects.ReadUserData("kat", "kfreeman@ithaca.edu")
        expected = {"names": ["kat"],
                    "emails": ["kfreeman@ithaca.edu"],
                    "comments": [None],
                    "likes": [None],
                    "dislikes": [None]
                    }
        obj1.organize()
        self.assertEqual(a_file.critique_data, expected)

        testing = obj1.displaying_data()
        self.assertEqual(None, testing)


class TestSearchAndSort(unittest.TestCase):        # testing here isn't as straightforward as I anticipated. I have
    # to go to the site and fill out forms and then test for those form responses/names having tests for every method
    # seemed counterintuitive when I have to go to the site anyway, so my mode of testing has been messing around
    # with the site itself to see if any problems arise
    def testing(self):
        obj1 = objects.SearchAndSort.search_for_ic_students()
        self.assertEqual(obj1, ["kfreeman@ithaca.edu"])

