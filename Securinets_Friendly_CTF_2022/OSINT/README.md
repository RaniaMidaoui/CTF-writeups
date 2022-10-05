# Securinets Friendly CTF 2022 writeups
![Categorie](https://img.shields.io/badge/Category-OSINT-blue?style=for-the-badge)


This is my first CTF as an author, I hope that every participant enjoyed my tasks as much as I did while writing them. These are the writeups for all the OSINT challenges, enjoy reading, and don't hesitate to contact me for clarifications.

All the original files are in the repository.

## Bridge

### Description
> There is a bridge near this spot, can you give me its name?
>
>Flag format: Securinets{BRIDGENAME}
>
>For example Securinets{RUSSKYBRIDGE}

This picture was attached: 

![2022-10-04_20h09_26](https://user-images.githubusercontent.com/68945305/193906228-e6548304-d7ad-4ae9-8bca-1793c060f1c3.png)
### Solution
This is a simple reverse image search task, we can use google's image search (https://images.google.com/) or yandex images ([images.yandex.com](https://yandex.com/images/))

![2022-10-04_20h34_46](https://user-images.githubusercontent.com/68945305/193909616-e3b87cc0-c485-436f-a373-f0486005f8b8.png)
The red building is a hospital named The Lister Hospital, in London, we can get the bridge name from google maps

![2022-10-04_20h38_48](https://user-images.githubusercontent.com/68945305/193910398-e6952de6-a416-4248-9ac4-5641855c9999.png)

Securinets{CHELSEABRIDGE}


## Bus

### Description
>Can you give me the camera model name of the camera that took this picture?
>
>Flag format: Securinets{CAMERAMODEL}

This picture was attached:

![bus (1)](https://user-images.githubusercontent.com/68945305/193913037-827a980c-a285-4083-a709-ad52b5ce3083.jpg)
### Solution
Using exiftool, or Aperi'Solve if you don't have exiftool installed (You can also use other tools to extract exif data it doesn't matter):

![2022-10-04_21h06_30](https://user-images.githubusercontent.com/68945305/193915553-3d3fa19a-46d6-4c44-a0c6-c33ed351d1cb.png)
Securinets{FINEPIX2650}


## File

### Description
>I wonder what this file can contain.

This file was attached: [file.kmz](./file.kmz)

KMZ files are KML files that have been compressed for easier download and distribution. Files with the.kmz extension store the locations of the maps that are used by the Google Earth mapping application.

There is a tool that can help us decompress the KMZ file: https://www.ezyzip.com/open-kmz-file-online.html

![2022-10-04_22h21_56](https://user-images.githubusercontent.com/68945305/193932302-d4381814-6481-4c4b-a834-3dac1658c178.png)
It will extract the KML file.
Since the flag is in the KML file, you can check if its plaintext by strings, you can find the flag. Its the easiest way.

Securinets{kml_m4p5_4r3_1nt3r3st1ng}


## Wireless

### Description
>If i give you the SSID of a wireless router, can you give me the MAC address? SSID: topnet2550
>
>Note: Sometimes you need more than the SSID to find the wireless router because it is not a universally unique ID (Not the case of this task). Flag format: >Securinets{XX:XX:XX:XX:XX:XX}

### Solution
There's a tool named WiGle : https://www.wigle.net/ which helps vizualize and observe networks, you can search wireless routers by SSID in the advanced search:

![2022-10-05_18h49_13](https://user-images.githubusercontent.com/68945305/194127542-5371ba84-0c1a-4f6d-b206-4170c678bb24.png)
Securinets{00:26:91:2C:3F:3F}


## OldTown

### Description
>We are looking for a guy named Jorgan, he is a history enthusiast and he writes articles analyzing historical events. He stated in one of his articles that he chose >to live in a city that attracted him by its architectural remnants as it was spared by World War II bomb raids. This picture was attached to the article. The building >on his right looks like a monument, can you find the city and the number of that building? it would be very helpful.
>
>Flag format: Securinets{CITY_XXX}

This picture was attached:

![oldtown](https://user-images.githubusercontent.com/68945305/194129123-854afe72-30a2-4f08-b524-daae7110796a.png)

There's many ways to solve this challenge, we'll go with the one that focuses on the description.

The description contained many hints: The first one is Jorgan, which is a common German name (You can also find it in other european countries but its rare). The second hint was "city that attracted him by its architectural remnants as it was spared by World War II bomb raids", so the city contains a lot of monuments and it survived the bombings in WWII, when we search cities with these 2 charactetics, we find articles listing many towns, but the best one is this: https://theculturetrip.com/europe/germany/articles/10-facts-about-heidelberg-you-need-to-know/

We can confirm that the city is Heidleberg when reading it, it matches the description.
When we see a list of Heidleberg's monuments, we find what we're looking for, the building is the Heidelberg university library :

![2022-10-05_20h01_16](https://user-images.githubusercontent.com/68945305/194141035-3cdc9935-5616-4377-8f51-e1effb420a65.png)

And the number of the building is: 

![2022-10-05_20h02_34](https://user-images.githubusercontent.com/68945305/194141350-c2a32762-cdb2-43da-995b-d038f5102924.png)

Securinets{HEIDELBERG_107}


## Driver License

### Description
>There is a way to extract information from this destroyed driver license. Can you give me the name of the driver and where he lives?
>
>Flag format: Securinets{FIRSTNAME_LASTNAME_TOWN}

This picture was attached: 

![driverlicense (2)](https://user-images.githubusercontent.com/68945305/194146213-2598fdb1-3be3-4ec7-ae28-2a7b73a42729.png)

### Solution
Scanning the pdf417 code on the driver license with https://products.aspose.app/barcode/recognize/pdf417 we get this (you can cut the barcode from the driver license to scan it alone for better results):

![2022-10-05_20h33_12](https://user-images.githubusercontent.com/68945305/194146869-7f74c893-2c5e-4d50-a464-27128958bb39.png)

@<0xA><0x1E><0xD>ANS­I 636049030002DL004104­66ZN05070057DLDCABCD­E<0xA>DCBBCDEFJKLMW<­0xA>DCDHLPT <0xA>DBA00000000<0xA­>DCSHEATHWAY <0xA>DCTMICHAEL <0xA>DBD00000000<0xA­>DBB00000000<0xA>DBC­1<0xA>DAYAAA<0xA>DAU­ <0xA>DAG123 HEAVEN DRIVE <0xA>DAHAPT. 00 <0xA>DAISYTOWN <0xA>DAJNV<0xA>DAK12­3450000 >><0xA>DAQ123456789123­ <0xA>DCE <0xA>DCF000000000000­0012345671234<0xA>DC­GUSA<0xA>DCHNONE<0xA­>DCK <0xA>DAZABC<0xA>DCU <0xA><0xD>ZNZNAORGAN­ DONOR<0xA>ZNBREVISIO­N DATE00000000<0xA>ZNC­603<0xA>ZND180<0xA><­0xD>

Securinets{MICHAEL_HEATHWAY_DAISYTOWN}


## Relief

### Description
>A friend sent me the geographic coordinates to a relief, it's essentially a scuplture where the sculpted pieces are bonded to a solid background of the same material, >or curved into the material. He told me to guess the name of the artist that designed the square where the relief is placed, what they call the collection of markers >the relief is part of, and the year they were placed in the square. Can you help me? These are the geo coordinates: 41.9022523,12.4570589
>
>Flag format: Securinets{ARTIST_NAMEOFTHECOLLECTION_XXXX}

### Solution
When we search the coordinates on Google maps, they take us to Saint Peter's square:

![2022-10-05_20h10_40](https://user-images.githubusercontent.com/68945305/194142696-dc327d53-4d55-41ae-8d74-d17a47f8bab6.png)

Saint Peter's square is designed by Bernini (Gian Lorenzo Bernini) so that's the first part of the flag.
As the description stated, the geographic coordinates point to the relief, when we open street view, we can see it right in front of us on the floor: 

![2022-10-05_20h24_15](https://user-images.githubusercontent.com/68945305/194145099-edbc2c95-a8fa-45e6-9c9b-4746e6dda2be.png)

Searching "West Ponente Saint Peter's Square", we can find this web page: http://www.stpetersbasilica.info/Exterior/Obelisk/WindRose.htm

![2022-10-05_20h26_01](https://user-images.githubusercontent.com/68945305/194145394-904b6d67-4391-42e8-a8ce-faa4527a862b.png)
![2022-10-05_20h26_32](https://user-images.githubusercontent.com/68945305/194145465-675bf8dd-5beb-4f6c-9d01-98dcc9427c94.png)

The collection name is The Wind Rose, and the date is was placed in the square is 1852.

Securinets{BERNINI_WINDROSE_1852}


## Anonymous 1: 

### Description
>One of our employees recieved an anonymous call, the person pretends that a hacker they're following online hacked our company and leaked something. We don't know yet >if this is true, our security team is searching for any trace of intrusion, but we're counting on you to search this person and see if they're telling the truth. The >phone number used by this person is +46731292127. Which country is the phone number from?
>
>Flag format: Securinets{COUNTRY}

### Solution
+46 -> sweden

Securinets{SWEDEN}


## Anonymous 2:

### Description
>Under which name is the phone number registered?
>
>Flag format: Securinets{FIRSTNAME_LASTNAME}

### Solution
When we search the number on TrueCaller, it is registered under the name Maximiliam Holmberg

![310755563_5253053974822058_5789858062373520615_n](https://user-images.githubusercontent.com/68945305/194151308-7b318ac4-19fe-4a44-aa2e-610d1e2ee1c2.png)

Securinets{MAXIMILIAM_HOLMBERG}


## Anonymous 3: 

### Description
>Can you find which username the person is using for social media accounts? This can be really helpful.
>
>Flag format: Securinets{username}

### Solution

When we get the name, first thing we do is a google search, which gives nothing. Then, we search the name in the popular social media (Facebook, Instagram, Twitter..), we find an Instagram account with his full name.

![2022-10-05_21h24_54](https://user-images.githubusercontent.com/68945305/194156411-63cbda8e-7beb-4bf1-9587-dff6dba32ae1.png)

The username for this account is mholm9851.
In other tasks, if this is a dead end, we can use people search tools, but these will not always give us good results

Securinets{mholm9851}


## Anonymous 4:

### Description
>Where does this person live?
>
>Flag format: Securinets{StreetName_City} 
>
>For example Securinets{Baldersvägen_ Sundsvall}

### Solution
There's a an image in the Instagram account: 

![2022-10-05_21h26_05](https://user-images.githubusercontent.com/68945305/194156616-7040e5d3-55f8-4068-866b-0153629e3222.png)

with the description: “Buying this house is the best choice i made in years!! I wake up to this everyday!”; This is the street that we need to find, and there is a big garden just in front of the house.

We can't get any more informations from the image, downloading it will not help in any way, exif extraction tools, google lence... will not work.
Next thing we can try is see if our guy have made any other social media accounts with that username.

Using WhatsMyName: https://whatsmyname.app/ and NameCheckup: https://namecheckup.com/ we get this:

![2022-10-05_21h35_36](https://user-images.githubusercontent.com/68945305/194158342-2a27c755-441e-42d5-9097-81cce3f95262.png)
![2022-10-05_21h31_54](https://user-images.githubusercontent.com/68945305/194157809-cc5365d8-6586-4eaf-96c2-7ba252c078cc.png)

So there's an empty Reddit account, and a Twitter account that looks promising (The other accounts detected by NameCheckup do not exist).
Scrolling down the Twitter account, we find another post: 

![2022-10-05_21h36_55](https://user-images.githubusercontent.com/68945305/194158593-7ea05b1e-92d8-4bfc-a383-70d17c30e037.png)

From the description, we can safely assume that Maximiliam Holmberg lives 30 minutes away from that location, so the street pictured in the Instagram post is not far from that location: there is 2 options: either he takes 30 minutes walking or driving to get there, a hint was released “Our guy likes to walk long distances” so we go with the first option (without the hint, we can assume that he walked there from the post's description, the choice of words, or we can simply try both options).

First of all, we have to find the place in the twitter picture: a reverse image search is enough: 

![2022-10-05_21h38_24](https://user-images.githubusercontent.com/68945305/194158882-035caec6-919a-479d-abff-f3ca6a4ea714.png)

The picture was taken just in front of the Nordic museum at Djurgårdsvägen, Stockholm.
We need create a 30 minutes raduis around the museum, and search for big gardens:

The first step is to locate the Nordic museum on Google maps and get its geographical coordinates: 

![2022-10-05_21h42_41](https://user-images.githubusercontent.com/68945305/194159550-9122f9e9-5cf6-49e5-8f8e-bf8c3f9a1c08.png)

Second step, we will generate a KML file with KML4EARTH http://kml4earth.appspot.com/tools.html that contains a 30 minutes raduis circle around the Nordic museum, a normal person can walk between 2 and 2.5 Km in 30 minutes so we will put the choose the following parameters: 

![2022-10-05_21h46_37](https://user-images.githubusercontent.com/68945305/194160197-c60b0d5c-78e0-4e2d-a628-f235a626812c.png)

A KML file will be downloaded, you can open it in https://mymaps.google.com , this is the result 

![2022-10-05_21h48_09](https://user-images.githubusercontent.com/68945305/194160547-1325421e-c701-4a49-841f-433f9f3b68d2.png)

In this map, we search for gardens, located near the circle which will not take so much time since we will eliminate many gardens sue to their huge size.
When we find one, we compare the streets around it (with the street view) with the picture we found on Instagram. Obviously we will not check every garden, we have a lot of details in the image that can help us: 

![2022-10-05_21h50_24](https://user-images.githubusercontent.com/68945305/194160923-6b3dbd18-7bec-4dcd-8900-05abbcb4d799.png)
![2022-10-05_21h51_00](https://user-images.githubusercontent.com/68945305/194161011-31ccfd05-ec2f-4226-b5a9-73fb301d1517.png)
![2022-10-05_21h50_43](https://user-images.githubusercontent.com/68945305/194160972-8f01c134-ee61-47c9-bdcd-6ed2a40e632f.png)


Our street is: 
https://earth.google.com/web/search/Mus%c3%a9e+nordique/@59.34201031,18.07693227,18.71720809a,0d,90y,18.67723277h,81.60263484t,0r/data=CigiJgokCSQs2GXsqU1AEaZ_ovNFqE1AGRqf-QwuIDJAIXftV8U2ETJAIhoKFmxNVDVPRHVfQm9wdzEzYXJaYUl3emcQAg

Securinets{Östermalmsgatan_Stockholm}


## Anonymous5:

### Description
>Can you find the username of the hacker he's talking about?
>
>Flag format: Securinets{username}

### Solution
We check who our guy is following on Instagram, we can see some cybersecurity pages but nothing there. 

We go the the Twitter account and do the same but here we find a lot of hackers, one of them “@cyberdef77” has mentioned that he managed to hack a comapny and has a leak that will be posted:

![2022-10-05_21h57_41](https://user-images.githubusercontent.com/68945305/194162248-cc51ccb0-3370-4703-ad70-6fda9c5e8d80.png)
![2022-10-05_21h58_18](https://user-images.githubusercontent.com/68945305/194162330-4fc63986-b452-49bf-acb5-1b6443e1b7ee.png)

This is our hacker!

Securinets{cyberdef77}


## Anonymous6:

### Description
>Can you find what the hacker leaked?

### Solution
The hacker mentioned that he will post the leak “tomorrow” on september the 15th, but we can't find it.
There is another post that says:

![2022-10-05_21h59_39](https://user-images.githubusercontent.com/68945305/194162535-c156ee41-47e4-4138-bfcd-8429d8bf2f8a.png)

The hacker deleted the leak, but we can get is with a wayback machine http://web.archive.org/ : 

![2022-10-05_22h05_21](https://user-images.githubusercontent.com/68945305/194163536-ec5bfe71-d0c3-4bc9-afd6-f62ef0e61620.png)

The snapshot form 18 sep 2022 contains a deleted tweet: 

![2022-10-05_22h07_39](https://user-images.githubusercontent.com/68945305/194163933-07868c17-23e0-4d72-9f7a-a1af4ca595eb.png)

Its a base64 string, decoding it gives us the flag:

Securinets{S0c14l_m3d14_OSINT_y'4ll_02445126634759200754556}
