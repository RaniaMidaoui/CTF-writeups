## Description
>
> I want to tell you a secret, but i'm afraid someone will intercept our communication. I know how good you are now with quantum encoding, so I will let you figure it out on your own. 
> I used the following code to get to encode the secret:
 ```
 qc.s(q[2])
 qc.ccx(q[0],q[1],q[2])
 qc.h(q[2])
 qc.swap(q[1],q[0])
 qc.y(q[0])
 ```
>The secret is: VMëÜÁÂÎèÜ
>
>Also, the secret contains two english words, it doesn't contain special characters nor numbers.
>
>Flag format: Securinets{decoded_message}
>
>BE CAREFUL, YOU ONLY HAVE 5 attempts
>
>Author: mida0ui

## Solution
