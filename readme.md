**task-1:**
RSA API
follwing methods are supported by the API 

aijax@aijax:~/Documents/NS/netsec-lab$ python3 rsa.py 
_____ created RSA cryptosystem with  following configuration _____
randomly choosen primes p =  19  q =  41
public key (e, phi(n)) =  (553, 779)
private key d =  457
----------**THE RSA API**-----------------
Select option
1. Encrypt
2. Decrpyt
3. Get Public key of the CryptoSystem
4. Exit 

1
Please enter a message (format: INT32 < 779 )120
cipher text of message M =  120  is C =  612
----------**THE RSA API**------------------
Select option
1. Encrypt
2. Decrpyt
3. Get Public key of the CryptoSystem
4. Exit 

3
(553, 779)
---------- **THE RSA API** -------------------
Select option
1. Encrypt
2. Decrpyt
3. Get Public key of the CryptoSystem
4. Exit 

2
Please enter a message (format: INT32 < 779 )612
Plain text of cipher =  612  is m =  120
----------- **THE RSA API** ------------------
Select option
1. Encrypt
2. Decrpyt
3. Get Public key of the CryptoSystem
4. Exit 

4
Thank You /\

***************** TASK 2 ***************
aijax@aijax:~/Documents/NS/netsec-lab$ python3 smp.py
enter value of n at bob : 55
enter bob's Publckey(e) : 7
enter bob's private key : 23
enter value of m1: 39
enter value of prime p for bob's computaion : 31
Enter two distinct integers x,y 1<= x,y <= 4 seperated by space: 
4 2
(7, 55)
cipher text of message M =  39  is C =  19
got c1 as  15  m1 as  39
Value of Alice is greater than Bob's

*************** TASK 3*****************
aijax@aijax:~/Documents/NS/netsec-lab/2019h1030019h_TASK_3$ python3 clientTable.py 

server is up and running...
127.0.0.1:37828 has connected.

*CLIENT*
aijax@aijax:~/Documents/NS/netsec-lab/2019h1030019h_TASK_3$ python3 client
.py 
server:  Hello there! Let's get you registered! 
server:  Please enter 4 digit user ID
your reply: 9090
server:  2user ID : 9090 
Please enter a password:
pasha

*SERVER*
********** updated table of hashed passwords **********
9090  -->  72d1be9259cfd91d41ff442bd88a2a6e85d3ead66e19980b0ad422bf7a075b2e


*CLIENT*

registered sucessfully
Press Enter to exit...
aijax@aijax:~/Documents/NS/netsec-lab/2019h1030019h_TASK_3$ python3 client
.py 
server:  Hello there! Let's get you registered! 
server:  Please enter 4 digit user ID
your reply: 9090


*SERVER*
server:  user ID : 9090 has already registered

*************** TASK 4 *****************
uses RSA API created in task 1 to generate cryptosystem at each client
Execution:
aijax@aijax:~/Documents/NS/netsec-lab/RSA table$ python3 client.py 
_____ created RSA cryptosystem with  following configuration _____
randomly choosen primes p =  11  q =  26
public key (e, phi(n)) =  (207, 286)
private key d =  93
""
    **every client is uniquely identified with a user id**
            
""
Enter 4-digit user id: 6566 
(207, 286)
MENU
1. Update RSA
2.Query a Public key
3.Exit
Choose a option: 2
enter the uid the client who's Public key is to retrived: 6566
public key of 6566 is ( 207 , 286)
MENU
1. Update RSA
2.Query a Public key
3.Exit
Choose a option: 3   
aijax@aijax:~/Documents/NS/netsec-lab/RSA table$ python3 client.py 
_____ created RSA cryptosystem with  following configuration _____
randomly choosen primes p =  23  q =  14
public key (e, phi(n)) =  (173, 322)
private key d =  205
every client is uniquely identified with a user id
Enter 4-digit user id: 6588
(173, 322)
MENU
1. Update RSA
2.Query a Public key
3.Exit
Choose a option: 2       
enter the uid the client who's Public key is to retrived: 6566
public key of 6566 is ( 207 , 286)
MENU
1. Update RSA
2.Query a Public key

**Any number of clients can be instantiated simultaneously**


****************** TASK 5 *****************
**RUN SERVER**
aijax@aijax:~/Documents/NS/netsec-lab/2019h1030019h_TASK_5$ python3 server.py 
server is up and running
both alice and bob are connected!
ewe

**RUNNING Alice client**
aijax@aijax:~/Documents/NS/netsec-lab/2019h1030019h_TASK_5$ python3 a_client.py enter Alice'sock Wealth(x) 4
calculated c1 :  25  m1 :  39
Alice is wealthier than Bob' 

**RUNNING BOB Client**
aijax@aijax:~/Documents/NS/netsec-lab/2019h1030019h_TASK_5$ python3 b_client.py 
bob'sock Wealth (y)<=10 : 2
Alice is wealthier than Bob' 