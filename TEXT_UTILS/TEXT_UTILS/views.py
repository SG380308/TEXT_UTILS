# # I HAVE CREATED THIS FILE

# #from django.http import HttpResponse

# # LECTURE 7

# # def INDEX(request):
# #     return HttpResponse('''<h1> INDEX </h1> 
# #                         <a href= "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> DJANGO CODE WITH SAJAL </a><br>
# #                         <a href="https://www.facebook.com/"> FACEBOOK </a> <br>
# #                         <a href="https://www.flipkart.com/"> FLIPKART </a> <br>
# #                         <a href="https://www.hindustantimes.com/"> NEWS </a> <br>
# #                         <a href="https://www.google.com/"> GOOGLE </a> <br>''')

# # def ABOUT(request):
# #     return HttpResponse("ABOUT PAGE")
                     

# # LECTURE 8

# # from django.http import HttpResponse


# # def INDEX(request):
# #     return HttpResponse('''<h1> HOME </h1> 
# #                         <a href= "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> DJANGO CODE WITH SAJAL </a><br>
# #                         <a href="https://www.facebook.com/"> FACEBOOK </a> <br>
# #                         <a href="https://www.flipkart.com/"> FLIPKART </a> <br>
# #                         <a href="https://www.hindustantimes.com/"> NEWS </a> <br>
# #                         <a href="https://www.google.com/"> GOOGLE </a> <br>''')
                     

# # def REMOVE_PUNCTUATION(request):
# #     return HttpResponse("REMOVE_PUNCTUATION <a href='/'>BACK</a>")
# # def CAPITALIZE_FIRST(request):
# #     return HttpResponse("CAPITALIZE_FIRST <a href='/'>BACK</a>")
# # def NEW_LINE_REMOVE(request):
# #     return HttpResponse("NEW_LINE_REMOVE <a href='/'>BACK</a>")
# # def SPACE_REMOVE(request):
# #     return HttpResponse("SPACE_REMOVE <a href='/'>BACK</a>")
# # def CHAR_COUNT(request):
# #     return HttpResponse("CHAR_COUNT <a href='/'>BACK</a>")



# # LECTURE 9

# # from django.http import HttpResponse
# # from django.shortcuts import render


# # def INDEX(request):
# #     # DICTIONARY = {'NAME':'HARRY' , 'PLACE':'MARS'}
# #     return render (request , 'INDEX.HTML' , DICTIONARY)
# #     # return HttpResponse("<h1> HOME </h1>" )
# # def REMOVE_PUNCTUATION(request):
# #   # GET THE TEXT 
#     # DJANGO_TEXT = (request.GET.get('TEXT' , 'DEFAULT'))
#     # print(DJANGO_TEXT)
# #     return HttpResponse("REMOVE_PUNCTUATION <a href='/'>BACK</a>")
# # def CAPITALIZE_FIRST(request):   
# #     return HttpResponse("CAPITALIZE_FIRST <a href='/'>BACK</a>")
# # def NEW_LINE_REMOVE(request):
# #     return HttpResponse("NEW_LINE_REMOVE <a href='/'>BACK</a>")
# # def SPACE_REMOVE(request):
# #     return HttpResponse("SPACE_REMOVE <a href='/'>BACK</a>")
# # def CHAR_COUNT(request):
# #     return HttpResponse("CHAR_COUNT <a href='/'>BACK</a>")


# from django.http import HttpResponse
# from django.shortcuts import render


# def INDEX(request):
#     # DICTIONARY = {'NAME':'HARRY' , 'PLACE':'MARS'}
#     return render (request , 'INDEX.HTML')
#     # return HttpResponse("<h1> HOME </h1>" )

# def SUBMIT(request):    
#     # GET THE TEXT 
#     DJANGO_TEXT = request.GET.get('TEXT', 'DEFAULT')
#     print(DJANGO_TEXT)

#     # CHECK IF THE "REMOVE PUNCTUATION" CHECKBOX IS CHECKED
#     REMOVE_PUNCTUATION = request.GET.get('REMOVE_PUNCTUATION', 'OFF')
#     print(REMOVE_PUNCTUATION)

#     UPPERCASE = request.GET.get('UPPERCASE', 'OFF')
#     print(UPPERCASE)

