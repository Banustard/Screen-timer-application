import time
def main():
    nsec = int(input("Enter number of seconds: "))
    # range from nsec to zero backwards
    for x in range(nsec, -1, -1):
        time.sleep(1)
        print(formatTime(x))
def formatTime(x):
    minutes, seconds_rem = divmod(x, 60)
    # use string formatting with C type % specifiers
    # %02d means integer field of 2 left padded with zero if needed
    return "T ninus %02d:%02d" % (minutes, seconds_rem)

main()
