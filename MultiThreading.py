""" example """

##here all the statements are getting executed line by line. So, all of the lines comes under same thread

print("statement") 
print("statement")
print("statement")
print("statement")
print("statement")
print("statement")
print("statement")
print("statement")
print("statement")

""" Now using multi_threading concepts which will execute all the independent parts od programms simultaneously"""

import threading 
from threading import *
print("current thread executing: ", threading.current_thread().getName()) #This will return the current thread i.e getting executed currently.

""" Creating a thread without using any class"""

def display():
    for i in range(5):
        print('child thread')

t = Thread(target=display) #crearing a thread object to execute display
#above this line there is only one thread i.e main thread. After t.start(), there wil be one child thread apart from main thread. so, below for loop will be implemented by main thread and above display function will be executed by child thread.
t.start()

for i in range(5): #this fucntion will be implemented by main thread and above function by child thread simultaneously.
    print('Main Thread')

## if we execute the above threading programm multiple times, then It will be different every time. Since, both the for loops are getting executed simultaneously.

""" another example"""

def display():
    for i in range(5):
        print(current_thread().getName())

t = Thread(target=display) #crearing a thread object to execute display
#above this line there is only one thread i.e main thread. After t.start(), there wil be one child thread apart from main thread. so, below for loop will be implemented by main thread and above display function will be executed by child thread.
t.start()

for i in range(5): #this fucntion will be implemented by main thread and above function by child thread simultaneously.
    print(print(current_thread().getName()))

""" second way of starting a thread i.e using a class variable"""

class  Mythread(Thread):

    def run(self):
        for i in range(5):
            print('child thread')

t = Mythread()
t.start()

for i in range(5):
    print('Main Thread')


""" without executing Thread(OOP)"""

from threading import *
class Test():
    def test_function(self):
        for i in range(5):
            print('child Thread')

obj = Test()
t = Thread(target = obj.test_function)
t.start()

for i in range(5):
    print('Main Thread')

""" calculating time for the s program and then by using multithreading concept"""

import time
def doubles(number):
    for i in number:
        time.sleep(1)
        print('doubles: ', 2*i)

def square(number):
    for i in number:
        time.sleep(1)
        print('square: ', i*i)

numbers = [1,2,3,4,5,6,7,8,9]
start_time = time.time()
doubles(numbers)
square(numbers)
end_time = time.time()

print('the complete time taken: ', end_time-start_time)

""" output of above code:
    doubles:  2
    doubles:  4
    doubles:  6
    doubles:  8
    doubles:  10
    doubles:  12
    doubles:  14
    doubles:  16
    doubles:  18
    square:  1
    square:  4
    square:  9
    square:  16
    square:  25
    square:  36
    square:  49
    square:  64
    square:  81
    the complete time taken:  18.020644664764404
"""
    
###using multithreading concept

from threading import *
import time
def doubles(number):
    for i in number:
        time.sleep(1)
        print('doubles: ', 2*i)

def square(number):
    for i in number:
        time.sleep(1)
        print('square: ', i*i)

numbers = [1,2,3,4,5,6,7,8,9]
start_time = time.time()
t1 = Thread(target=doubles, args = (numbers,))
t2 = Thread(target=square, args = (numbers,))
t1.start() #executed by thread1
t2.start() #executed by thread2
end_time = time.time() 
print('the complete time taken: ', end_time-start_time) #executed by main thread

"""output of above code:
    the complete time taken:  0.0002918243408203125 #this is executed by main thread
    doubles:  2
    square:  1
    doubles:  4
    square:  4
    doubles:  6
    square:  9
    square:  16
    doubles:  8
    square:  25
    doubles:  10
    square:  36
    doubles:  12
    doubles:  14
    square:  49
    doubles:  16
    square:  64
    doubles:  18
    square:  81
There is a time difference in both the programms.
"""

"""get the name od thread and set its name"""

from threading import *
print(current_thread().getName())
# current_thread().setName("Abhishek")
current_thread().name = 'Ashish'
print(current_thread().getName())

""" calculating identification number of main thread and child thread"""

