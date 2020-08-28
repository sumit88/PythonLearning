import re

if __name__ == '__main__':
    N = int(input())

    firstNameList = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.search('@gmail\.com$', emailID):
            firstNameList.append(firstName)

    print(*sorted(firstNameList), sep='\n')
