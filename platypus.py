from cs1graphics import*
from time import sleep

''' Perry the platypus class with various perry the platypus abilities'''

class Platypus(Layer):

    def __init__(self, skin = 'darkcyan'):
        '''
        Initialization of the platypus
        '''
        super().__init__() #inherits from Layer() class

        self._pet = True # for switching between pet and agent
        self._gone = False # for dissapearing
        self._trapped = False # for getting trapped

        # code for platypus legs
        flipperNormal = ClosedSpline(Point(0,0), Point(.4,1), Point(1,1.4),
                                     Point(2.1,2), Point(4,1.8), Point(5.2,1),
                                     Point(6,0), Point(5.5,-1), Point(5,-1.5),
                                     Point(4,-1.3), Point(3,-1), Point(1,-.6),
                                     Point(0,0))
        flipperNormal.setFillColor('orange')
        flipperNormal.setBorderWidth(.2)
        flipperNormal.move(.8,8)
        flipperNormal.scale(.8)
        flipperNormal1 = flipperNormal.clone()
        flipperNormal1.move(5,.8)
        
        self._leg1 = ClosedSpline(Point(0,0), Point(.4,1), Point(.5,1.5),
                            Point(0,1.6), Point(.2,2), Point(.5,2),
                            Point(.7,1.5), Point(.9,1.1), Point(1,1),
                            Point(1,0), Point(0,0))
        self._leg1.setFillColor(skin)
        self._leg1.move(-6,5)
        self._leg1.setBorderWidth(.1)
        self._leg1.scale(2.2)
        self._leg2 = self._leg1.clone()
        self._leg2.scale(1.4)
        self._leg2.move(3,-1)
        self._leg3 = Ellipse(2,6)
        self._leg3.setFillColor(skin)
        self._leg3.setBorderWidth(.2)
        self._leg3.move(4,5)
        self._leg4 = Ellipse(2,7)
        self._leg4.setFillColor(skin)
        self._leg4.setBorderWidth(.2)
        self._leg4.move(9,5)
        self._leg4.rotate(-5)
        self._normallegs = Layer()
        self._normallegs.add(flipperNormal)
        self._normallegs.add(flipperNormal1)
        self._normallegs.add(self._leg1)
        self._normallegs.add(self._leg2)
        self._normallegs.add(self._leg3)
        self._normallegs.add(self._leg4)
        self.add(self._normallegs)

        # Platypus body
        self._bodyNormal = Rectangle(20,10)
        self._bodyNormal.setFillColor(skin)
        self._bodyNormal.setBorderWidth(.5)
        self.add(self._bodyNormal)
        
        #Platypus eyes
        self._normalEyes = Layer()
        leftEye = Ellipse(4,2.5)
        leftEye.setFillColor('white')
        leftEye.move(-10,-2)
        leftEye.setBorderWidth(.4)
        rightEye = leftEye.clone()
        rightEye.move(5,.2)
        leftPupil = Ellipse(1,.8)
        leftPupil.setFillColor('black')
        leftPupil.move(-10.5,-2.2)
        rightPupil = leftPupil.clone()
        rightPupil.move(5,.2)
        self._normalEyes.add(leftEye)
        self._normalEyes.add(rightEye)
        self._normalEyes.add(rightPupil)
        self._normalEyes.add(leftPupil)
        self.add(self._normalEyes)

        # Platypus hair
        self._hair = Spline(Point(0,0), Point(2,1), Point(3,4),
                          Point(2,3), Point(.5,2), Point(2,3),
                          Point(3,4), Point(3.5,2), Point(3.1,.5))
        self._hair.setBorderWidth(.5)
        self._hair.move(-8.2,-9)
        self.add(self._hair)

        # Mouth used for both platypus and agent versions
        mouthShape = ClosedSpline(Point(0,0), Point(.7,1), Point(2,3),
                                         Point(3,4), Point(4,5), Point(5.3,5.8),
                                         Point(5.2,7), Point(4,7.3), Point(2,7.4),
                                         Point(0,7), Point(-1,6), Point(-2,6),
                                  Point(-4,6.2), Point(-6.6,6), Point(-6.5,5),
                                  Point(-6,4), Point(-4,4), Point(-2,4.2),
                                  Point(-.5,4.3), Point(-.8,3), Point(-.7,2),
                                  Point(-.5,1), Point(0,0))
        mouthShape.setFillColor('orange')
        mouthShape.setBorderWidth(.4)
        mouthLine = Path(Point(-1,6), Point(-1,5.9),Point(0,5.5), Point(2,5.6), Point(3.5,6))
        mouthLine.setBorderWidth(.5)
        self._mouth = Layer()
        self._mouth.add(mouthShape)
        self._mouth.add(mouthLine)
        self._mouth.scale(.8)
        self._mouth.move(-8,-1)
        self._mouth.setDepth(49)
        self.add(self._mouth)

        # tail used for both platypus and agent version
        self._tail = Layer()
        paddleshape = ClosedSpline(Point(0,0), Point(0,2.5), Point(2,3),
                                   Point(4,4), Point(5,4.5), Point(7,6),
                                   Point(8,6.1), Point(9,5.5), Point(9.5,5),
                                   Point(10.1,4), Point(10.5,2),Point(10.2,1),
                                   Point(10,0), Point(9,-.5),Point(6,-1),
                                   Point(4,-.9), Point(2,-.7), Point(1,-.3),
                                   Point(0,0))
        paddleshape.setFillColor('sandybrown')
        paddleshape.setBorderWidth(.4)
        paddleshape.move(10,0)
        self._tail.add(paddleshape)
        tailWebbing = Spline(Point(.5,-.1), Point(1,.8), Point(1.1,2),
                             Point(1.1,2.6), Point(2,2), Point(3,1.2),
                             Point(4,.3), Point(4.2,0), Point(4.8,-1),
                             Point(5.1,0), Point(5.5,1), Point(5.6,2),
                             Point(5.6,3), Point(5.6,4), Point(5.4,4.8),
                             Point(6,4.2), Point(7,3.4), Point(8,2.3),
                             Point(9,1.2), Point(9.5,0))
        tailWebbing.move(10,0)
        tailWebbing.setBorderWidth(.6)
        tailWebbing1 = tailWebbing.clone()
        tailWebbing1.move(10,0)
        tailWebbing1.flip()
        self._tail.add(tailWebbing1)
        self._tail.add(tailWebbing)
        self._tail.setDepth(55)
        self.add(self._tail)

        # Hat for agent version
        self._hat = Layer()
        hatshape = ClosedSpline(Point(0,0), Point(.2,-1), Point(.7,-2),
                                 Point(1.1,-3), Point(2,-3),Point(3,-2.6),
                                 Point(4,-1.8), Point(4.5,-1.5), Point(5,-1.7),
                                 Point(6,-1.8), Point(6.3,-1), Point(6.5,0),
                                 Point(7,.5), Point(8,.7), Point(8.7,1),
                                 Point(8,2), Point(7,3), Point(6.6,2), Point(6,1),
                                 Point(5,1), Point(3,1.2), Point(2,1.5), Point(1,1.8),
                                 Point(0,1.9), Point(-2,1.8), Point(-3,1.4),
                                 Point(-3.9,1), Point(-2,.8), Point(-1,.6), Point(0,0))
        hatshape.setFillColor('brown4')
        hatshape.setBorderWidth(.5)
        hatband = ClosedSpline(Point(0,0), Point(1,.2), Point(2,.5),
                               Point(3,.8), Point(3.4,1.2), Point(5,1),
                               Point(6,.6), Point(7,.5),Point(6,-.1),
                               Point(5,-.7), Point(4,-1), Point(3,-1.1),
                               Point(2,-1.4), Point(1,-1.5), Point(.4,-1.6))
        hatband.setFillColor('black')
        hatband.setBorderWidth(0)
        self._hat.add(hatshape)
        self._hat.add(hatband)
        self._hat.move(-3,-10)

        self._agentBody = Rectangle(6.5,18)
        self._agentBody.setFillColor(skin)
        self._agentBody.setBorderWidth(.5)
        
        # agent eyes
        self._agentEye = Layer()
        sclera = ClosedSpline(Point(0,0), Point(1,-.2), Point(2,-.3),
                              Point(4,0), Point(5,0), Point(4,0), Point(4,.4),
                              Point(3.7,.8), Point(3.4,1),Point(3,1.2),
                              Point(2,1.5), Point(1,1.2), Point(.6,1), Point(.3,.5),)
        sclera.setFillColor('white')
        sclera.setBorderWidth(.3)
        iris = ClosedSpline(Point(0,0), Point(1,-.2), Point(2,-.3), Point(2.3,-.3),
                            Point(2,.7), Point(1.6,1), Point(1,1.1), Point(.6,1),
                            Point(.3,.5))
        iris.setFillColor('brown4')
        iris.setBorderWidth(.2)
        pupil = Circle(.6)
        pupil.move(1,.4)
        pupil.setFillColor('black')
        pupil.setBorderWidth(0)
        
        self._agentEye.add(sclera)
        self._agentEye.add(iris)
        self._agentEye.add(pupil)
        self._agentEye.move(-1,-7.5)
        self._agentEye.scale(.9)

        self._agentEye1 = Layer()
        sclera1 = sclera.clone()
        sclera1.flip()
        iris1 = iris.clone()
        iris1.move(-4,0)
        pupil1 = pupil.clone()
        pupil1.move(-4,0)
        self._agentEye1.add(sclera1)
        self._agentEye1.add(iris1)
        self._agentEye1.add(pupil1)
        self._agentEye1.move(-2,-7.5)
        self._agentEye1.scale(.9)
        
        # agent arms and legs
        self._agentarm = ClosedSpline(Point(0,0), Point(1,1), Point(1.7,2), Point(2.4,3),
                           Point(3.1,4), Point(3.8,5), Point(4.3,6), Point(4.6,6.6),
                           Point(5.2,6), Point(6.5,5), Point(6.8,5.6),
                           Point(6.5,6), Point(6,6.2), Point(5.4,7), Point(6,7.2),
                           Point(7,7.3), Point(8,7.6),Point(7,8), Point(6,8),
                           Point(6.8,9), Point(6.5,9.5), Point(5,9.4), Point(4.4,9),
                           Point(4.6,8), Point(3,8), Point(1.6,7.6), Point(3,7.2),
                           Point(3,6), Point(2,5.2), Point(1,4.3),Point(0,3.8))
        self._agentarm.setFillColor(skin)
        self._agentarm.setBorderWidth(.4)
        self._agentarm.setDepth(51)
        self._agentarm.move(1.5,-3)
        self._agentarm2 = self._agentarm.clone()
        self._agentarm2.move(-5,2)
        self._agentarm2.flip()
        self._agentarm2.scale(.8)
        self._agentarm2.setBorderWidth(.4)

        self._detail1 = Path(Point(0,0), Point(0,1.8)) #hides line between arm and body
        self._detail1.setBorderColor(skin)
        self._detail1.move(3,0)
        self._detail2 = self._detail1.clone()
        self._detail2.move(-6.2,0)

        self._agentleg = Layer()
        agentleg = ClosedSpline(Point(0,0), Point(1,.6),Point(1.6,1),Point(2.5,2),
                                Point(3,3),Point(2.8,4), Point(2.6,5), Point(2,5.8),
                                Point(1.6,6), Point(1,6.5), Point(0,6.9), Point(-.3,6),
                                Point(-.4,5),Point(-.6,4.4), Point(-1,4.2), Point(-1.7,4.2))
        agentleg.setFillColor(skin)
        agentleg.setBorderWidth(.3)
        agentleg.scale(.7)
        agentleg.rotate(-20)
        agentleg.move(2.5,5.4)

        detail3 = Path(Point(0,0), Point(0,2.8))
        detail3.setBorderColor(skin)
        detail3.move(2.8,5.7)

        flipper = flipperNormal.clone()
        flipper.flip()
        flipper.setDepth(51)
        flipper.move(6.5,1.5)
        flipper2 = flipper.clone()
        flipper2.setDepth(51)
        flipper2.move(0,0)
        

        
        self._agentleg.add(agentleg)
        self._agentleg.add(detail3)
        self._agentleg1 = self._agentleg.clone()
        self._agentleg.add(flipper)
        self._agentleg1.flip()
        self._agentleg1.add(flipper2)

        # code for trap
        self._trapAgent = Layer()
        top = Rectangle(14,1)
        top.setDepth(30)
        top.setFillColor('grey')
        top.setBorderWidth(.1)
        bottom = top.clone()
        top.move(0,-15)
        bottom.move(0,12)
        self._trapAgent.add(top)
        self._trapAgent.add(bottom)
        
        for k in range(7):
            bar = Rectangle(.5,27)
            bar.setFillColor('grey')
            bar.setBorderWidth(.1)
            bar.setDepth(31)
            bar.move(-6+k*2,-1)
            self._trapAgent.add(bar)

        # leg when attack function called
        self._attackleg = Layer()
        attackleg = ClosedSpline(Point(-2.7,-3), Point(-1.7,-2), Point(-.7,-1),
                                 Point(0,0), Point(.6,1), Point(1,2),Point(1.3,1),
                                 Point(.8,0), Point(.5,-1),Point(.2,-2),Point(.3,-3),
                                 Point(.5,-4))
        attackleg.setFillColor(skin)
        attackleg.setBorderWidth(.3)
        attackfoot = ClosedSpline(Point(1,2), Point(1,3), Point(1.2,4), Point(2,4.6),
                                  Point(3,4.2), Point(4,3.2), Point(4.8,2), Point(5,1),
                                  Point(4.6,1.7), Point(4.2,-.2), Point(3.4,-.1),
                                  Point(3,-1.1),Point(2,-.4), Point(1.3,1))
        attackfoot.setFillColor('orange')
        attackfoot.setBorderWidth(.4)
        self._attackleg.add(attackleg)
        self._attackleg.add(attackfoot)
        self._attackleg.scale(1.2)
        self._attackleg.move(3,9)

    def setColor(self, color = 'darkcyan'):
        '''
        allows user to change the color of perry while in pet form. Otherwise just returns a message on the screen
        '''
        if self._pet:
            self._bodyNormal.setFillColor(color)
            self._leg1.setFillColor(color)
            self._leg2.setFillColor(color)
            self._leg3.setFillColor(color)
            self._leg4.setFillColor(color)
        else:
            message = Text("Perry the Platypus!")
            message.setFontSize(3)
            message.move(0,-15)
            self.add(message)
            sleep(2)
            self.remove(message)

    def agent(self):
        '''
        changes platypus to agent form if it is in pet form by replacing the pet body parts with agent ones
        '''
        if self._pet:
            self.remove(self._normallegs)
            self.remove(self._bodyNormal)
            self.remove(self._normalEyes)
            self.remove(self._hair)
            self.add(self._agentBody)
            self.add(self._hat)
            self._mouth.move(6,-6)
            self._mouth.scale(.7)
            self._tail.rotate(-65)
            self._tail.move(-2.5,13)
            self.add(self._agentEye)
            self.add(self._agentEye1)
            self.add(self._agentarm)
            self.add(self._detail1)
            self.add(self._agentarm2)
            self.add(self._detail2)
            self.add(self._agentleg)
            self.add(self._agentleg1)
            self._pet = False

    def pet(self):
        '''
        changes agent to pet similar to agent(). However, agent can't be in a cage (trapped) when this function is called
        '''
        if not self._trapped:
            if not self._pet:
                self.add(self._normallegs)
                self.add(self._bodyNormal)
                self.add(self._normalEyes)
                self.add(self._hair)
                self._mouth.move(-6,6)
                self._mouth.scale(1/.7)
                self._tail.move(2.5,-13)
                self._tail.rotate(65)
                self.remove(self._agentEye)
                self.remove(self._agentEye1)
                self.remove(self._agentarm)
                self.remove(self._detail1)
                self.remove(self._agentarm2)
                self.remove(self._detail2)
                self.remove(self._agentleg)
                self.remove(self._agentleg1)
                self.remove(self._agentBody)
                self.remove(self._hat)
                self._pet = True
            
    
    def walk(self, units = 10):
        '''
        moves perry in the direction he is tradiationally facing by units specified or default 10 units slowly
        '''
        if not self._trapped:
            for k in range(4):
                self.move(-units/4,0)
                sleep(.1)

    def run(self, units = 10):
        '''
        moves perry in the direction he is tradiationally facing by units specified or default 10 units faster
        '''
        if not self._trapped:
            self.move(-units,0)

    def wheresperry(self):
        '''
        Makes perry dissapear in pet form but he only loses his hat in agent form because that is what is identifying him
        '''
        if not self._trapped:
            if not self._gone: # previously defined for this purpose
                if self._pet:
                    self.remove(self._normallegs)
                    self.remove(self._bodyNormal)
                    self.remove(self._normalEyes)
                    self.remove(self._hair)
                    self.remove(self._mouth)
                    self.remove(self._tail)
                    message = Text("Where's Perry")
                    message.setFontSize(3)
                    self.add(message)
                    sleep(2)
                    self.remove(message)
                else:
                    self.remove(self._hat)
                    message = Text("Where'd you go Perry the Platypus")
                    message.setFontSize(2)
                    message.move(0,-13)
                    self.add(message)
                    sleep(3)
                    self.remove(message)
                self._gone = True

    def foundhim(self):
        '''
        Opposite of wheresperry() to find him if he is gone
        '''
        if self._gone:
            if self._pet:
                self.add(self._normallegs)
                self.add(self._bodyNormal)
                self.add(self._normalEyes)
                self.add(self._hair)
                self.add(self._mouth)
                self.add(self._tail)
                message = Text("Hey it's Perry!")
                message.setFontSize(3)
                message.move(0,-10)
                self.add(message)
                sleep(2)
                self.remove(message)
            else:
                self.add(self._hat)
            self._gone = False

    def trap(self):
        '''
        makes a cage fall on perry if he is in agent form as he gets trapped by Dr. Doofenshmirtz
        '''
        if not self._trapped: # this trapped is used elsewhere as well so perry can't do many things while he is trapped
            if not self._pet:
                self._trapAgent.move(0,-40)
                self.add(self._trapAgent)
                for k in range(10):
                    sleep(.1)
                    self._trapAgent.move(0,4)
                self._trapped = True
            else:
                message = Text("Hey Perry!")
                message.setFontSize(3)
                message.move(0,-15)
                self.add(message)
                sleep(2)
                self.remove(message)

    def escape(self):
        '''
        opposite of trap which helps perry escape the cage. When he is in pet form, he simply makes text appear for these functions for fun
        '''
        if self._trapped:
            if not self._pet:
                self.remove(self._trapAgent)
                self._trapped = False
        else:
            if self._pet:
                message = Text("Hey Perry!")
                message.setFontSize(3)
                message.move(0,-15)
                self.add(message)
                sleep(2)
                self.remove(message)

    def attack(self, units = 20):
        '''
        Makes perry appear to attack as his leg changes to attacking version and he moves in direction of his kick
        '''
        if not self._pet:
            if not self._trapped:
                self.remove(self._agentleg)
                self.add(self._attackleg)
                sleep(1)
                self.move(units,0)
                sleep(1)
                self.remove(self._attackleg)
                self.add(self._agentleg)

    def tailslap(self):
        '''
        Rotates perry's tail to make a tailslap attack which can be used in both agent and pet form
        '''
        if not self._pet:
            if not self._trapped:
                for k in range(4):
                    self._tail.rotate(10)
                    self._tail.move(-1,-.5)
                    sleep(.1)
                for k in range(4):
                    self._tail.rotate(-10)
                    self._tail.move(1,.5)
                    sleep(.1)
        else:
            for k in range(3):
                self._tail.rotate(10)
                self._tail.move(-1,-.5)
                sleep(.1)
            for k in range(3):
                self._tail.rotate(-10)
                self._tail.move(1,.5)
                sleep(.1)

    def theme(self):
        '''
        Simply makes a short text "theme" appear if in agent form
        '''
        if not self._pet:
            message = Text("Agent Perry!")
            message.setFontSize(3)
            message.move(0,-15)
            self.add(message)
            sleep(2)
            self.remove(message)
                
            
        


if __name__ == '__main__':
    paper = Canvas(800,400)
    perry = Platypus()
    perry1 = Platypus()
    perry1.move(200,300)
    perry1.scale(5)
    paper.add(perry1)
    perry1.setColor('purple')
    perry1.wheresperry()
    perry.move(100,100)
    perry.scale(4)
    perry.agent()
    perry1.foundhim()
    perry1.walk()
    paper.add(perry)
    perry.attack()
    perry.tailslap()
    perry.pet()
    sleep(.5)
    perry.agent()
    perry1.trap()
    perry.trap()
    sleep(.5)
    perry.escape()
    perry1.tailslap()
    perry.wheresperry()
    perry.foundhim()
    sleep(.5)
    perry.theme()
    perry.attack(50)
    perry.walk()
    perry.run()
    perry.walk()
    perry1.trap()
    perry1.agent()
    perry1.trap()
    sleep(.5)
    perry1.escape()
    perry1.pet()
    
    
    
    
