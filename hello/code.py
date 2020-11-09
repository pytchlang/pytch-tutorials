import pytch

class Snake(pytch.Sprite):
   Costumes = ["Snake.png"]

   def speak(self):
      self.say_for_seconds("Hello there!", 2.0)
