#Lets you vote for anything
#run from console
#names must be unique

class Vote(object):
	def __init__(self, name, vote):
		self.name = name
		self.vote = vote

	@classmethod
	def from_input(self):
		return self(
			input('Name: '),
			input('Vote: '),
			)

	def get_name(self):
		return self.name



class Voting:
	def __init__(self, subject):
		self.subject = subject

	@classmethod
	def subject_input(self):
		return self(
			input('Enter a question for your poll: '))

	def voting(self):
		votes = {}
		prompt = str('---{}---\n'.format(self.subject))
		vote_time = True

		#After the subject is set the polls begin
		while vote_time:
				#skip lines so you cant see what others voted
				for skip in range(100):
					print("\n")
				print(prompt)
				user = Vote.from_input()
				if user.name in votes.keys():
					print("\tThat person has already voted." + 
							"\n\tPlease use a different name.")
				else:
					votes[user.name] = user.vote

				#If there are more voters there are more votes
				exit = input("\nType 'exit' to exit," 
							+ " or press enter to keep voting...")

				#End the Poll and Print Results
				if exit.upper() == 'EXIT':
					for skip in range(100):
						print("\n")
					print("{:^50}".format("Results:\n"))
					for name, vote in votes.items():
						print("{:^20} voted {:^20}".format(name, vote))

					#End the program
					vote_time = False
				

vote_now = Voting.subject_input()
vote_now.voting()
