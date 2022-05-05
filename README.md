# WordlistGeneratorUsingPython

This is a simple wordlist generator using Python that can be used for cracking Wi-Fi passwords.

When I started learning about Ethical Hacking, I was mesmerized by Wi-Fi hacking and started with that on Kali Linux. I initially tried it out on my Wi-Fi router using all the wordlist that was provided by Kali Linux. The sad part was when none of the passwords in the wordlist was the password for my Router and the cracking failed.

At that time, I wasn't a Python Developer so I had to create a wordlist using Java where I had to use 'n' number of for loops where 'n' is the number of characters needed(i.e., if the password was or 8 characters, the value of n would be 8, so I had to iterate through 8 for loops). Adding or removing extra loops for each value of 'n' was a hassle.

After Python, I tried my first PIN List (containing 0000-9999) and since the technique is still Brute Force so I made sure all the numbers were in the pinlist.txt file, after which I finally made the wordlist.
