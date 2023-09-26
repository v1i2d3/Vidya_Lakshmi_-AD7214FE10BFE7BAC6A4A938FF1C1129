
class player:
  def play(self):
    print("The player is playing cricket.")


class Batsman(player):
  def play(self):
    print("The batsman is batting.")

    
    class Bowler(player):
      def play(self):
        print("The bowler is bowling.")

        # create objects of Batsman and Bowler classes
        batsman = batsman()
        bowler = bowler()

        # call the play() method for each object
        batsman.play()
        bowler.play()
        

      
          