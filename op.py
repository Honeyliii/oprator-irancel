shomareh= input("code dastore")
if shomareh=="*555#":
    while True:
        print("0-takmile kharid")
        print("1-hesab")
        print("5-internet hamrah")
        print("8-internet sabet")
        print("14-pishnahade shakhsi")
        print("00-badi")
        entekhab=int(input("entekhab konid:"))
        match entekhab:
            case 0:
                print("shoma hich tarakoneshi nadarid")
                break
        entekhab=int(input("entekhab konid:"))

        match entekhab:    
            case 1:
                print("5- tekrar akharin tarakonesh")
                print("1-sharje")
                print("2-sorathsab va pardakhti")
                print("khat be khat")
                print("00-badi")
                entekhab=int(input("entekhab konid:"))
                match entekhab:
                    case 5:
                        print(" in serves baray moshtariyani ast ke dar30 roze akhir kharid karde bashand")
                        break
                match entekhab:    
                    case 1:    
                        print("1-kharid online  sharje etebari")
                        print("2-karte sharje moshakhas")
                        print("3-vrodekarte sharj")
                match entekhab:        
                    case 5:
                        print("internet")    
                        print("14-pishnahad shakhsi")
                        print("3-30 roze")
                        print("13-15 roze")
                        print("2-7 roze")
                        print("1-1 roze")
                        print("00-badi")
                        entekhab=int(input("entekhab konid:"))
                match entekhab:    
                    case 8:
                        
                        print("1-baste 7roze")   
                        print("2-baste 30roze")
                        print("3-baste 90reze")
                        print("4-baste 180roze")
                        print("5-baste 365roze")
                        print("00-badi")
                        entekhab=int(input("entekhab konid:"))
                match entekhab:        
                    case 14:
                        
                        print("pshanahad dagh data")
                        print("1-mokaleme")
                        print("2-internet")
                        entekhab=int(input("entekhab konid:"))
                match entekhab:                
                    case 00:
                        print("22-peigiri sefsresh")    
                        print("6-scan it")
                        print("3-tarh ha")
                        print("4-setting")
                        print("01-ghabli")
                        print("00-badi")
                        entekhab=int(input("entekhab konid:"))
                match entekhab:
                    case 22:
                        code_peigiri=int(input("code paigiri ra nared konid"))
                        print(code_peigiri)

                        continue
                match entekhab:    
                    case 6:
                        print("1-ghlbi bray bordan:10jayeza200mil")
                        print("2-20jayeze 10mil")   
                        print("00-badi")
                match entekhab:        
                    case 3:
                        print("tarh tarefeh")    
                        print("2-tarhehay mahane")
                        print("3-contorol masraf internet binolmelali")
                        print("00-badi")
                match entekhab:        
                    case 4:
                                 
                        print("sting")    
                        print("2-internet")
                        print("3-language")
                        print("4-rahnam")
                        print("00-badi")
                        entekhab = int(input('staing'))
                        match entekhab:
                            case 3:
                                print("1-farsi")
                                print("2-english")
                                lang = int(input('zaban ra entekhab konid'))
                                match lang:
                                    case 1:
                                        print('farsi entekhab shod')
                                    case 2:
                                        print('engilsh eelected')    
                                
                   
                        