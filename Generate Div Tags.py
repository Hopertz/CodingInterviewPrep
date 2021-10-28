"""
     Generate Div Tags ☆
   Write a function that takes in a positive integer numberOfTags and returns a list of all the valid strings that you can
   generate with that number of matched <div></div> tags.
   A string is valid and contains matched <div></div> tags if for every opening tag <div> , there's a closing tag </div>
   that comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should
   contain exactly numberOfTags opening tags and numberOfTags closing tags.["<div></div><div></div>",

   For example, given numberOfTags = 2, the valid strings to return would be: "<div><div></div></div>"] .
   Note that the output strings don't need to be in any particular order.

   Sample Input
     numberOfTags = 3

   Sample Output
     [
       "<div><div><div></div></div></div>",
       "<div><div></div><div></div></div>",
       "<div><div></div></div><div></div>",
       "<div></div><div><div></div></div>",
       "<div></div><div></div><div></div>",
     ] // The strings could be ordered differently.

"""
# SOLUTION 1

# 0((2n)!/((n!((n + 1)!)))) time | ((2n)!/((n!((n + 1)!)))) space -
# where n is the input number
def generateDivTags(numberOfTags):
    matchedDivTags = []
    generateDivTagsFromPrefix(numberOfTags, numberOfTags,"", matchedDivTags)
    return matchedDivTags

def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded - 1, closingTagsNeeded, newPrefix, result)

    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded - 1, newPrefix, result)

    if closingTagsNeeded == 0:
        result.append(prefix)
