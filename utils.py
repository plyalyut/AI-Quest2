import sys, time

def type_print(string):
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print() # So we get a new line at hte end