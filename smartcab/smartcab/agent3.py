import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class QLearn:
	def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
		self.q = {}

		self.epsilon = epsilon
		self.alpha = alpha
		self.gamma = gamma
		self.actions = actions

	def getQ(self, state, action):
		return self.q.get((state, action), 0.0)

	def updateQ(self, curr_state, action, reward, next_state):
		newv = reward + self.gamma * max([self.getQ(next_state, a) for a in self.actions])
		
		oldv = self.q.get((curr_state, action), None)
		if oldv is None:
			self.q[(curr_state, action)] = reward
		else:
			self.q[(curr_state, action)] = oldv + self.alpha * (newv - oldv)

	def chooseAction(self, state):
		if random.random() < self.epsilon:
			action = random.choice(self.actions)
		else:
			q = [self.getQ(state, a) for a in self.actions]
			maxQ = max(q)
			count = q.count(maxQ)
			if count > 1:
				best = [i for i in range(len(self.actions)) if q[i] == maxQ]
				i = random.choice(best)
			else:
				i = q.index(maxQ)

			action = self.actions[i]
		return action

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        self.qlearn = QLearn(Environment.valid_actions, epsilon=.05, alpha=0.1, gamma=0.9)

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        
		# Generate the current state
        curr_state = inputs.items()
        curr_state.extend(self.next_waypoint)
        curr_state = tuple(curr_state)

        # Choose the current action
        action = self.qlearn.chooseAction(curr_state)
            
        # Execute action and get reward
        reward = self.env.act(self, action)
        
        # Next state
        # Get the next input of the current state
        inputs2 = self.env.sense(self)
        # Get the next waypoint of the next state
        next2_waypoint = self.planner.next_waypoint()
        next_state = inputs2.items()
        next_state.append(next2_waypoint)
        next_state = tuple(next_state)
        
        # Update the current state
        self.qlearn.updateQ(curr_state, action, reward, next_state)

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.005, display=True)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
