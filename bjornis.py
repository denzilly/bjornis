#!/usr/bin/env python
# encoding: utf-8


import random


#mode = input("Weird mode? (y/n)")


#Weird characters



def namegen():

    mode = 1

    replacers = ["a","e","o","i","b"]



    #Suffixes
    prefixes = ["b","k","d","s"]
    core = ["orn","an","arn","ern","enn","ann","urn","oon","ork","ark",]
    suffixes = ["ise","is","es","ese","os","i","o"]

    prefix = prefixes[random.randint(0,len(prefixes)-1)]

    suffix = suffixes[random.randint(0,len(suffixes)-1)]

    core = core[random.randint(0,len(core)-1)]



    if(random.randint(0,1)) == 1:
        prefix = ""
    if(random.randint(0,1)) == 1:
        suffix = ""

    name = prefix + "j" + core + suffix


    if mode == 0:
        count = 0
        for x in name:
            if x in replacers:


                name = replace(name, x, count)
            count += 1


    print(name)
    #print(pyfiglet.figlet_format(name))

def replace(name, letter, count):

    a = ["à","á","â","ã","ä","å","æ"]
    e = ["è","é","ê","ë"]
    o = ["ò","ó","ô","õ","ö","ø"]
    i = ["ì","í","î","ï","ÿ"]
    b = ["ß"]


    if letter == "a":
        name = name[:count] + a[random.randint(0,len(a)-1)] + name[count+1:]
        print("letter is a")
        print(name)
    if letter == "e":
        name = name[:count] + e[random.randint(0,len(e)-1)] + name[count+1:]
        print("letter is e")
        print(name)
    if letter == "o":
        name = name[:count] + o[random.randint(0,len(o)-1)] + name[count+1:]
        print("letter is o")
        print(name)
    if letter == "i":
        name = name[:count] + i[random.randint(0,len(i)-1)] + name[count+1:]
    if letter == "b":
        name = name[:count] + b[random.randint(0,len(b)-1)] + name[count+1:]

    return(name)

def namegen_weird():

    mode = 1

    replacers = ["a","e","o","i","b"]



    #Suffixes
    prefixes = ["b","k","d","s"]
    core = ["orn","an","arn","ern","enn","ann","urn","oon","ork","ark",]
    suffixes = ["ise","is","es","ese","os","i","o"]

    prefix = prefixes[random.randint(0,len(prefixes)-1)]

    suffix = suffixes[random.randint(0,len(suffixes)-1)]

    core = core[random.randint(0,len(core)-1)]



    if(random.randint(0,1)) == 1:
        prefix = ""
    if(random.randint(0,1)) == 1:
        suffix = ""

    name = prefix + "j" + core + suffix


    if mode == 1:
        count = 0
        for x in name:
            if x in replacers:


                name = replace(name, x, count)
            count += 1


    #print(name)
    print(name)

def replace(name, letter, count):

    a = ["à","á","â","ã","ä","å","æ"]
    e = ["è","é","ê","ë"]
    o = ["ò","ó","ô","õ","ö","ø"]
    i = ["ì","í","î","ï","ÿ"]
    b = ["ß"]


    if letter == "a":
        name = name[:count] + a[random.randint(0,len(a)-1)] + name[count+1:]

    if letter == "e":
        name = name[:count] + e[random.randint(0,len(e)-1)] + name[count+1:]

    if letter == "o":
        name = name[:count] + o[random.randint(0,len(o)-1)] + name[count+1:]

    if letter == "i":
        name = name[:count] + i[random.randint(0,len(i)-1)] + name[count+1:]
    if letter == "b":
        name = name[:count] + b[random.randint(0,len(b)-1)] + name[count+1:]

    return(name)


while(True):
    mode = input("Weird mode on (y/n)?")
    if mode == "n":
        while(True):
            input("")
            print("Hello, my name is:")
            namegen()
    if mode == "y":
        while(True):
            input("")
            print("Hello, my name is:")
            namegen_weird()
