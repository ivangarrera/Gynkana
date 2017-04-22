48982
You passed the step 0!
(The maximum score (in the best case) is indicated )

This is the server por the Network Computer ginkana.
Version 0.20170316.

Remember that you can see the server log in:
http://atclab.esi.uclm.es/ginkana/

Students are advised to use UTF-8 encoding in their terminal to avoid coding
problems.

Step 1: UDP
-----------

- Create a UDP server on your machine (on the port you want)
- Send a message to the UDP server atclab.esi.uclm.es: 2000
  indicating the identifier "48982" and the port on which you have created
  your UDP server, separated by a space.
  Example: "48982 7777" (without quotes).

Your UDP server will receive the instructions to continue.
You have 4 seconds.

Hints:
- Check that it is possible to connect to your UDP server from a machine with
  a public IP (use netcat to check that).

1990
You passed the step 1!

Etapa 2: Aritmetic
------------------

- Connect to server atclab.esi.uclm.es:1990
- You will receive a text string with a mathematical operation in ASCII format.
- The expression contains parentheses and brackets, and are well balanced (there
  are so many opening and closure).
- Calculate the result of the operation and reply through the same socket, placing
  the result within parentheses.
- The process is repeated for an undetermined number of operations.

If everything is right, the server will instruct you to continue.
You have 20 seconds.

Tracks:
- The parentheses are vital, the spaces trivial.
- The symbol '/' represents an entire division.
- Example:
   - server: (2 * [3+ 5] * {1 -0})
   - client: (16)

Restrictions:
- It is not allowed to use the function eval(), exec() or any other that evaluates
  python statements.

You have 20 seconds.

[[86/ (17 * 34)]+ 89]
Result is 89
[{21*25}* 46]
Result is 24150
({70 *{72 *69}}+[[[59 +0]/ {47 *31}] -39])
Result is 347721
(76 -{{74 / 70}- [9 - {56-40}]})
Result is 68
39126
You passed the step 2!

Step 3: HTTP Client
---------------------

- You must download the file
  "http://atclab.esi.uclm.es:5000/39126".

The file contains the instructions to continue.
You have 6 seconds.

Restrictions:
- It is not allowed to use urllib, urllib2 and urllib3 modules.

74309
You passed the step 3!

Step 4: Ping
-------------

- You must send an ICMP Echo Request message to atclab.esi.uclm.es.
  the payload of this message must include, AFTER the usual
  content, the ASCII string "74309".

     +--------------+----------------------------+
     | Echo Request |                            |
     | Header       | timestamp(8 bytes) + 74309 |
     +--------------+----------------------------+

- You will receive an ICMP Echo Reply message with the instructions to
  continue.

You have 5 seconds.

Hints:
- Using wireshark, analyze the content and size of a conventional ping
  message. You can send pings that are shorter than normal with "ping -s size".
- Study the chapter "RAW Sockets" in the lab manual.
- Remember that to use raw sockets you must run the program with
  admin privileges.
- Build an ICMP message mimicking the one you have captured. Identical
  at first. If it works, add your changes step by step.
- To construct the message you can use struct.pack().
- You can use the checksum calculation function in
  https://bitbucket.org/arco_group/python-net/src/tip/raw/icmp_checksum.py
- Constructs the ICMP message indicating a 0 in the checksum field. Calculate the
  checksum and rebuilds the message using the calculation result.

11:04:5742935
You passed the step 4!

Step 5: Proxy Web
------------------

- Create an HTTP Proxy server on your computer (in the port of your choice).
- Your server will receive a random amount of HTTP requests for download
  third-party URLs, you must download these resources (using HTTP) and
  return them to the requesting customer.

 +--------+        +--------------+       +-------------+
 | Client |        | Proxy server |       | HTTP server |
 +--------+        +--------------+       +-------------+
      |                    |                     |
      |  GET(server, url)  |                     |
      +------------------>+++  connect(server)   |
      |                   | |------------------->|
      |                   | |   file: GET(url)   |
      |      file         | |------------------->|
      |<------------------+++                    |
      |                    |                     |


- Create a client socket and send a message to the server TCP atclab.esi.uclm.es:9000
  Indicating the identifier "42935" and the port on which you have created
  Your proxy server, separated by a space.
  Example: "42935 7777".
- Through the same socket you will receive further instructions or information
  about errors.

Hints:
- Caution: Your proxy will receive simultaneous requests and it is expected that
  serve them quickly. If it takes too long, this step will fail. In order to
  achieve it create a concurrent server for your proxy.
- You can prove that your proxy is right by executing it as a independent program
  (unrelated to gink
