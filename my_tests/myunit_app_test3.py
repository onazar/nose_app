import unittest
import myunit.app

class MyUnitTest(unittest.TestCase):

  def testInit(self):
    app = myunit.app.App(100)
    self.assertEquals(app.var, 100)