from threading import *

def test(number):
    print(f'My favourite number is {number}')

number = 1
t = Thread(target = test, args = (number,))
t.start()

print('Main thread Identification number: ', current_thread().ident)
print('Child thread Identifiication number: ', t.ident)

""" calculating number of activae threads"""

from threading import *

import time
def display():
    print(current_thread().name, "....started")
    time.sleep(3)
    print(current_thread().name, "....ended")


print('The number of active threads:', active_count())
t1 = Thread(target = display, name= 'childThread-1')
t2 = Thread(target = display, name= 'childThread-2')
t3 = Thread(target = display, name= 'childThread-3')
t1.start()
t2.start()
t3.start()
print('The number of active threads: ', active_count())
time.sleep(10)
print('The number of active threads: ', active_count())

""" is_alive function: It is used to check whether a particular thread running or not"""

from threading import *

import time
def display():
    print(current_thread().name, "....started")
    time.sleep(3)
    print(current_thread().name, "....ended")


print('The number of active threads:', active_count())
t1 = Thread(target = display, name= 'childThread-1')
t2 = Thread(target = display, name= 'childThread-2')
t3 = Thread(target = display, name= 'childThread-3')
t1.start()
t2.start()
t3.start()
print('alive threads: ', t1.is_alive())
print('alive threads: ', t2.is_alive())
print('alive threads: ', t3.is_alive())
time.sleep(5)
print('alive threads: ', t1.is_alive())
print('alive threads: ', t2.is_alive())
print('alive threads: ', t3.is_alive())

"""output of above program:
   The number of active threads: 1
    childThread-1 ....started
    childThread-2 ....started
    childThread-3 ....started
    alive threads:  True
    alive threads:  True
    alive threads:  True
    childThread-2 ....ended
    childThread-3 ....ended
    childThread-1 ....ended
    alive threads:  False
    alive threads:  False
    alive threads:  False"""

""" other methods used in multi threading:
1. join() method: If athread wants to wait until completing other thread, Then we use join method  """

from threading import *
import time

def display():
    for i in range(10):
        print('seetha thread')
        time.sleep(3)

t = Thread(target= display)
t.start()

t.join(10) #10 here is the waiting time i.e 10 seconds. after this main thread will start executing.
for i in range(10):
    print('Rama Thread')


""" output without join method:
    seetha thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread

and output with join method:
  seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
seetha thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread"""

""" Questions on multi threading"""
"""1. I need to send an email to 20,000 users stored in a database and also make sure that the email does not do multiple times, so how may I acheive 
through multi threading"""


from threading import *

def send_email(lst):
    for i in lst:
        print('mail sent to a person')

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [9,10,11,12]
l4 = [13,14,15,16]
t1 = Thread(target=send_email, args = (l1,))
t2 = Thread(target=send_email, args = (l2,))
t3 = Thread(target=send_email, args = (l3,))
t4 = Thread(target=send_email, args = (l4,))
t1.start()
t2.start()
t3.start()
t4.start()


"""Daemon threads: the threads which runs in the background are called as daemon threads."""
##once a thread is started. we can't change its daemon nature. we will get runtime error while setting a status for an active thread.

from threading import *
mt = current_thread()
print(mt.isDaemon())
print(mt.daemon)

#main thread is by default not a daemon thread. But, thr child thread can be a daemon thread before it gets started.
#Generally, If the parent thread is not a daemon thread then the child thread is also not a daemon thread.

from threading import *
def job():
    print('thread is executed by child thread')

t = Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())

###another example

from threading import *
import time

def job1():
    print('executed by thread_1')
    t2 = Thread(target=job2)
    print("t2 is daemon: ",t2.isDaemon())
    t2.start()
    

def job2():
    print('executed by thread_2')

t1 = Thread(target=job1)
t1.setDaemon(True)
print("t1 is daemon: ", t1.isDaemon())
t1.start()
time.sleep(10)

##once last daemon thread gets terminated every  daemon thread gets terminated automatically.
##supporting jobs can be implemented by daemon threads while the main jobs are implemented by non daemon threads.







