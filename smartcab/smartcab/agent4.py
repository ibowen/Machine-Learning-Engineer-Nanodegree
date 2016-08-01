import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import os
import numpy as np

# Based on the Q-learning implementation of Travis DeWolf in https://github.com/studywolf
class QAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env, epsilon=0.1, alpha=0.2, gamma=0.9):
        super(QAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        # Q_Learning state dictionary
        self.q = {}
		# exploration threshold
        self.epsilon = epsilon
		# learning rate
        self.alpha = alpha
		# discount rate
        self.gamma = gamma
        self.actions = Environment.valid_actions
        # total reward
        self.total_reward = 0.0

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.total_reward = 0.0
        
	# query Q_Learning dictionary to get the state value
    def getQ(self, state, action):
		return self.q.get((state, action), 0.0)
	
	# update Q value
    def updateQ(self, curr_state, action, reward, next_state):
		newv = reward + self.gamma * max([self.getQ(next_state, a) for a in self.actions])
		
		oldv = self.q.get((curr_state, action), None)
		if oldv is None:
			self.q[(curr_state, action)] = reward
		else:
			self.q[(curr_state, action)] = oldv + self.alpha * (newv - oldv)
			
	# update state value
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
        action = self.chooseAction(curr_state)
            
        # Execute action and get reward
        reward = self.env.act(self, action)
        self.total_reward += reward
        
        # Next state
        # Get the next input of the current state
        inputs2 = self.env.sense(self)
        # Get the next waypoint of the next state
        next2_waypoint = self.planner.next_waypoint()
        next_state = inputs2.items()
        next_state.append(next2_waypoint)
        next_state = tuple(next_state)
        
        # Update the current state
        self.updateQ(curr_state, action, reward, next_state)

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]

    def chooseAction(self, state):
		# introduce exploration to avoid local minimum
		if random.random() < self.epsilon:
			action = random.choice(self.actions)
		else:
			# normal implementation of Q update
			q = [self.getQ(state, a) for a in self.actions]
			maxQ = max(q)
			count = q.count(maxQ)
			if count > 1:
				# handle multiple equal best choices
				best = [i for i in range(len(self.actions)) if q[i] == maxQ]
				i = random.choice(best)
			else:
				i = q.index(maxQ)

			action = self.actions[i]
		return action

def run():
    """Run the agent for a finite number of trials."""
    # create output file
    target_dir = os.path.dirname(os.path.realpath(__file__))
    target_path = os.path.join(target_dir, 'qlearning_tuning_report.txt')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
	# loop the parameters
    for epsilon in [0.1, 0.5, 0.9]:
        for alpha in np.arange(0.1, 1, 0.2):
            for gamma in np.arange(0.1, 1, 0.2):
                print epsilon, alpha, gamma
                # Set up environment and agent
                e = Environment()  # create environment (also adds some dummy traffic)
                a = e.create_agent(QAgent, epsilon, alpha, gamma)  # create agent
                e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
				# NOTE: You can set enforce_deadline=False while debugging to allow longer trials

				# Now simulate it
                sim = Simulator(e, update_delay=0.001, display=False)  # create simulator (uses pygame when display=True, if available)
				# NOTE: To speed up simulation, reduce update_delay and/or set display=False
                sim.run(n_trials=100)  # run for a specified number of trials
                # get the count for the number of successful trials and average running time
                summary = sim.report()
                
                # write out the results
                try:
					with open(target_path, 'a') as f:
						f.write('epsilon {}, alpha {}, gamma {} : success {}, avg_time {}, total_reward {}\n'.format(epsilon, alpha, gamma, summary[0], summary[1], round(a.total_reward, 3)))
						f.close()
                except:
					raise

if __name__ == '__main__':
    run()
