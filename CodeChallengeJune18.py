# Without directly modifying the data structures, create a script in either
# python or javascript that cycles through all the parents and prints to the
# terminal the proper activities for their child's age group. When there are no
# more activities for that parent, print “Curriculum complete!”..
#
# (Make sure your script accounts for any edge cases in the provided data!)

parents = {
    'Henry': {'childName': 'Calvin', 'age': 1},
    'Ada': {'childName': 'Lily', 'age': 4},
    'Emilia': {'childName': 'Petra', 'age': 2},
    'Biff': {'childName': 'Biff Jr', 'age': 3},
    'Milo': {}
}

activities = [
    {
        'age': 1,
        'activity': [
            'Go outside and feel surfaces.',
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]
import sys
# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Document your creation process with proper git workflow.
# - Personalize the message output to make it more friendly.
# - Allow users to input new activities & parents before executing the script.
# - Print one activity at a time per parent and continue cycling through until
#   all parents have recieved all their activities.
print("\n\n-----------------------------------------------------------------------------------\n")
print("Enter the choice:\n\n1. Create new activity\n2. Register a parent\n3. Display all parent's info\n4. Display all activities\n5. Display activities for a child of a particular parent\n6. Display all information about the parents and their child's activities\n7. Exit\n")
print("-----------------------------------------------------------------------------------")
try:
	option=int(input())
except:
	print("-----------------------------------------------------------------------------------")
	print("Enter an integer value!!")
	print("-----------------------------------------------------------------------------------")
	print("EXITING THE PROGRAM!!")
	print("-----------------------------------------------------------------------------------")
	sys.exit(1)
print("-----------------------------------------------------------------------------------")
while(option!=7):
	if(option==1):
		try:
			age_group=int(input("Enter the age group:\n"))
		except:
			print("-----------------------------------------------------------------------------------")
			print("Enter an integer value!!")
			print("-----------------------------------------------------------------------------------")
			print("EXITING THE PROGRAM!!")
			print("-----------------------------------------------------------------------------------")
			sys.exit(1)
		print("-----------------------------------------------------------------------------------")
		flag=0
		for i in activities:
			if i['age']==age_group:
				act=input("Enter the activity(enter quit to return to the menu):\n")
				print("-----------------------------------------------------------------------------------")
				while(act.upper()!="QUIT"):
					i['activity'].append(act.capitalize())
					act=input("Enter the activity(enter quit to return to the menu):\n")
					print("-----------------------------------------------------------------------------------")
				flag=1
				break
		if flag==0:
			new_age_group={
				'age':age_group,
				'activity':[]
			}
			act=input("Enter the activity(Enter quit to return to the menu):\n")
			print("-----------------------------------------------------------------------------------")
			while(act.upper()!="QUIT"):
				new_age_group['activity'].append(act.capitalize())
				act=input("Enter the activity(Enter quit to return to the menu):\n")
				print("-----------------------------------------------------------------------------------")
			activities.append(new_age_group)
	elif option==2:
		name=input("Enter the name of the parent:\n")
		all_parents_names=[i.upper() for i in list(parents.keys())]
		if name.upper() in all_parents_names:
			print("\nParent name already exists\nCheck below for the existing entry")
			print("-----------------------------------------------------------------------------------")
			option=3
			continue
		else:
			name=name.lower().capitalize()
			childName=input("Enter the child's name:\n").lower().capitalize()
			try:
				age=int(input("Enter the child's age:\n"))
			except:
				print("-----------------------------------------------------------------------------------")
				print("Enter an integer value!!")
				print("-----------------------------------------------------------------------------------")
				print("EXITING THE PROGRAM!!")
				print("-----------------------------------------------------------------------------------")
				sys.exit(1)
			parents[name]={
				'childName':childName,
				'age':age
			}

	elif option==3:
		for parent in parents:
			print("Parent Name: ",parent,sep="")
			if 'age' in parents[parent]:
				print("Child Age: ",parents[parent]['age'],sep="")
			if 'childName' in parents[parent]:
				print("Child Name: ",parents[parent]['childName'],sep="")
			print("-----------------------------------------------------------------------------------")

	elif option==4:
		for a in activities:
			print("Age Group: ",a['age'],sep="")
			cnt=0
			flag=0
			if 'activity' in a:
				for activity in a['activity']:
					if cnt==0:
						print("\tActivities:")
					cnt+=1
					print("\t\t",cnt,". ",activity,sep="")
					flag=1
				if flag==0:
					print("No activity exists for this age group")
			else:
				print("No activity exists for this age group")
			print("-----------------------------------------------------------------------------------")

	elif option==5:
		name=input("Enter the name of the parent:\n")
		print("-----------------------------------------------------------------------------------")
		all_parents_names=[i.upper() for i in list(parents.keys())]
		if name.upper() in all_parents_names:
			name=name.lower().capitalize()
			print("Parent Name: ",name,sep="")
			if 'childName' in parents[name]:
				print("Child Name: ",parents[name]['childName'],sep="")
			if 'age' in parents[name]:
				age_group=parents[name]['age']
				print("Child Age: ",parents[name]['age'],sep="")
				flag=0
				for i in activities:
					if i['age']==age_group:
						cnt=0
						if 'activity' in i:
							for activity in i['activity']:
								if cnt==0:
									print("\tActivities:")
								cnt+=1
								print("\t\t",cnt,". ",activity,sep="")
								flag=1
							if flag==1:
								print("Curriculum complete!")
						else:
							print("Curriculum complete!")
							print("No activity exists for this age group")
						break
				if flag==0:
					print("Curriculum complete!")
					print("No activity exists for this age group")
			else:
				print("Parent's information is not complete!")
		else:
			print("Parent's information doesn't exist")
	elif option==6:
		for name in parents:
			print("Parent Name: ",name,sep="")
			if 'childName' in parents[name]:
				print("Child Name: ",parents[name]['childName'],sep="")
			if 'age' in parents[name]:
				age_group=parents[name]['age']
				print("Child Age: ",age_group,sep="")
				flag=0
				for i in activities:
					if i['age']==age_group:
						cnt=0
						if 'activity' in i:
							for activity in i['activity']:
								if cnt==0:
									print("\tActivities:")
								cnt+=1
								print("\t\t",cnt,". ",activity,sep="")
								flag=1
							if flag==1:
								print("Curriculum complete!")
						else:
							print("Curriculum complete!")
							print("No activity exists for this age group")
						break
				if flag==0:
					print("Curriculum complete!")
					print("No activity exists for this age group")
			print("-----------------------------------------------------------------------------------")	

	print("\n\n-----------------------------------------------------------------------------------\n")
	print("Enter the choice:\n\n1. Create new activity\n2. Register a parent\n3. Display all parent's info\n4. Display all activities\n5. Display activities for a child of a particular parent\n6. Display all information about the parents and their child's activities\n7. Exit\n")
	print("-----------------------------------------------------------------------------------")
	option=int(input())
	print("-----------------------------------------------------------------------------------")

print("EXITING THE PROGRAM!!")
print("-----------------------------------------------------------------------------------")
