'''Expert system that can learn if it comes to something it does not know.'''

animalTree = ['Does it live on land?',  # equivalent to expert.html example
               ['Is it covered with fur?',
                 ['Does it bark?',
                   ['dog'],
                   ['cat']
                 ],
                 ['spider']
               ],
                ['Does it have webbed feet?',
                  ['duck'],
                  ['goldfish']
                ]
             ]
def expert(tree):
    '''tree is an expert system composed of nested lists.
    The innermost lists have just a single element,
       an answer.
    Other lists have three parts:
       a question,
       a subtree to check if the answer to the queston is yes, and
       a subtree to check if the answer to the question is no.
    The system may supply the correct answer after a number of questions.
    If the answer is wrong, the tree is extended with the help of the user.
    '''
    currentNode = tree
    while len(currentNode) == 3:
        [question, yesNode, noNode] = currentNode # name the parts of the list
        if agree(question):
            currentNode = yesNode
        else: 
            currentNode = noNode
    # When the while loop is over, currentNode is a leaf with a single element.       
    [result] = currentNode
    if agree("Is it a {}?".format(result)):
        print("I figured that out!")
    else: 
        newResult = input("So what WERE you thinking of? ")
        newQuestion = input('What question could I ask that is TRUE for a\n'+
                            '  {} but not for a {}? '.format(result, newResult))
        newYesNode = [result]
        newNoNode = [newResult]
        #currentNode[:] =... replaces the entire contents of currentNode
        currentNode[:] = [newQuestion, newYesNode, newNoNode] 
        print("Thank you for teaching me something new!")

def agree(question):
    '''return True if user agrees.'''
    answer = input(question + ' (y/n) ')
    return answer.startswith('y')

def prettyStr(tree, indent='', dif='  '):
    '''Each node shows the question or answer first.
    If there further lists for yes and no responses,
    they are both further indented by dif, with any
    further child nodes further indented...'''
    if len(tree) == 1:
        return indent + repr(tree) #repr(string) -> quoted form used in programs
    [question, t1, t2] = tree
    t1Str = prettyStr(t1, indent+dif)
    t2Str = prettyStr(t2, indent+dif)
    return '''{indent}[{question!r},
{t1Str},
{t2Str}
{indent}]'''.format(**locals())

def main():
    fileName = input('Enter the name of a file containing an expert system,\n'+
                     '  or just press Enter to use the simple animal example: ')
    if not fileName:
        tree = animalTree
        fileName = 'animalExpert.txt'
    else:
        tree = eval(fileToStr(fileName)) #eval evaluates a string expression
    print("\nUsing this expert system tree:\n")
    print(prettyStr(tree))
    more = True
    while more:
        expert(tree)
        more = agree('\nDo you want to use the expert system some more?')
    print("\nThe expert system tree is now:\n")
    print(prettyStr(tree))    
    saveTree(tree, fileName)
    
def saveTree(tree,fileName):
    '''Options for saving the expert tree, pretty formatted:
       Just press Enter to save to {fileName},
       or enter a new filename,
       or respond with / to cancel saving.  ?:  '''
    ans = input(saveTree.__doc__.format(**locals())).strip()
    if ans and ans in '/\\':
        print('Nothing saved.')
    else:
        if ans:
            fileName = ans
        strToFile(prettyStr(tree), fileName) # could use just repr(tree)
        print('File', fileName, 'saved.')    # prettyStr formats for humans

# old functions from tutorial      
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

if __name__ == '__main__':
    main()


                         