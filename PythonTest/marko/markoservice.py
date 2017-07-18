from decimal import *
class State:
    def __init__(self, name : str):
        self.name = name

#here we model prob as class instead of just a decimal because it also
#represents state transition
class Prob:
    def __init__(self, state_start : State, state_end : State, prob : Decimal):
        self.state_start = state_start
        self.state_end = state_end
        self.prob = prob



import unittest
class StepByStepTest(unittest.TestCase):
    #https://www.youtube.com/watch?v=5uGhAQOs6Aw&index=5&list=PLKG3ExuC02lsnZUJDdOlYJd5CRe3otzq1
    def test_ab1(self):
        state_A = State("A")
        state_B = State("B")

        prob_state_A_to_state_A = Prob(state_A, state_A, 0.6)
        prob_state_B_to_state_A = Prob(state_B, state_A, 0.2)

       
        #test state_A at step2
        prob_state_A_step_1 = 0.6
        prob_state_B_step_1 = 1 - prob_state_A_step_1
        prob_state_A_step_2 = prob_state_A_to_state_A.prob * prob_state_A_step_1 + prob_state_B_to_state_A.prob * prob_state_B_step_1
        self.assertTrue(prob_state_A_step_2 == 0.44)

        #test state_A at step3
        prob_state_B_step_2 = 1 - prob_state_A_step_2
        prob_state_A_step_3 = prob_state_A_to_state_A.prob * prob_state_A_step_2 + prob_state_B_to_state_A.prob * prob_state_B_step_2
        self.assertTrue(prob_state_A_step_3 == 0.376)

    #https://www.youtube.com/watch?v=5I0YPndroIE&index=7&list=PLKG3ExuC02lsnZUJDdOlYJd5CRe3otzq1
    def test_ab2(self):
        state_A = State("A")
        state_B = State("B")

        prob_state_A_to_state_A = Prob(state_A, state_A, 0.5)
        prob_state_B_to_state_A = Prob(state_B, state_A, 1)

       
        #test state_A at step2
        prob_state_A_step_1 = 0.5
        prob_state_B_step_1 = 1- prob_state_A_step_1
        prob_state_A_step_2 = prob_state_A_to_state_A.prob * prob_state_A_step_1 + prob_state_B_to_state_A.prob * prob_state_B_step_1
        self.assertTrue(prob_state_A_step_2 == 0.75)

        #test state_A at step3
        prob_state_B_step_2 = 1 - prob_state_A_step_2
        prob_state_A_step_3 = prob_state_A_to_state_A.prob * prob_state_A_step_2 + prob_state_B_to_state_A.prob * prob_state_B_step_2
        self.assertTrue(prob_state_A_step_3 == 0.625)



        #https://www.youtube.com/watch?v=4xfEvRGRBnU&list=PLKG3ExuC02lsnZUJDdOlYJd5CRe3otzq1&index=13
    def test_sequencetoprob(self):
        sequence = ["s","s","s","s","s","r","s","s","s","r","r"]
        state_A = State("A")
        state_B = State("B")

        prob_state_A_to_state_A = Prob(state_A, state_A, 0.5)
        prob_state_B_to_state_A = Prob(state_B, state_A, 1)

       
        #test state_A at step2
        prob_state_A_step_1 = 0.5
        prob_state_B_step_1 = 1- prob_state_A_step_1
        prob_state_A_step_2 = prob_state_A_to_state_A.prob * prob_state_A_step_1 + prob_state_B_to_state_A.prob * prob_state_B_step_1
        self.assertTrue(prob_state_A_step_2 == 0.75)

        #test state_A at step3
        prob_state_B_step_2 = 1 - prob_state_A_step_2
        prob_state_A_step_3 = prob_state_A_to_state_A.prob * prob_state_A_step_2 + prob_state_B_to_state_A.prob * prob_state_B_step_2
        self.assertTrue(prob_state_A_step_3 == 0.625)