#     # SUBMITTED = DJANGO_TEXT
#     if REMOVE_PUNCTUATION == "ON":
#         PUNCTUATION_LIST = "!',@,#,$,%,&,*,(,),;"
#         SUBMITTED = ""
#         PREV_CHAR = ""

#         for char in DJANGO_TEXT:
#             # CHECK IF THE CHARACTER IS NOT IN THE PUNCTUATION LIST 
#             if char not in PUNCTUATION_LIST:
#                 # APPEND THE CHARACTER TO THE RESULT
#                 SUBMITTED += char
#                 PREV_CHAR = char
#             elif char == " " and PREV_CHAR != " ":
#                 # ADD A SINGLE SPACE BETWEEN WORDS IF THE PREVIOUS CHARACTER WAS NOT A SPACE
#                 SUBMITTED += " "
#                 PREV_CHAR = char

#         DICTIONARY = {'PURPOSE': 'REMOVE_PUNCTUATION', 'SUBMITTED_TEXT': SUBMITTED}
#         # SUBMIT THE TEXT
#         return render(request, 'SUBMIT.HTML', DICTIONARY)
#     elif UPPERCASE == "ON":
#         SUBMITTED = ""
#         for char in DJANGO_TEXT:
#             SUBMITTED += char.upper()

#         DICTIONARY = {'PURPOSE': 'CHANGED TO UPPERCASE', 'SUBMITTED_TEXT': SUBMITTED}
#         # SUBMIT THE TEXT
#         return render(request, 'SUBMIT.HTML', DICTIONARY)
#     else:
#         return HttpResponse("ERROR")


from django.http import HttpResponse
from django.shortcuts import render

def INDEX(request):
    return render(request, 'INDEX.HTML')

def SUBMIT(request):    
    # GET THE TEXT 
    DJANGO_TEXT = request.GET.get('TEXT', '')

    # CHECK IF THE "REMOVE PUNCTUATION" CHECKBOX IS CHECKED
    REMOVE_PUNCTUATION = request.GET.get('REMOVE_PUNCTUATION', False)

    # CHECK IF THE "UPPERCASE" CHECKBOX IS CHECKED
    UPPERCASE = request.GET.get('UPPERCASE', False)

    # CHECK IF THE "NEW_LINE_REMOVER" CHECKBOX IS CHECKED
    NEXT_LINE_REMOVER = request.GET.get('NEXT_LINE_REMOVER', False)

    # CHECK IF THE "EXTRA_SPACE_REMOVER" CHECKBOX IS CHECKED
    EXTRA_SPACE_REMOVER = request.GET.get('EXTRA_SPACE_REMOVER', False)

    # CHECK IF THE "LENGTH_COUNT" CHECKBOX IS CHECKED
    CHARACTERS_COUNTER = request.GET.get('CHARACTERS_COUNTER', False)

    # PROCESS THE TEXT BASED ON CHECKBOX SELECTIONS
    if REMOVE_PUNCTUATION:
        import string
        DJANGO_TEXT = DJANGO_TEXT.translate(str.maketrans('', '', string.punctuation))

    if UPPERCASE:
        DJANGO_TEXT = DJANGO_TEXT.upper()
    
    if NEXT_LINE_REMOVER:
        DJANGO_TEXT = DJANGO_TEXT.replace("\n" , "")

    if EXTRA_SPACE_REMOVER:
        DJANGO_TEXT = DJANGO_TEXT.strip() 

    if CHARACTERS_COUNTER:
        DJANGO_TEXT =len( DJANGO_TEXT) 

    # CHECK IF NO CHECKBOX ARE CHECKED
    if not REMOVE_PUNCTUATION and not UPPERCASE and not NEXT_LINE_REMOVER and not EXTRA_SPACE_REMOVER and not CHARACTERS_COUNTER :
        return HttpResponse("ERROR: PLEASE SELECT AT LEAST ONE OPTION.")
   



    DICTIONARY = {'PURPOSE': 'TEXT MODIFICATION', 'SUBMITTED_TEXT': DJANGO_TEXT}
    return render(request, 'SUBMIT.HTML', DICTIONARY)


    
    










