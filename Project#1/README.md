### <center>*SDLC FILE*</center>
## <center>First Project</center>  
____________________________________________________________________________
#### <ins>The Current problem:</ins>
we will receive an encrypted string that should be decrypted using a specific logic to replace specific letters. 

#### <ins>The plan:</ins>  
we have requirements to follow in order to solve the problem successfully, and they're the following:

- find the most 4 common letters in the encrypted text and replace them with the 4 most common letters in English; e,t,o,r  
then find the logic that connects the common letters in the text and in English.


- replace the characters in the encrypted text according to the logic we found in part1.


- after we decrypted the text, we should append the decrypted text to the original one.  
also create a new results file and write in it only the decrypted text.


- find the longest word in the text, find the number of lines in the text.
and print the longest word by the number of lines.  
and lastly print a pattern in the end of the original file.  

- to summary everything, create a README file and do SDLC.

#### <ins>The design:</ins>  
- made a file and added the encrypted text to it.  
  - defined a function to find the most 4 common letters in the encrypted text.  
  -  counted the appearance of each letter in the text.  
  - sorted and replaced the 4 most common letters in the text with the 4 most common letters in English; (e,t,o,r).  
  - with a function, found the dictionary that contains the logic that connects the common letters in the text and in English.
>used only alpha characters, the code is designed to be case-sensitive.  


- replaced the characters in the encrypted text according to the logical dictionary we found in part 1.  


- after we decrypted the text, we appended the decrypted text to the file that contains the original one.  
also created a new results file and wrote in it only the new decrypted text.


- defined two new functions;
  - function1: found the longest word in the results.
  - function2: found the number of lines in the results file.
  - additionally we defined a new function that called main, which printed the longest word multiplied by the number of lines.  
  - lastly, draw the required pattern in the end of the original file.

