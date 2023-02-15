import csv

def gradecomment(grade):
  '''returns a comment based on grade percentage'''
  if grade > 90:
    return(f'your performance has been consistently excellent, scoring a {grade}. Your programs and solutions are clever and efficient, and I hope you continue to engage with Computer Science in the future.')
  elif grade>71:
    return(f'your performance in this class is solid, scoring a {grade}. You still have room to grow and expand your thinking. Keep working hard!')
  elif grade<=70:
    return(f'you have faced some challenges in this course scoring a {grade}, but please continue to work hard and check in with me. I would encourage checking in with me during office hours or before tests.')

def strongoutcome(outcome, example):
  '''returns a comment based on performance on a learning indicator'''
  return(f"This semester, you showed particular strength on our learning outcome of '{outcome}' when you {example}. I was uniquely impressed by your ability and aptiude for this outcome, and I'm hoping you'll help your classmates get to the same level you're at.")
  
def weakoutcome(outcome, example):
  '''returns a comment based on performance on a learning indicator'''
  return(f"On the other hand, you had some difficulty with our outcome of '{outcome}' after you {example}. I'd encourage you to reach out to me or your classmates for help figuring out this outcome, and to focus on improving here for the next semester.")
  
def absences(number):
  '''returns a comment based on number of absences'''
  if number>10:
    return('Please make sure to make the classes in semester 2! Your grade will be affected according to your absences.')
  elif number>5:
    return('Please make sure to check in with me for absences.')
  elif number<=5:
    return('I appreciate your attendence in class! Keep up the great work')
      
def homework(note):
  '''returns a comment based on homework consistency'''
  if note==5:
    return('You have never miss a single assignment. Keep up the great work!')
  elif note==4:
    return('You turn in your homework consistently, great work!')
  elif note==3:
    return('You have only turn in half of the assignments this semester, please communitcate with me beforehand if you have any questions.')
  elif note==2:
    return('You have only turn in a few assignment, is there a way I can help you next semester? I can provide you some advise on time management!')
  elif note==1:
    return('PLEASE COME TALK TO ME ABOUT YOUR FUTURE HOMEWORK PLANS!')
    
def comment():
  '''using the teacher.csv file, combines the above functions to quickly generate comments for a hypothetical Data Science class'''
  with open('teacher.csv') as f:
    header=f.readline().split(',')
    data = csv.reader(f)
    for line in data:
      with open(f'{line[0]}.txt', 'w') as comment:
        try:
          comment.write('This semester in Data Science we covered the topics of csv file, debugging, and coding and began the study of recursion, which we will continue into the second semester. In addition to daily homework and frequent quizzes, we had two in-class unit tests, a cumulative final exam, and two projects, one on generating comment and one on modeling for SRP.\n')
          comment.write(f'{line[0]}, {gradecomment(int(line[1]))}\n')
          comment.write(f'{strongoutcome(line[2], line[3])}\n')
          comment.write(f'{weakoutcome(line[4], line[5])}\n')
          comment.write(f'{homework(int(line[6]))}\n')
          comment.write(f'{absences(int(line[7]))}\n')
          if line[-1] == '0':
            pass
          else:
            comment.write(line[-1])
            pass
          comment.close()
        except(TypeError,ValueError):
          pass
comment()
