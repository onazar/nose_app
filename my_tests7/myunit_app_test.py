import unittest
import myunit.app
import time

class MyUnitTest(unittest.TestCase):

  def testInit(self):
    app = myunit.app.App(100)
    time.sleep(70)
    self.assertEquals(app.var, 100)

