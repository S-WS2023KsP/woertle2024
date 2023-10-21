#!/usr/bin/python3
'''
This program takes multiple strings from a file as an input and saves it to a list.
This list is then sorted and printed
'''

license = 'public Domain'
author = 'Patrick Weber'
scriptDate = '2023-10-21'
scriptName = 'Woertle_Uebung'
scriptVersion = '3.0'

filename = 'Testdatei.txt'
outputFilename = 'Outputdatei.txt'
specialCharSet = {'*', '&', '+', '-', '[', ']', '{', '}', '@', '$', '#', "'", '"'}
grammaticalCharSet = {',', '.', '?', '(', ')', '!', '/', ';', ':'}
inputList = []
wordDict = dict()
fileLineNumber = 0

inputFile = open(filename, "r", encoding='UTF-8')
print(f"Datei {filename} wurde geöffnet", end='')

for line in inputFile:

    fileLineNumber += 1

    cleanedLine = line

    # replace grammatical Characters with a Space
    for character in grammaticalCharSet:
        cleanedLine = cleanedLine.replace(character, ' ')
                                                                                                    #print(cleanedLine)
    inputList.extend(cleanedLine.strip().split())

inputFile.close()
print(f", {fileLineNumber} Zeilen gelesen")

for word in inputList:
    cleanedWord = word

    # remove special Characters                                                                     #print(cleaned_word)
    for character in specialCharSet:
        cleanedWord = cleanedWord.replace(character, '')

    if len(cleanedWord) > 5:
        continue

    if len(cleanedWord) < 5:
        continue

    if cleanedWord in wordDict:
        wordDict[cleanedWord] += 1
        continue
    wordDict[cleanedWord] = 1
                                                                                        #print(wordDict)
                                                                                        #print(wordDict)
outputFile = open(outputFilename, 'w')
numberOfLinesWriten = 0
for word in wordDict.keys():
    outputFile.write(word + "\n")
    numberOfLinesWriten += 1

outputFile.close()
print(f"{numberOfLinesWriten} Worte geschrieben in Datei {outputFilename}")
